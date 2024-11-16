import requests
from bs4 import BeautifulSoup
from html import unescape
import csv

url = "http://books.toscrape.com/"

def scrape_books():
    response = requests.get(url)
    if response.status_code != 200:
        return

    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    books_data = []
    for book in books:
        title = unescape(book.h3.a['title'])
        price = unescape(book.find('p', class_='price_color').text)
        books_data.append({"Title": title, "Price": price})

    with open('books.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Price"])
        writer.writeheader()
        writer.writerows(books_data)

    print(f"Scraped {len(books_data)} books and saved to 'books.csv'.")
