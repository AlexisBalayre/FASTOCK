import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
import json
import urllib3
import time

# Désactivation des messages d'avertissement
#urllib3.disable_warnings()

def ChercherProduits(url_produits):
    while True: 
        # Ouverture d'une session
        #s = requests.Session()

        # Configuration du header 
        user_agent = generate_user_agent(os=('mac', 'linux'))
        header = {
            'Content-Type': 'application/json',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'fr-fr',
            'Accept-Encoding': 'gzip, deflate, br',
            'User-Agent': user_agent,
            'Connection': 'keep-alive',
            'Referer': 'https://www.google.com/'
        }
    

        # Tentative d'accès à la page 
        try:
            r = requests.get(url_produits, headers=header)
            break
        except:
            print('problème !')
            time.sleep(120)
            pass

    # Recherche des informations de stock
    soup = BeautifulSoup(r.content, "html.parser")
    rep = soup.find_all("script")
    print(rep[1])


ChercherProduits('https://www.hollisterco.com/shop/eu-fr/gars-bas-offres-spéciales?filtered=true&rows=240&start=0&facet=ads_f43002_ntk_cs:(%2228W%22)')



