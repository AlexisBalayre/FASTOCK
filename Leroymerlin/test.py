import requests

# Url API
url_api = 'https://api-gateway.leroymerlin.fr/api-stock/v1/stocks'

# Configuration du header 
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
    'X-Gateway-APIKey': 'E5hmPshuXX6S2NsnquFC0b3AxeYxQ2ij',
    'Content-Type': 'application/json'
}

payload = {
    'productIds': '65222493',
    'stockNames': 'stockAvailableImmediate',
    'storeId': 380
}

r = requests.get(url_api, headers=header, params=payload)
print(r)
print(r.content)