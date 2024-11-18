def get_next_page_url(soup, current_url):
    """Retourne l'URL de la page suivante si elle existe, sinon None."""
    next_button = soup.find('li', class_='next')
    if next_button:
        return current_url.rsplit('/', 1)[0] + '/' + next_button.find('a')['href']
    return None
