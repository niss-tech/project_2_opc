import os
import csv
import requests

def save_to_csv(data, output_file):
    """Sauvegarde les données dans un fichier CSV."""
    if not data:
        return
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def download_image(image_url, folder='images'):
    """Télécharge et enregistre une image dans un dossier."""
    if not os.path.exists(folder):
        os.makedirs(folder)
    image_name = os.path.join(folder, image_url.split('/')[-1])
    response = requests.get(image_url)
    with open(image_name, 'wb') as file:
        file.write(response.content)

