import requests
from bs4 import BeautifulSoup
import lxml

import excel_writing
import string_operations

NumPages = 25

url = "https://allo.ua/ua/kompjutery/action-da/"

headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 "
                  "Safari/537.36"
}

discount_prices = {}

count = 1

session = requests.session()

for j in range(1, NumPages + 1):
    print(f"------Page {j} done------")
    response = session.get(f"{url}/p-{j}/", headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        all_products = soup.find_all("div", class_="product-card")
        for i in all_products:
            title = i.find("a", class_="product-card__title")
            price = i.find("div", class_="v-pb__cur discount")
            if price:
                discount_prices[count] = f"{title.text}|{price.text}"
                count += 1

excel_writing.File = "catalog.xlsx"

lowest_price = "100000000000000|0"

for i, (key, element) in enumerate(discount_prices.items(), start=1):
    splited = element.split("|")
    excel_writing.write_file(f"A{i}", f"{splited[0]}")
    excel_writing.write_file(f"B{i}", f"{splited[1]}")
    number_price = int(string_operations.extract_numbers(splited[1]))
    if number_price < int(lowest_price.split("|")[0]):
        lowest_price = f"{number_price}|{i}"

lowest_price_str = discount_prices[int(lowest_price.split("|")[1])]

print(f"найнижча ціна на товарі {lowest_price_str.split('|')[0]}, з ціною {lowest_price_str.split('|')[1]}")