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

# Allergen selection
user_allergen = st.multiselect(
    "Select any food allergies:",
    ["Peanuts", "Tree Nuts", "Dairy (Milk)", "Eggs", "Wheat (Gluten)", "Soy", "Fish", "Shellfish", "Sesame", "Mustard", "Sulfites"], 
    help="Select any allergens you might have."
)

# Barcode input method selection
method = st.segmented_control(
    "Choose how to input the barcode:",
    options=["Enter barcode number as text", "Upload a barcode image"]
)

barcode = None
if method == "Enter barcode number as text":
    barcode = st.text_input("Enter barcode number of food product:", placeholder="e.g., 1234567890")
elif method == "Upload a barcode image":
    # Inject CSS for custom styling
    st.markdown(
        """
        <style>
        /* Target the file uploader label to change the font color */
        .stFileUploader label {
            color: green;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader("Upload a barcode image:", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        barcode = scan_barcode(uploaded_file)

# Safety check button
if st.button("Test Food Safety"):
    try:
        # Ensure the barcode is valid
        if barcode is None or not str(barcode).isdigit():
            raise ValueError("Invalid barcode")
        
        # Fetch product data
        data = fetch_product_data(barcode)

        if data in ["Product not found.", "Missing ingredients. This may not be a food item."]:
            st.error(data)
        else:
            # Extract relevant data
            ingredients = data['ingredients']
            nutriments = data['nutriments']
            food_allergens = data['allergens']
            
            # Check healthiness
            safety_status = check_healthiness(ingredients, nutriments, user_allergen, food_allergens, ailments)
            if safety_status == "Green":
                st.success("✅ This food is safe for you!")
            elif safety_status == "Yellow":
                st.warning("⚠️ This food is moderately safe. Consume in limited quantities.")
            elif safety_status == "Red":
                st.error("❌ This food is not safe for you.")
            
            # Display recommendations
            st.subheader("Recommendations/Alternatives")
            st.write(recommendations_alternatives(ingredients, nutriments, user_allergen, food_allergens, ailments, safety_status))
    except ValueError as e:
        st.error("Please provide a valid barcode (text or image).")

