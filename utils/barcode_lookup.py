import requests
import json

def fetch_product_data(code):
    url = f"https://world.openfoodfacts.org/api/v2/product/{code}.json"
    x = requests.get(url)
    if x.json()['status'] == 0:
        return "Product not found."
    if "ingredients" in x.json()['product']['ecoscore_data']['missing'].keys():
        return "Missing ingredients. This may not be a food item."
    ingredients = x.json()['product']['ingredients_text_en']
    return ingredients

print(fetch_product_data("42208556"))