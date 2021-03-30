import requests

URL = "http://78dec2e98afd.ngrok.io/product/1"

r = requests.get(url=URL)

data = r.json()


print("Name of product is", data["name"], "and its price is", data["price"])
