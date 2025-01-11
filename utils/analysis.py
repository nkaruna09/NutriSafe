
import cohere

api_key = "rFtQp6u9Dj0QIfwyKRAGGEZwbuZWOutMSoi4wMZ0"
co = cohere.Client(api_key)
 
def check_healthiness(ingredients, nutrition_data, disease):
    # Construct the prompt to send to Cohere API
    prompt = f"""
    Ingredients: {ingredients}, Nutrition: {nutrition_data}
    Classify the healthiness of this product based on its nutritional content and its compatibility with a person with {disease}.
    Return one of the following labels: Green (healthy), Yellow (moderately healthy), Red (unhealthy).
    Only state the label. Do not provide explaination or description.
    """
    
    try:
        # Use Cohere's generate function to get a response
        response = co.generate(
            model='command-r-08-2024',  # Choose the model size you prefer (xlarge is a good balance)
            prompt=prompt,
            max_tokens=150  # Limit the response length to 150 tokens
        )
        
        # Extract the generated text (healthiness classification)
        health_label = response.generations[0].text.strip()
        return health_label
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
#product_name = "Organic Apple Juice"
#ingredients = "Apple juice, Water, Natural flavor, Sugar"
#nutrition_data = "150 calories, 35g sugar, 0g fat, 5g sodium"

#health_status = check_healthiness(ingredients, nutrition_data, "Diabetes")
#print(f"Health Status: {health_status}")