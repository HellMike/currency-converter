import requests
import json

trade = dict()
currency_name = input()
url = f"http://www.floatrates.com/daily/{currency_name.lower()}.json"
data = requests.get(url)
exchange_rate = json.loads(data.text)
if "usd" in exchange_rate:
    trade["usd"] = exchange_rate["usd"]["rate"]
if "eur" in exchange_rate:
    trade["eur"] = exchange_rate["eur"]["rate"]

while True:
    exchange_currency = input()
    if exchange_currency == "":
        break
    amount_of_money = float(input())
    print("Checking the cache...")
    if exchange_currency.lower() in trade:
        print("Oh! It is in the cache!")
        print(f"You received {round(amount_of_money * trade[exchange_currency.lower()], 2)} {exchange_currency.upper()}.")
    else:
        print("Sorry, but it is not in the cache!")
        trade[exchange_currency.lower()] = exchange_rate[exchange_currency.lower()]["rate"]
        print(f"You received {round(amount_of_money * trade[exchange_currency.lower()], 2)} {exchange_currency.upper()}.")

