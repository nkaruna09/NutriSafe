
import cohere
from dotenv import load_dotenv
import os


# Load the .env file
load_dotenv()

# Get the API key from the .env file
api_key = os.getenv("COHERE_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please add it to the .env file.")

# Initialize the Cohere client
co = cohere.Client(api_key)
 
def check_healthiness(ingredients, nutrition_data, user_allergen, food_allergens, disease):
    # Prompt to send to Cohere API
    prompt = f"""
    Ingredients: {ingredients}, Nutrition: {nutrition_data}, Allergens in food: {food_allergens}
    Classify the healthiness of this product based on its nutritional content and its compatibility with a person with {disease} and with these allergies: {user_allergen}.
    Return one of the following labels: Green (healthy), Yellow (moderately healthy/safe), Red (unhealthy/not safe).
    If food contains the user's allergen, automatically return Red.
    Only state the label. Do not provide explaination or description.
    """
    
    try:
        response = co.generate(
            model='command-r-08-2024',  
            prompt=prompt,
            max_tokens=150  # Limit the response length to 150 tokens
        )
        
        # Extract the generated text (healthiness classification)
        health_label = response.generations[0].text.strip()
        return health_label
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def recommendations_alternatives(ingredients, nutrition_data, user_allergen, food_allergens, disease, safety): 
    prompt = f"""
    Ingredients: {ingredients}, Nutrition: {nutrition_data}, Allergens: {food_allergens}
    I have this {disease} and these allergens {user_allergen}. You said this food is {safety} for me. Explain why. If unsafe or moderately safe, provide healthier alternatives (under 100 words). 
    """

    try:
        response = co.generate(
            model='command-r-08-2024',  
            prompt=prompt,
            max_tokens=150  # Limit the response length to 150 tokens
        ) 
        
        # Extract the generated text (healthiness classification)
        recommendation = response.generations[0].text.strip()
        return recommendation
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
#product_name = "Organic Apple Juice"
#ingredients = "Apple juice, Water, Natural flavor, Sugar"
#nutrition_data = "150 calories, 35g sugar, 0g fat, 5g sodium"

#health_status = check_healthiness(ingredients, nutrition_data, "Diabetes")
#print(f"Health Status: {health_status}")