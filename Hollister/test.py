import requests
from user_agent import generate_user_agent

user_agent = generate_user_agent(os=('mac', 'linux'))
url = 'https://httpbin.org/ip'
s = requests.Session()
s.headers.update({
    'Content-Type': 'application/json',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'fr-fr',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': user_agent,
    'Connection': 'keep-alive',
    'Referer': 'https://www.google.com/'
})
s.proxies = {
    "https": "http://bdfsfksn-rotate:hdmzx6j1ek9k@p.webshare.io:80/"
}
test = s.get("https://www.fnac.com")
print(test)
response = s.get(url, verify=False)
print(response.json())