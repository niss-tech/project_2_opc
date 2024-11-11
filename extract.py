# extract.py
import requests
from bs4 import BeautifulSoup

def get_book_data(book_url):
    """Extrait les informations d'un livre à partir de son URL."""
    response = requests.get(book_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    data = {
        "product_page_url": book_url,
        "universal_product_code": soup.find('th', text='UPC').find_next_sibling('td').text,
        "title": soup.find('h1').text,
        "price_including_tax": soup.find('th', text='Price (incl. tax)').find_next_sibling('td').text,
        "price_excluding_tax": soup.find('th', text='Price (excl. tax)').find_next_sibling('td').text,
        "number_available": soup.find('th', text='Availability').find_next_sibling('td').text,
        "product_description": soup.select_one('meta[name="description"]')['content'].strip(),
        "category": soup.find('ul', class_='breadcrumb').find_all('a')[2].text,
        "review_rating": soup.find('p', class_='star-rating')['class'][1],
        "image_url": 'http://books.toscrape.com/' + soup.find('img')['src']
    }
    return data

def get_books_from_category(category_url):
    """Récupère les URLs des livres pour une catégorie spécifique."""
    response = requests.get(category_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    book_urls = ['http://books.toscrape.com/catalogue/' + a['href'].replace('../../../', '')
                 for a in soup.select('h3 a')]
    return book_urls
