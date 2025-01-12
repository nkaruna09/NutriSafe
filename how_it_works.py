import streamlit as st

# Display how it works section
st.subheader("How NutriSafe Works")
st.write("""
    1. **Select your ailment/disease** and any **allergens** from the options.
    2. **Enter or upload a picture of the barcode** of the food product you want to check.
    3. **Get the safety status** along with recommendations or alternatives.
    """)

# Button to start checking food safety
if st.button("Start Checking Food Safety"):
    st.switch_page("check_food_safety.py")
