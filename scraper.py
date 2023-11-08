import requests
from bs4 import BeautifulSoup


def get_html_content(url):
    response = requests.get(url)
    return response.text


def extract_headlines(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    
    headline_elements = soup.find_all('h2', class_='headline')
    
    headlines = [element.text for element in headline_elements]
    return headlines

if __name__ == "__main__":
    # Specify the URL of the website to scrape
    website_url = "https://example.com/news"

    html_content = get_html_content(website_url)
  
    headlines = extract_headlines(html_content)
    print("News Headlines:")
    for index, headline in enumerate(headlines, start=1):
        print(f"{index}. {headline}")
