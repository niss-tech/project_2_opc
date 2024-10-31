# import re
# from extract import extract_book_data

# def transform_data(book_data: dict):
#     """
#     Transforme les données en dictionnaire pour écriture en CSV.
#     Args:
#         book_data: Dictionnaire contenant les informations extraites d'un livre.

#     Returns: dict contenant les informations formatées et le nom d'image.
#     """
    
#     # Extraction des champs de book_data
#     url = book_data.get("product_page_url")
#     title = re.sub(r'\([^)]+\)', "", book_data["title"]).strip()
#     product_information = book_data["universal_product_code"], book_data["price_excluding_tax"], book_data["price_including_tax"], book_data["number_available"]
#     description = book_data["product_description"].strip()
#     category = book_data["category"]
#     review_rating = book_data["review_rating"]
#     img_url = book_data["image_url"]  # Suppose qu'il y a une seule image principale
    
#     # Nom de fichier pour l'image
#     img_name = re.sub(r"[^_a-zA-Z0-9]", "", title.replace(" ", "_")) + "_" + product_information[0]  # Utilisation de universal_product_code pour le nom

#     # Transformation en dictionnaire final
#     book_dict = {
#         "product_page_url": url,
#         "universal_product_code": product_information[0],
#         "title": title,
#         "price_including_tax": product_information[2],
#         "price_excluding_tax": product_information[1],
#         "number_available": product_information[3],
#         "product_description": description,
#         "category": category,
#         "review_rating": review_rating,
#         "image_url": img_url
#     }

#     return book_dict, img_name

import re


def transform_data(url: str,
                   title: str,
                   product_information: [],
                   description: str,
                   category: str,
                   star_review: str,
                   img_url: str
                   ):
    """
    Tranforme les données en dictionnaire pour écriture en csv
    Args:
        url: Url du livre
        title: titre complet
        product_information: liste des produits
        description: description du livre
        category: catégorie du livre
        star_review: notation entre 1 et 5
        img_url: url de l'image

    Returns: dict contenant les informations propre + img name

    """

    title = re.sub(r'\([^)]+\)', "", title).strip()
    nb_av = product_information[5].string  # récupération du nombre de livre dispo
    nb_av = int(nb_av[nb_av.index("(") + 1:nb_av.index(")")].replace(" available", "").strip())
    description = description.strip()
    code_upc = product_information[0].string
    price_excl_tax = product_information[3].string
    price_incl_tax = product_information[2].string
    # mise en forme du nom de l'image, suppression de caratères spéciaux ...
    img_name = re.sub(r"[^_a-zA-Z0-9]", "", title.replace(" ", "_")) + "_" + str(code_upc)
    # mise en forme des données
    book_dict = {"product_page_url": url,
                 "universal_ product_code": code_upc,
                 "title": title,
                 "price_including_tax": price_incl_tax,
                 "price_excluding_tax": price_excl_tax,
                 "number_available": nb_av,
                 "product_description": description,
                 "category": category,
                 "review_rating": star_review,
                 "image_url": img_url
                 }
    return book_dict, img_name


