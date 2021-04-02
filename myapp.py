import requests
import json

URL = "http://127.0.0.1:8000/product/create"

data = {'name': 'test_product', 'price': '789'}


json_data = json.dumps(data)
print(json_data)

r = requests.post(url=URL, data=json_data)

data = r.json()


print(data)
