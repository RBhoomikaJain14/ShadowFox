import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "http://quotes.toscrape.com/page/{}/"
quotes_data = []

for page in range(1, 11):
    print(f"Scraping page {page}...")
    response = requests.get(BASE_URL.format(page))
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")
    for q in quotes:
        text = q.find("span", class_="text").get_text()
        author = q.find("small", class_="author").get_text()
        tags = [tag.get_text() for tag in q.find_all("a", class_="tag")]
        quotes_data.append([text, author, ", ".join(tags)])

print(f"Total quotes scraped: {len(quotes_data)}")

with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Quote", "Author", "Tags"])
    writer.writerows(quotes_data)

print("Quotes saved to quotes.csv")
