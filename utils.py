import requests
import os
import time
from bs4 import BeautifulSoup

def paginate_category(category_url):
    "Retourne toutes les pages d'une catégorie avec pagination."
    pages = [category_url]
    while True:
        response = requests.get(category_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        next_button = soup.find('li', class_='next')
        if next_button:
            category_url = category_url.rsplit('/', 1)[0] + '/' + next_button.find('a')['href']
            pages.append(category_url)
        else:
            break
        time.sleep(1)  # Respectez le serveur en ajoutant une pause entre les requêtes
    return pages

def download_image(image_url, folder='images'):
    "Télécharge et enregistre une image dans le dossier spécifié."
    if not os.path.exists(folder):
        os.makedirs(folder)
    image_name = os.path.join(folder, image_url.split('/')[-1])
    response = requests.get(image_url)
    with open(image_name, 'wb') as file:
        file.write(response.content)
