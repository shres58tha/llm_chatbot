import requests
from bs4 import BeautifulSoup

def scrape_news(url='https://www.bbc.com/news', unwanted=[''],limit=10):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')

        articles = soup.find_all('div', class_='gs-c-promo-body')
        unwanted = ['']

        article_data = []

        for article in articles:
            headline = article.find('h3').get_text().strip()
            if headline not in unwanted:
                summary = article.find('p', class_='gs-c-promo-summary')
                summary_text = summary.get_text().strip() if summary else "Summary not available"
                article_data.append({'headline': headline, 'summary': summary_text})
                if len(article_data) == limit:
                    break

        return article_data
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

def display_news():
    url = 'https://www.bbc.com/news'
    articles =     scrape_news(url)

    if articles:
        print("BBC News Top Articles:")
        for i, article in enumerate(articles, start=1):
            print(f"{i}. {article['headline']}")
            print(f"   Summary: {article['summary']}\n")
    else:
        print("Failed to fetch articles.")

#display_news()
