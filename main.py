import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,es;q=0.8"
}


def get_scrapped_data(uri: str):
    res = requests.get(uri, headers=headers)
    return BeautifulSoup(res.text, 'lxml')


def get_price(price: str):
    return float(price.strip()[1:])


# print(soup.prettify())
uri = 'https://www.amazon.com/Samsung-Bluetooth-Advanced-monitoring-Tracking/dp/B089DPMDNM/ref=sr_1_3?dchild=1&keywords=oneplus+watch&qid=1618435615&sr=8-3'
soup = get_scrapped_data(uri)

price = soup.find('span', {'id': 'price_inside_buybox'}).text


print(get_price(price))
