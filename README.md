# YouTube Video Information Scraper API

This API allows users to fetch information about YouTube videos based on search keywords using web scraping techniques.

## Endpoints

### Search Videos

- **Endpoint:** `/get`
- **Method:** `GET`
- **Parameters:**
  - `query`: Search keywords
  - Additional optional parameters (e.g., max results, order)(upcomming version)
- **Response:** JSON with video information (title, description, views, likes, etc.)

Example:

```bash
curl -X GET 'https://youtube-search-api-eta.vercel.app/get?query=aradhya'
```

# Getting Started
- **Clone the repository:**
    ```bash
    git clone https://github.com/chintamani-pala/youtube-search-api.git
    cd youtube-search-api
    ```
- **Install dependencies:**
     ```bash
    pip install -r requirements.txt
    ```
- **Run the Flask application:**
     ```bash
    python index.py
    ```
# Usage
- Make GET requests to the /search endpoint with the necessary parameters.
- Receive JSON responses containing video information based on the provided search query using web scraping techniques.
# Technologies Used
- Python
- Flask
- Web Scraping (Beautiful Soup, Requests or other relevant libraries)
# Note
 **Web scraping YouTube might violate their terms of service. Use this API responsibly and be aware of potential legal and ethical implications.**
# Contributing
  **Contributions are welcome! Fork the repository, make your changes, and create a pull request for review.**
# License
**This project is licensed under the MIT License.**
