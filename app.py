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

col1, col2 = st.columns([0.15, 0.85])

with col1:
    st.image("assets/nutrisafe_logo.png")
with col2:
    st.title("Welcome to NutriSafe!")

# Configure sidebar for multiple pages 
pages = [st.Page("how_it_works.py", title="Learn About NutriSafe"), st.Page("check_food_safety.py", title="Try NutriSafe Out"), st.Page("user_history.py", title="Barcode History"), st.Page("AI_chat_bot.py", title="Talk to our AI-chat bot!")]
pg = st.navigation(pages)
pg.run()

st.logo("assets/nutrisafe_small_logo.png")
