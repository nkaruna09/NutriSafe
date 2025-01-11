import requests
import json

def fetch_product_data(code):
    url = f"https://world.openfoodfacts.org/api/v2/product/{code}.json"
    x = requests.get(url)
    if x.json()['status'] == 0:
        return "Product not found."
        
    ingredients = x.json()['product']['ingredients_text']
    return ingredients

