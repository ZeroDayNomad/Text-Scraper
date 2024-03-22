import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# URL of the website you want to scrape
url = input("Add Site Link: ")

# Function to scrape the website's text and title
def scrape_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract text content
        paragraphs = soup.find_all('p')
        text = ''
        for paragraph in paragraphs:
            text += paragraph.get_text() + '\n'

        # Extract title
        title = soup.title.string.strip()

        return text, title
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

# Function to create a PDF from the scraped text
def create_pdf(text, title):
    try:
        if not title:
            title = "Untitled Article"

        # Replace invalid characters in the title to create a valid filename
        title = "".join(c if c.isalnum() or c in (' ', '-') else '_' for c in title)

        output_file = f"{title}.pdf"
        doc = SimpleDocTemplate(output_file, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        # Add a title to the first page
        title_paragraph = Paragraph(f"<b>{title}</b>", styles['Title'])
        story.append(title_paragraph)

        # Create Paragraphs with the scraped text and add them to the PDF
        normal_style = styles['Normal']
        paragraphs = text.split('\n')
        for paragraph in paragraphs:
            if paragraph.strip():
                formatted_text = Paragraph(paragraph, normal_style)
                story.append(formatted_text)
                # Add a spacer (double line break) between paragraphs
                story.append(Spacer(1, 12))  # Adjust the 12 value to control spacing

        doc.build(story)
        print(f"PDF saved as '{output_file}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    scraped_text, article_title = scrape_website(url)
    if scraped_text:
        create_pdf(scraped_text, article_title)
