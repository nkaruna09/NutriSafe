import requests

def fetch_product_data(code):
    url = f"https://world.openfoodfacts.org/api/v2/product/{code}.json"
    
    ingredient_breakdown = {}
    hasEstimates = False 

    rsp = requests.get(url)
    if rsp.json()['status'] == 0:
        return "Product not found."
    if "ingredients" in rsp.json()['product']['ecoscore_data']['missing'].keys():
        return "Missing ingredients. This may not be a food item."
        
    if "ingredients" in rsp.json()['product'].keys():
        for ingredient in rsp.json()['product']['ingredients']:
            if "percent_estimate" in ingredient:
                hasEstimates = True
                if ingredient['percent_estimate'] < 1:
                    if "other" not in ingredient_breakdown.keys():
                        ingredient_breakdown['other'] = ingredient['percent_estimate']
                    else:
                        ingredient_breakdown['other'] += ingredient['percent_estimate']
                else:
                    ingredient_breakdown[ingredient['text']] = ingredient['percent_estimate']


    product_data = {
        "ingredients": rsp.json()['product']['ingredients_text_en'],
        "allergens" : ', '.join([item.removeprefix("en:") for item in rsp.json()['product']['allergens_tags']]),
        "nutriments": rsp.json()['product']['nutriments'] 
    }

    if hasEstimates:
        product_data["ingredient_breakdown"] = ingredient_breakdown

    return product_data
