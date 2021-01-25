import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
import json
import urllib3
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry



'''# Désactivation des messages d'avertissement
#urllib3.disable_warnings()

# Réglage des "Timeouts"
class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = 15
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)


# Réglage des "Retries"
retries = Retry(total=5, backoff_factor=0, status_forcelist=[429, 500, 502, 503, 504])'''


def ChercherProduit(url_produit):
    """# Ouverture d'une session
    s = requests.Session()

     # Réglage des paramètres de la session
    s.mount("https://", TimeoutHTTPAdapter(max_retries=retries))"""

    # Configuration du header 
    user_agent = generate_user_agent(os=('mac'))
    header = {
        'Content-Type': 'application/json',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'fr-fr',
        'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': user_agent,
        'Connection': 'keep-alive',
   }

    # Accès à la page
    r = requests.get(url_produit, headers=header)
    print('Accès à la page terminé')

    # Fermeture de la session
    #s.close

    # Recherche des informations de stock
    soup = BeautifulSoup(r.content, "html.parser")
    rep = soup.find_all("select")
    rep_bis = rep[1]
    list_product = rep_bis.find_all("option")
    list_product.pop(0)

    # Recherche des tarifs
    rep_3 = soup.find_all("script")
    rep_3_bis = rep_3[1].contents[0]
    list_rep_3 = rep_3_bis.split('items')
    list_item = []
    for x in list_rep_3:
        list = x.split('{')
        z = 0
        for y in list:
            try:
                if z == 0: 
                    if y == '":':
                        index_sku = list.index('":') + 1
                        sku = list[index_sku].lstrip('"').rstrip('"').strip(':')
                        z += 1
                list_bis = y.split('"')
                if z >= 1:
                    index_sku = list_bis.index("listPrice") + 2
                    sku = list_bis[index_sku].lstrip('"').rstrip('"').strip(':')
                index_prix = list_bis.index("offerPrice") + 1
                prix = list_bis[index_prix].strip(',').strip(':')
                list_item.append([sku, prix])
            except:
                pass

    # Création d'un dict avec tous les produits disponibles et leurs informations 
    product_dict = {

    }
    for x in list_product:
        if x['data-inventory-status'] == 'Available':
            color = 'unique'
            try:
                color = x['data-swatch']
            except:
                pass
            product_dict["%s" % color] = {}
    for x in list_product:
        if x['data-inventory-status'] == 'Available':
            W = x['data-size-primary']
            L = ""
            color = 'unique'
            try:
                color = x['data-swatch']
            except:
                pass
            try: 
                L = ", "+x['data-size-secondary']
            except:
                pass
            sku = x['value']
            for y in list_item:
                if y[0] == sku:
                    prix = y[1]
            product_dict["%s" % color]["%s%s" % (W, L)] = {
                "sku": sku,
                "prix": prix
            }

    print(product_dict)

ChercherProduit('https://www.hollisterco.com/shop/eu-fr/p/sweat-à-capuche-à-motif-et-emblème-43196819?categoryId=6173709&seq=07')