import requests



# Url du produit 
url_produit = 'https://ipv4.webshare.io/'

# Configuration du header 
header = {
    'Content-Type': 'application/json',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'fr-fr',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
    'Connection': 'keep-alive'
}


# Accès à la page 
r_s = requests.get(url_produit, headers=header, proxies={"https": "http://bdfsfksn-rotate:hdmzx6j1ek9k@p.webshare.io:80/"})
print(r_s.text)


