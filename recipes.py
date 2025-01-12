import streamlit as st

import requests
import streamlit as st

# Function to fetch recipes by product name
def fetch_recipes_by_name(product_name):
    api_key = "4bdc4378f72d41fea7c8aa2a58be7a94"  # Replace with your Spoonacular API key
    url = "https://api.spoonacular.com/recipes/complexSearch"
    
    params = {
        "query": product_name,  # Search recipes using the product name
        "number": 5,            # Number of recipes to fetch
        "apiKey": api_key
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        st.error(f"Failed to fetch recipes. Error code: {response.status_code}")
        return []

# Streamlit UI
st.header("Potential Recipes by Product Name")
st.text("Using the result from NutriSafe, generate potential recipes with your healthy product!")

# Input field for product name
product_name = st.text_input("Enter the product name:", placeholder="e.g., Chocolate Spread")

if product_name:
    st.write(f"Searching for recipes using **{product_name}**...")
     
    # Fetch recipes
    recipes = fetch_recipes_by_name(product_name)
    
    if recipes:
        st.write("**Recipes Found:**")
        for recipe in recipes:
            st.subheader(recipe["title"])
            if "image" in recipe:
                st.image(recipe["image"], use_container_width=True)
            st.write(f"[View Full Recipe](https://spoonacular.com/recipes/{product_name}-{recipe['id']})")
    else:
        st.write("No recipes found for this product name. Try another!")
else:
    st.info("Please enter a product name to search for recipes.")


