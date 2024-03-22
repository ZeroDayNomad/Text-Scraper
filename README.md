# Text Scraper

## Overview
The Text Scraper is a Python script designed to extract text content from a specified website and convert it into a well-formatted PDF document. This tool is particularly useful for users who want to save the textual content of web articles, blog posts, or other online resources for offline reading or archiving purposes.

## How It Works
- **User Input:** The script begins by prompting the user to provide the URL of the website they wish to scrape. This URL can be any webpage that contains text content, such as news articles, blog posts, or informative web pages.
- **Web Scraping:** The script uses the requests library to send a GET request to the provided URL, retrieving the webpage's HTML content. It then employs the BeautifulSoup library to parse the HTML and extract the text content.
- **PDF Generation:** After extracting the text content, the script utilizes the reportlab library to create a PDF document. It defines the document's structure, styles, and layout.
- **Text Formatting:** The scraped text is organized into paragraphs, and appropriate line breaks and spacing are added to maintain readability. The title of the webpage is set as the PDF's title and displayed in a bold font.
- **PDF Saving:** Finally, the generated PDF document is saved with a filename based on the title of the scraped webpage. Invalid characters in the title are replaced with underscores to create a valid filename.

## Features
- **Dynamic Title Handling:** The scraper automatically extracts the title of the webpage being scraped and uses it as the PDF title.
- **Proper Formatting:** The tool ensures that the scraped text is well-formatted in the PDF, with paragraphs, line breaks, and appropriate styles.
- **Customizable:** Users can adjust the line spacing and styling of the generated PDF by modifying the script's parameters and styles.

## Requirements
The Text Scraper has the following requirements:

## Python 3.10 or Higher
- The requests library for making HTTP requests
- The BeautifulSoup library for HTML parsing
- The reportlab library for PDF generation

## Usage
Users can run the script by providing a valid URL as input, and it will generate a PDF document containing the scraped text. The resulting PDF file is saved with a filename based on the webpage's title.

## Contributing
Contributions to the project are welcome. Users can fork the repository, make their changes or improvements, and submit pull requests to contribute to its development.

## License
The Text Scraper is open-source software and is provided under a specified open-source license. Users should consult the included LICENSE.md file for detailed licensing information.

In summary, the Text Scraper is a versatile tool for extracting and preserving the textual content of webpages in a user-friendly PDF format. It simplifies the process of archiving online information and making it accessible for offline reading or reference.
