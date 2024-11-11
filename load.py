import csv

def save_to_csv(data, filename):
    "Enregistre une liste de données dans un fichier CSV."
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
