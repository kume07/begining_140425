import requests

url = "https://dummyjson.com/products?limit=194&skip=4"
TARGET_BRAND = "Samsung"

response = requests.get(url)
response_json = response.json()
products = response_json["products"]

count = 0
total_cost = 0
for product in products:
    if product.get("brand", "").lower() == TARGET_BRAND.lower():
        count += 1
        cost = product["price"] * product["stock"]
        total_cost += cost
print(f"{total_cost=}, {count=}")
