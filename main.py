# main.py
from extract import get_books_from_category, get_book_data
from transform import transform_data
from load import save_to_csv
from utils import paginate_category, download_image

def etl_process(category_url, output_filename):
    all_books_data = []
    
    # Pagination dans la catégorie
    pages = paginate_category(category_url)
    for page_url in pages:
        # Récupérer les URLs des livres dans la page
        book_urls = get_books_from_category(page_url)
        for book_url in book_urls:
            # Extraction des données du livre
            book_data = get_book_data(book_url)
            
            # Transformation des données
            transformed_data = transform_data(book_data)
            all_books_data.append(transformed_data)
            
            # Télécharger l'image
            download_image(transformed_data["image_url"])
    
    # Charger les données dans un fichier CSV
    save_to_csv(all_books_data, output_filename)
    print(f"ETL terminé ! Données enregistrées dans {output_filename}")

# Exécution de l'ETL pour une catégorie
category_url = 'https://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html'
etl_process(category_url, 'books_in_category.csv')
