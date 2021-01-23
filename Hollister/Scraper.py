import requests
from bs4 import BeautifulSoup

# Url du produit 
url_produit = 'https://www.hollisterco.com/shop/eu-fr/p/jean-slim-fusel%C3%A9-qui-ne-se-d%C3%A9lave-pas-42433945?categoryId=85264&seq=01&faceout=model1'

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

soup_2 = BeautifulSoup(r.content, "html.parser")
reponse_2 = soup_2.find_all("select")
reponse_3 = reponse_2[1]

print(reponse_3)