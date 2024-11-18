import re

def parse_product_page(soup, product_url):
    """Transforme le contenu HTML d'une page produit en dictionnaire."""
    book_data = {}
    book_data['product_page_url'] = product_url
    book_data['universal_product_code'] = soup.find('th', text='UPC').find_next_sibling('td').text
    book_data['title'] = soup.find('h1').text
    book_data['price_including_tax'] = soup.find('th', text='Price (incl. tax)').find_next_sibling('td').text
    book_data['price_excluding_tax'] = soup.find('th', text='Price (excl. tax)').find_next_sibling('td').text
    availability_text = soup.find('th', text='Availability').find_next_sibling('td').text
    book_data['number_available'] = int(re.search(r'\d+', availability_text).group())
    book_data['product_description'] = (
        soup.find('meta', attrs={'name': 'description'})['content'].strip()
        if soup.find('meta', attrs={'name': 'description'})
        else ''
    )
    book_data['category'] = soup.find('ul', class_='breadcrumb').find_all('li')[-2].text.strip()
    book_data['review_rating'] = soup.find('p', class_='star-rating')['class'][1]
    book_data['image_url'] = "http://books.toscrape.com/" + soup.find('img')['src'].replace('../', '')
    return book_data

