from extract import fetch_page_content, extract_category_links, extract_product_links
from transform import parse_product_page
from load import save_to_csv, download_image

def scrape_all_categories(base_url):
    """Scrape toutes les catégories et sauvegarde les données dans des CSV."""
    category_urls = extract_category_links(base_url)
    for category_url in category_urls:
        category_name = category_url.split('/')[-2]  # Nom de la catégorie
        print(f"Scraping catégorie : {category_name}")
        
        # Extraire les URLs des produits
        product_urls = extract_product_links(category_url)
        
        # Scraper les données de chaque produit
        all_books = []
        for product_url in product_urls:
            soup = fetch_page_content(product_url)
            if soup is None:  # Ignorez les pages inexistantes
                continue
            book_data = parse_product_page(soup, product_url)
            all_books.append(book_data)
            download_image(book_data['image_url'])
        
        # Sauvegarder dans un fichier CSV
        save_to_csv(all_books, f"{category_name}_books.csv")

if __name__ == "__main__":
    BASE_URL = "https://books.toscrape.com/index.html"
    scrape_all_categories(BASE_URL)
