import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

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
    """Extrait les liens des catégories depuis la page principale."""
    soup = fetch_page_content(base_url)
    if soup is None:
        return []

    category_links = soup.select('div.side_categories ul li a')
    return [urljoin(base_url, link['href']) for link in category_links]

def extract_product_links(category_url):
    """Extrait les liens des produits pour une catégorie donnée."""
    soup = fetch_page_content(category_url)
    if soup is None:
        return []

    product_links = [
        urljoin(category_url, a['href'])
        for a in soup.select('h3 a')
    ]
    return product_links
