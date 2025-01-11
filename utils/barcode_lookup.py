import requests
import json

def fetch_product_data(code):
    url = f"https://world.openfoodfacts.org/api/v2/product/{code}.json"
    rsp = requests.get(url)
    if rsp.json()['status'] == 0:
        return 1
    if "ingredients" in rsp.json()['product']['ecoscore_data']['missing'].keys():
        return 2
        
    product_data = {
        "ingredients": rsp.json()['product']['ingredients_text_en'],
        "allergens" : ', '.join([item.removeprefix("en:") for item in rsp.json()['product']['allergens_tags']]),
        "nutriments": rsp.json()['product']['nutriments'] 
        
    }
    return product_data



data = fetch_product_data("42208556")

ingredients = data['ingredients']
allergens = data['allergens']
nutriments = data['nutriments']
