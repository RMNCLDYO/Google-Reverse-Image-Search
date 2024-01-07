import time
import logging
import requests
from bs4 import BeautifulSoup
from typing import Dict, Optional
from urllib.parse import quote, urlparse

logging.basicConfig(
    filename='error.log',
    level=logging.INFO,
    format='%(asctime)s | [%(levelname)s]: %(message)s',
    datefmt='%m-%d-%Y / %I:%M:%S %p'
)

class SearchResults:
    def __init__(self, results):
        self.results = results

    def __str__(self):
        output = ""
        for result in self.results:
            output += "---\n"
            output += f"Title: {result.get('title', 'Title not found')}\n"
            output += f"Link: {result.get('link', 'Link not found')}\n"
            output += "---\n"
        return output

class GoogleReverseImageSearch:
    def __init__(self):
        self.base_url = "https://www.google.com/searchbyimage"
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
        self.retry_count = 3
        self.retry_delay = 1

    def response(self, query: str, image_url: str, max_results: int = 10, delay: int = 1) -> SearchResults:
        self._validate_input(query, image_url)
        
        encoded_query = quote(query)
        encoded_image_url = quote(image_url)

        url = f"{self.base_url}?q={encoded_query}&image_url={encoded_image_url}&sbisrc=cr_1_5_2"

        all_results = []
        start_index = 0

        while len(all_results) < max_results:
            if start_index != 0:
                time.sleep(delay)
                
            paginated_url = f"{url}&start={start_index}"

            response = self._make_request(paginated_url)
            if response is None:
                break

            search_results, valid_content = self._parse_search_results(response.text)
            if not valid_content:
                logging.warning("Unexpected HTML structure encountered.")
                break

            for result in search_results:
                if len(all_results) >= max_results:
                    break
                data = self._extract_result_data(result)
                if data and data not in all_results:
                    all_results.append(data)

            start_index += (len(all_results)-start_index)

        if len(all_results) == 0:
            logging.warning(f"No results were found for the given query: [{query}], and/or image URL: [{image_url}].")
            return "No results found. Please try again with a different query and/or image URL."
        else:
            return SearchResults(all_results[:max_results])
    
    def _validate_input(self, query: str, image_url: str):
        if not query:
            raise ValueError("Query not found. Please enter a query and try again.")
        if not image_url:
            raise ValueError("Image URL not found. Please enter an image URL and try again.")
        if not self._validate_image_url(image_url):
            raise ValueError("Invalid image URL. Please enter a valid image URL and try again.")
    
    def _validate_image_url(self, url: str) -> bool:
        parsed_url = urlparse(url)
        path = parsed_url.path.lower()
        valid_extensions = (".jpg", ".jpeg", ".png", ".webp")
        return any(path.endswith(ext) for ext in valid_extensions)
    
    def _make_request(self, url: str):
        attempts = 0
        while attempts < self.retry_count:
            try:
                response = requests.get(url, headers=self.headers)
                if response.headers.get('Content-Type', '').startswith('text/html'):
                    response.raise_for_status()
                    return response
                else:
                    logging.warning("Non-HTML content received.")
                    return None
            except requests.exceptions.HTTPError as http_err:
                logging.error(f"HTTP error occurred: {http_err}")
                attempts += 1
                time.sleep(self.retry_delay)
            except Exception as err:
                logging.error(f"An error occurred: {err}")
                return None
        return None

    def _parse_search_results(self, html_content: str) -> (Optional[list], bool):
        try:
            soup = BeautifulSoup(html_content, "html.parser")
            return soup.find_all('div', class_='g'), True
        except Exception as e:
            logging.error(f"Error parsing HTML content: {e}")
            return None, False

    def _extract_result_data(self, result) -> Dict:
        link = result.find('a', href=True)['href'] if result.find('a', href=True) else None
        title = result.find('h3').get_text(strip=True) if result.find('h3') else None
        return {"link": link, "title": title} if link and title else {}
