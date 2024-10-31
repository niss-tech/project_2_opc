# def extract_book_data(url: str):
#     # Requête pour récupérer le contenu de la page
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')

#     # Extraction du titre
#     title = soup.body.h1.string

#     # Récupération des informations générales
#     product_information = soup.findAll(['td'])

#     # Extraction de la catégorie
#     category = soup.ul.find_all('li')[2].a.string

#     # Extraction de la description du produit
#     product_description = soup.find('article').find_all('p')[3].get_text(strip=True)

#     # Extraction de l'évaluation en étoiles
#     review_rating = soup.find(class_="star-rating")["class"][1]

#     # Extraction des URLs des images et transformation en URLs absolues
#     img_urls = [urljoin(url, img.get('src')) for img in soup.find_all('img') if img.get('src')]

#     # Retour des données sous forme de dictionnaire
#     return {
#         "product_page_url": url,
#         "title": title,
#         "universal_product_code": product_information[0],  # Code UPC
#         "price_excluding_tax": product_information[3],
#         "price_including_tax": product_information[2],
#         "number_available":int(product_information[5].split()[0]),  # Nombre disponible
#         "product_description": product_description,
#         "category": category,
#         "review_rating": review_rating,
#         "image_url": img_urls,
        
#     }


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from transform import transform_data

#extraction des données depuis une page web produit  et appelle transform_data ppour transformer les données en dictionnaire
def extract_book_data(url: str):
   
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.body.h1.string
    product_information = soup.findAll(['td']) # récupération de la table product information
    category = soup.ul.findAll('li')[2].a.string
    description = soup.head.find(attrs={"name": "description"})['content']
    star_review = soup.find(class_="star-rating")["class"][1]
    img_url = urljoin(url, soup.find('img')["src"])

    data_clean, img_name = transform_data(url, title, product_information, description, category, star_review, img_url)

    img = requests.get(img_url)  # stockage de l'image
    

    return data_clean