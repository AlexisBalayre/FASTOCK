import requests

# Url du produit 
url_produit = 'https://www.hollisterco.com/api/search/h-eu-fr/search/category/6239368'

# Configuration du header 
header = {
    'Content-Type': 'application/json',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'fr-fr',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
    'Connection': 'keep-alive'
}

# Paramètres url taille 29W et 30W
payload_taille_s = {
    'catalogId': '11558',
    'facet': 'ads_f43002_ntk_cs:("29W")',
    'requestType': 'category',
    'rows': '240',
    'start': '0',
    'storeId': '19158'
}
payload_taille_m = {
    'catalogId': '11558',
    'facet': 'ads_f43002_ntk_cs:("30W")',
    'requestType': 'category',
    'rows': '240',
    'start': '0',
    'storeId': '19158'
}

# Accès à la page 
r_s = requests.get(url_produit, headers=header, params=payload_taille_s)
r_m = requests.get(url_produit, headers=header, params=payload_taille_m)

# Récupération des dictionnaires
rep_dict_s = r_s.json()
rep_dict_m = r_m.json()

# Listes produit disponibles en S et M
product_list_s = rep_dict_s['products']
product_list_m = rep_dict_m['products']

# Création d'un dict avec tous les produits disponibles et leurs informations 
product_dict = {
    "29W": {},
    "30W": {}
}
y_s = 0
y_m = 0 
for x in product_list_s:
    y_s += 1
    product_dict["29W"].update({
        y_s: {
            'name': x['name'],
            'color': x['colorFamily'],
            'price': x['lowPrice']
        }
    })
      
for y in product_list_m:
   y_m += 1
   product_dict["30W"].update({
        y_m: {
            'name': y['name'],
            'color': y['colorFamily'],
            'price': y['lowPrice']
        }
    })
    
print(product_dict)