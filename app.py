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
Your food safety assistant for managing health conditions.
""")

# Configure sidebar for multiple pages 
pages = [st.Page("how_it_works.py", title="Learn About NutriSafe"), st.Page("check_food_safety.py", title="Try NutriSafe Out")]
pg = st.navigation(pages)
pg.run()
