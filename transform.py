import re

#cette fonction transforme les donnees en dictionnaires
def transform_data(url: str,
                   title: str,
                   product_information: [],
                   description: str,
                   category: str,
                   star_review: str,
                   img_url: str
                   ):


    title = re.sub(r'\([^)]+\)', "", title).strip()
    nb_av = product_information[5].string  # récupération du nombre de livre dispo
    nb_av = int(nb_av[nb_av.index("(") + 1:nb_av.index(")")].replace(" available", "").strip())
    description = description.strip()
    code_upc = product_information[0].string
    price_excl_tax = product_information[3].string
    price_incl_tax = product_information[2].string
    
    
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
    return book_dict


