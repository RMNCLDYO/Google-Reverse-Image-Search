<p align="center">
    <a href="https://python.org" title="Go to Python homepage"><img src="https://img.shields.io/badge/Python-&gt;=3.x-blue?logo=python&amp;logoColor=white" alt="Made with Python"></a>
</p>

<p align="center">
    <img src="https://img.shields.io/badge/maintained-yes-2ea44f" alt="maintained - yes">
    <a href="/CONTRIBUTING.md" title="Go to contributions doc"><img src="https://img.shields.io/badge/contributions-welcome-2ea44f" alt="contributions - welcome"></a>
</p>

<p align="center">
    <a href="https://pypi.org/project/requests"><img src="https://img.shields.io/badge/dependency-requests-critical" alt="dependency - requests"></a>
    <a href="https://pypi.org/project/beautifulsoup4"><img src="https://img.shields.io/badge/dependency-beautifulsoup4-critical" alt="dependency - beautifulsoup4"></a>
</p>

<p align="center">
    <img width="700" src="https://raw.githubusercontent.com/RMNCLDYO/Google-Reverse-Image-Search/main/.github/logo.png">
</p>

<p align="center">
    <img src="https://img.shields.io/badge/dynamic/json?label=Google+Reverse+Image+Search&query=version&url=https%3A%2F%2Fraw.githubusercontent.com%2FRMNCLDYO%2FGoogle-Reverse-Image-Search%2Fmain%2F.github%2Fversion.json" alt="Version">
</p>

## Overview
Google Reverse Image Search is an open-source Python library designed for leveraging Google's search by image capabilities to perform reverse image searches programatically. This tool is particularly useful for applications like verifying the source of an image, finding higher resolution versions, or identifying the content and context of an image. It's designed for developers, researchers, and hobbyists who require an automated, programmatic way to perform reverse image searches.

## Key Features
- Automated reverse image searches using Google's search by image feature.
- Customizable search queries, delays and result limits.
- Parses and formats search results, including titles and links.
- Built-in error handling and logging.

## Prerequisites
- Python 3.x
- `requests` library
- `beautifulsoup4` library for HTML parsing

## Installation
Clone the repository and install the required dependencies:
```bash
git clone https://github.com/RMNCLDYO/Google-Reverse-Image-Search.git
cd Google-Reverse-Image-Search
pip install -r requirements.txt
```

## Dependencies
The tool requires the following Python packages:
- `requests`
- `beautifulsoup4`

## Usage

To use the Google Reverse Image Search module, follow these steps:

1. Import the module:
```python
from reverse_image_search import GoogleReverseImageSearch
```

2. Create an instance of `GoogleReverseImageSearch`:
```python
request = GoogleReverseImageSearch()
```

3. Perform a search by calling the `response` method with the query, image URL, and the number of results:
```python
response = request.response(
    query="<your-query>",
    image_url="<image-url>",
    max_results=5
)
```

4. Print or process the results as needed:
```python
print(response)
```

## Delay Feature

The response method includes an optional `delay` parameter, designed to manage the rate of search requests. This feature is particularly useful to prevent overwhelming the server with rapid successive requests, which could potentially trigger rate limiting or temporary blocking by Google's servers.

The `delay` parameter specifies the number of `seconds` to wait before making each new page request. This delay is applied only when fetching subsequent pages, not on the first request. It's an optional parameter, and if not set, defaults to 1 second.

To use the delay feature, set the `delay` parameter in the response method:

```python
response = request.response(
    query="<your-query>",
    image_url="<image-url>",
    max_results=10,
    delay=5 # Wait for 5 seconds before each request
)
```

## Example

Here is an example of how to use the module:
```python
from reverse_image_search import GoogleReverseImageSearch

request = GoogleReverseImageSearch()

response = request.response(
    query="Example Query",
    image_url="https://example.com/image.jpg",
    max_results=5
)

print(response)
```

## Contributing
Contributions are welcome. Please follow the guidelines in our [CONTRIBUTING.md](.github/CONTRIBUTING.md).

## Reporting Issues
Report issues via the GitHub issue tracker.

## License
Licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
