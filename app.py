import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

#import requests
#import openai
#from utils.barcode_lookup import fetch_product_data, is_food_item
#from utils.drug_list import fetch_drug_list
#from utils.analysis import analyze_interaction

st.set_page_config(page_title="NutriSafe", layout="centered")

# Load Custom CSS
with open("styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Welcome to NutriSafe")
st.write("""
Your food safety assistant for managing health conditions
""")

# Button to start checking food safety
if st.button("Start Checking Food Safety"):
    st.session_state.page = "Check Food Safety"
    st.rerun()  # Rerun to switch to the next page


# How it works Section
def display_how_it_works():
    st.subheader("How It Works")
    st.write("""
    1. **Select your ailment/disease** from the options.
    2. **Enter the barcode** of the food product you want to check.
    3. **Get the safety status** along with recommendations or alternatives.
    """)

# Display the "How It Works" section when the page is in the correct state
if "page" not in st.session_state:
    st.session_state.page = "Home"

if st.session_state.page == "Home":
    display_how_it_works()

elif st.session_state.page == "Check Food Safety":
    # Display the food safety check section
    st.header("Check Food Safety")
    
    # Ailment/Disease selection
    ailments = st.multiselect(
        "Select your ailment/disease:",
        ["Diabetes", "Blood Pressure", "Celiac Disease", "Lactose Intolerance", "Phenylketonuria (PKU)", 
         "Hypertension", "Hyperlipidemia", "Irritable Bowel Syndrome (IBS)", "Crohn's Disease", "Gallbladder Disease",
         "Chronic Kidney Disease", "Hepatic Encephalopathy", "Multiple Sclerosis", "Hashimoto's Thyroiditis",
         "Gout", "Anemia", "Galactosemia", "Fructose Intolerance", "Obesity", "Epilepsy", "Cancer"],
        help="Select one or more ailments to get recommendations"
    )

    # Barcode input
    barcode = st.text_input("Enter barcode of food product:", placeholder="e.g., 1234567890")


    # Safety check button
    if st.button("Test Food Safety"): 
        if barcode:
            # Mock safety status for the example (this should be fetched from your logic)
            safety_status = "green"  # You would replace this with actual logic
            if safety_status == "green": 
                st.success("✅ This food is safe for you!")
            elif safety_status == "yellow": 
                st.warning("⚠️ This food is moderately safe. Consume in limited quantities.")
            elif safety_status == "red": 
                st.error("❌ This food is not safe for you.")
            
            st.subheader("Recommendations / Alternatives")
            st.write("Here you can add recommendations or alternative products based on the selected ailment and food safety.")

        else:
            st.error("Please enter a barcode to test food safety.")