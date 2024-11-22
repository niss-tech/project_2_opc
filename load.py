import os
import csv
import requests

def save_to_csv(data, output_file):
    """Sauvegarde les données dans un fichier CSV dans un dossier extérieur."""
    if not data:
        return
    
    # Définir le chemin du dossier extérieur "fichiers_csv"
    parent_directory = os.path.dirname(os.getcwd())  # Chemin du dossier parent
    csv_folder = os.path.join(parent_directory, 'fichiers_csv')  # Chemin complet du dossier

    
    if not os.path.exists(csv_folder):
        os.makedirs(csv_folder)

    # Définir le chemin complet du fichier CSV
    output_path = os.path.join(csv_folder, output_file)

    
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def download_image(image_url, folder='images'):
    """Télécharge et enregistre une image dans un dossier à l'extérieur du dossier courant."""
    # Chemin du dossier parent
    parent_directory = os.path.dirname(os.getcwd())  
    folder = os.path.join(parent_directory, folder)  # Chemin absolu du dossier "images"

    if not os.path.exists(folder):
        os.makedirs(folder)
        
    image_name = os.path.join(folder, image_url.split('/')[-1])
    response = requests.get(image_url)
    with open(image_name, 'wb') as file:
        file.write(response.content)


