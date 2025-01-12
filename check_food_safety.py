import streamlit as st
from utils.analysis import check_healthiness
from utils.barcode_lookup import fetch_product_data
from utils.analysis import recommendations_alternatives
from utils.barcode_scanner import scan_barcode

# Display the food safety check section
st.header("Check Food Safety")
    
# Ailment/Disease selection
ailments = st.multiselect(
    "Select your ailment/disease:",
    ["Diabetes", "Blood Pressure", "Celiac Disease", "Lactose Intolerance", "Phenylketonuria (PKU)", 
     "Hypertension", "Hyperlipidemia", "Irritable Bowel Syndrome (IBS)", "Crohn's Disease", "Gallbladder Disease",
     "Chronic Kidney Disease", "Hepatic Encephalopathy", "Multiple Sclerosis", "Hashimoto's Thyroiditis",
     "Gout", "Anemia", "Galactosemia", "Fructose Intolerance", "Obesity", "Epilepsy", "Cancer"],
    help="Select one or more ailments/diseases to get recommendations."
)

user_allergen = st.multiselect(
    "Select any food allergies:",
    ["Peanuts", "Tree nuts", "Dairy (Milk)", "Eggs", "Wheat (Gluten)", "Soy", "Fish", "Shellfish", "Sesame", "Mustard", "Sulfites"], 
    help="Select any allergens you might have."
)

# Barcode input 
barcode = st.text_input("Enter barcode of food product:", placeholder="e.g., 1234567890")
uploaded_file = st.file_uploader("Upload a barcode image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    barcode = scan_barcode(uploaded_file)
    
# Safety check button 
if st.button("Test Food Safety"): 

    try:
        int(barcode)
    except ValueError or TypeError:
        barcode = None

    if barcode: 
        
        data = fetch_product_data(barcode)

        if data == "Product not found." or data == "Missing ingredients. This may not be a food item.":
            st.error(data)

        else:    
            print(data)        
            ingredients = data['ingredients'] 
            nutriments = data['nutriments']
            food_allergens = data['allergens']
            safety = ""
            safety_status = check_healthiness(ingredients, nutriments, user_allergen, food_allergens, ailments)
            print(safety_status)
            if safety_status == "Green": 
                st.success("✅ This food is safe for you!")
                safety = "safe"
            elif safety_status == "Yellow": 
                st.warning("⚠️ This food is moderately safe. Consume in limited quantities.")
                safety = "moderately safe"
            elif safety_status == "Red": 
                st.error("❌ This food is not safe for you.")
                safety = "not safe"
    
            st.subheader("Recommendations/Alternatives")
            st.write(recommendations_alternatives(ingredients, nutriments, user_allergen, food_allergens, ailments, safety)) 
             
    else: 
        st.error("Please enter a barcode to test food safety.")
