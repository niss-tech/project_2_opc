import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from utils import get_next_page_url

def fetch_page_content(url):
    """Récupère le contenu HTML d'une page."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
    except requests.exceptions.HTTPError as e:
        print(f"Erreur HTTP {e.response.status_code} pour l'URL : {url}")
        return None
    
def extract_category_links(base_url):
    """Extrait les liens des catégories depuis la page principale, sans inclure le lien 'Books'."""
    soup = fetch_page_content(base_url)
    if soup is None:
        return []

    # Sélectionne tous les liens des catégories
    category_links = soup.select('div.side_categories ul li a')

    # Exclus le lien dont le texte est "Books", car il regroupe tout les livres du sites"
    filtered_links = [
        link for link in category_links 
        if link.text.strip().lower() != 'books'  # Vérifier le texte
    ]

    # Construit les URL absolues et les retournent
    return [urljoin(base_url, link['href']) for link in filtered_links]



def extract_product_links(category_url):
    """Extrait les liens des produits pour une catégorie, avec gestion de la pagination."""
    product_links = []  
    current_url = category_url 

    while current_url:  # Boucle sur toutes les pages de la catégorie
        soup = fetch_page_content(current_url)  
        if soup is None:
            break  # Si la page est inaccessible, on arrête la boucle

        # Récupère les liens des produits sur la page actuelle
        product_links.extend(
            urljoin(current_url, a['href'])
            for a in soup.select('h3 a')
        )

        # Passe à la page suivante grâce à la fonction de pagination
        current_url = get_next_page_url(soup, current_url)

    return product_links

