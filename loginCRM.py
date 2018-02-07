import urllib.request
import requests
from bs4 import BeautifulSoup

payload = {'username': 'powerwolf',
            'password': 'power1234!',
            'rememberMe': 'true'}
with requests.Session() as s:
    url3 = "http://na.admin.estgames.co.kr/Account/LogOn?ReturnUrl=%2fcabalna%2fUser%2fUserList%3fKey%3did%26Val%3danamibeluisa%26State%3d1%26category%3d0%26MassCreation%3d0%26FromDate%3d%26ToDate%3d20180129%26limit%3d25&Key=id&Val=anamibeluisa&State=1&category=0&MassCreation=0&FromDate=&ToDate=20180129&limit=25"
    p = s.post(url3, data=payload)
    print(type(p.text))

    soup = BeautifulSoup(p.text, "html.parser")
    print(soup)
