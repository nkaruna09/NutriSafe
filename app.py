import streamlit as st
#import requests
#import openai
#from utils.barcode_lookup import fetch_product_data, is_food_item
#from utils.drug_list import fetch_drug_list
#from utils.analysis import analyze_interaction

st.set_page_config(page_title="NutriSafe", layout="centered")

# Load Custom CSS
with open("styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("NutriSafe")
st.write("Check the safety of food items and get recommendations")

ailments = st.multiselect(
    "Select your ailment/disease:",
    ["Diabetes", "Blood Pressure", "Celiac Disease", "Lactose Intolerance", "Phenylketonuria (PKU)", 
     "Hypertension", "Hyperlipidemia", "Irritable Bowel Syndrome (IBS)", "Crohn's Disease", "Gallbladder Disease",
     "Chronic Kidney Disease", "Hepatic Encephalopathy", "Multiple Sclerosis", "Hashimoto's Thyroiditis",
     "Gout", "Anemia", "Galactosemia", "Fructose Intolerance", "Obesity", "Epilepsy", "Cancer"],
    help="Select one or more ailments to get recommendations"
)

barcode = st.text_input("Enter Barcode:", placeholder="e.g., 1234567890")

if st.button("Test Food Safety"): 
    if barcode: 

        if safety_status == "green": 
            st.success("✅ This food is safe for you!")
        elif safety_status == "yellow": 
            st.warning("⚠️ This food is moderately safe. Consume in limited quantities.")
        elif safety_status == "red": 
            st.error("❌ This food is not safe for you.")

        st.subheader("Recommendations / Alternatives")
        
    else: 
        st.error("Please enter a barcode to test food safety.")