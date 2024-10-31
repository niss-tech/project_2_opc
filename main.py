import csv
from extract import extract_book_data

def main():
    # URL du livre à extraire
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    
    # Appel de la fonction pour extraire les données du livre
    try:
        book_data = extract_book_data(url)

        # Afficher les données extraites et transformées
        print("Données du livre :")
        for key, value in book_data.items():
            print(f"{key}: {value}")

        # Enregistrement des données dans un fichier CSV
        with open('book_data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=book_data.keys())
            # Si le fichier est vide, écrire les en-têtes
            if csv_file.tell() == 0:
                writer.writeheader()
            writer.writerow(book_data)  # Écrire les données du livre

    except Exception as e:
        print(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
    main()



