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
- `Python 3.x`

## Dependencies
The following Python packages are required:
- `requests`: For making HTTP requests to Google.
- `beautifulsoup4` library for parsing the results.

## Installation
Clone the repository and install the required dependencies:
```bash
git clone https://github.com/RMNCLDYO/Google-Reverse-Image-Search.git
cd Google-Reverse-Image-Search
pip install -r requirements.txt
```

## Usage
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

## Delay Parameter

The response method includes an optional `delay` parameter, designed to manage the rate of search requests. This feature is particularly useful to prevent overwhelming the server with rapid successive requests, which could potentially trigger rate limiting or temporary blocking by Google's servers.

The `delay` parameter specifies the number of `seconds` to wait before making each new page request. This delay is applied only when fetching subsequent pages, not on the first request. It's an optional parameter, and if not set, defaults to 1 second.

To use the delay feature, set the `delay` parameter in the response method:

```python
response = request.response(
    query="Example Query",
    image_url="https://example.com/image.jpg",
    max_results=10,
    delay=5 # Wait for 5 seconds before each request
)
```

## Contributing
Contributions are welcome!

Please refer to [CONTRIBUTING.md](.github/CONTRIBUTING.md) for detailed guidelines on how to contribute to this project.

## Reporting Issues
Encountered a bug? We'd love to hear about it. Please follow these steps to report any issues:

1. Check if the issue has already been reported.
2. Use the [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md) template to create a detailed report.
3. Submit the report [here](https://github.com/RMNCLDYO/Google-Reverse-Image-Search/issues).

Your report will help us make the project better for everyone.

## Feature Requests
Got an idea for a new feature? Feel free to suggest it. Here's how:

1. Check if the feature has already been suggested or implemented.
2. Use the [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md) template to create a detailed request.
3. Submit the request [here](https://github.com/RMNCLDYO/Google-Reverse-Image-Search/issues).

Your suggestions for improvements are always welcome.

## Versioning and Changelog
Stay up-to-date with the latest changes and improvements in each version:

- [CHANGELOG.md](.github/CHANGELOG.md) provides detailed descriptions of each release.

## Security
Your security is important to us. If you discover a security vulnerability, please follow our responsible disclosure guidelines found in [SECURITY.md](.github/SECURITY.md). Please refrain from disclosing any vulnerabilities publicly until said vulnerability has been reported and addressed.

## License
Licensed under the MIT License. See [LICENSE](LICENSE) for details.
