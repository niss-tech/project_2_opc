# transform.py
import re

def transform_data(book_data):
    """Nettoie et structure les données du livre."""
    # Extraire le nombre disponible
    availability_text = book_data["number_available"]
    book_data["number_available"] = int(re.search(r'\d+', availability_text).group())

    # Convertir la notation de review_rating en étoile
    rating_dict = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    book_data["review_rating"] = rating_dict.get(book_data["review_rating"], 0)

    return book_data
