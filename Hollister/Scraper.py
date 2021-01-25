import requests
from bs4 import BeautifulSoup
import json

# Url du produit 
url_produit = 'https://www.hollisterco.com/shop/eu-fr/p/pantalon-chino-ultra-skinny-hollister-epic-flex-13429336?categoryId=6239368&seq=04&faceout=prod1'

# Configuration du header 
header = {
    'Content-Type': 'application/json',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'fr-fr',
    'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'www.hollisterco.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
    'Connection': 'keep-alive'
}

# Accès à la page 
r = requests.get(url_produit, headers=header)

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
        color = x['data-swatch']
        product_dict["%s" % color] = {}
for x in list_product:
    if x['data-inventory-status'] == 'Available':
        W = x['data-size-primary']
        L = ""
        color = x['data-swatch']
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