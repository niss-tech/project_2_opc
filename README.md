**Web Scraping - Books to Scrape**


Ce projet est un script Python qui utilise un processus ETL pour extraire des données du site[Books to Scrape](http://books.toscrape.com). Les données sont extraites, transformées, puis chargées dans un fichier CSV.

**Les fichiers :** 
- `extract.py` : Extraction des données
- `transform.py` : Transformation des données
- `load.py` : Chargement des données dans des fichiers CSV et téléchargement des images.
- `utils.py` : Fonctions utilitaires (pagination, gestion des erreurs, etc.).
- `main.py` : Script principal pour exécuter le processus ETL


**Instructions d'installation et d'exécution**

    1/ Cloner le projet depuis GitHub :

    git clone https://github.com/niss-tech/project_2_opc.git
    cd project_2_opc

    2/ Mettez en place l'environnement avec : 
    python -m venv env
    
    3/ Puis activez le avec :

    sous windows -> env\Scripts\activate
    sous macOS / linux -> source env/bin/activate


    4/ Installez les bibliothèques nécessaires avec : 

    pip install -r requirements.txt

    5/ Puis executez le script avec (assurez vous d'être dans le bon dossier): 
    python main.py

    6/ Arreter le script à tout moment , appuyer dans le terminal : ctrl+c




**Fonctionnalités principales**

Scraping de toutes les catégories :
Le script parcourt toutes les catégories disponibles sur le site et extrait les informations de chaque livre.

Téléchargement d'images :
Les images des livres sont téléchargées et sauvegardées localement dans un dossier nommé images.

Génération de fichiers CSV :
Chaque catégorie est sauvegardée dans un fichier CSV distinct, par exemple : travel_books.csv.



