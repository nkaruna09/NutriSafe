import streamlit as st
from utils.analysis import check_healthiness
from utils.barcode_lookup import fetch_product_data
from utils.analysis import recommendations_alternatives
from utils.barcode_scanner import scan_barcode
import matplotlib.pyplot as plt

# Display the food safety check section
st.header("Check Food Safety")
    
# Ailment/Disease selection
ailments = st.multiselect(
    "Select your ailment/disease:",
    ["Anemia", "Cancer", "Celiac Disease", "Chronic Kidney Disease", "Crohn's Disease", "Diabetes", "Epilepsy", 
     "Fructose Intolerance", "Galactosemia", "Gallbladder Disease", "Gout", "Hashimoto's Thyroiditis", 
     "Hepatic Encephalopathy", "Hyperlipidemia", "Hypertension", "Hypotension", "Irritable Bowel Syndrome (IBS)",
     "Lactose Intolerance", "Phenylketonuria (PKU)", "Multiple Sclerosis", "Obesity"],
    help="Select one or more ailments/diseases to get recommendations."
)

# Allergen selection
user_allergen = st.multiselect(
    "Select any food allergies:",
    ["Dairy (Milk)", "Eggs", "Fish", "Mustard", "Peanuts", "Sesame", "Shellfish", "Soy", "Sulfites", "Tree Nuts", "Wheat (Gluten)"], 
    help="Select any allergies you might have."
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
            safety = ""
            
            if safety_status == "Green":
                st.success("✅ This food is safe for you!")
                safety = "safe"
            elif safety_status == "Yellow":
                st.warning("⚠️ This food is moderately safe. Consume in limited quantities.")
                safety = "moderately safe"
            elif safety_status == "Red":
                st.error("❌ This food is not safe for you.")
                safety = "unsafe"

            if "ingredient_breakdown" in data.keys():
                ingredient_breakdown = data["ingredient_breakdown"]

                labels = list(ingredient_breakdown.keys())
                sizes = list(ingredient_breakdown.values())

                # Create a Streamlit app with a pie chart
                st.subheader("Ingredient Composition Pie Chart")

                # Create the pie chart
                fig, ax = plt.subplots()
                ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
                ax.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle
                fig.patch.set_facecolor('#e8f5e9')


                # Display the pie chart in Streamlit
                st.pyplot(fig)
            
            # Display recommendations
            st.subheader("Recommendations/Alternatives")
            st.write(recommendations_alternatives(ingredients, nutriments, user_allergen, food_allergens, ailments, safety))

    except ValueError as e:
        st.error("Please provide a valid barcode (text or image).")


