import streamlit as st
from utils.analysis import check_healthiness
from utils.barcode_lookup import fetch_product_data
from utils.analysis import recommendations_alternatives

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
if not barcode.isdigit():
    st.error("Enter valid barcode.")
    
else:
    data = fetch_product_data(barcode)
    print(data)
    if data == 1:
            st.error("Invalid barcode entered.")
    elif data == 2:
            st.error("The ingredient list for this item is not available or it may not be a food item.")
    else:
        # Safety check button 
        if st.button("Test Food Safety"): 
            if barcode: 
                # Mock safety status for the example (this should be fetched from your logic)
                
                data = fetch_product_data(barcode)
                ingredients = data['ingredients'] 
                nutriments = data['nutriments']

                safety_status = check_healthiness(ingredients, nutriments, ailments)
                print(safety_status)
                if safety_status == "Green": # You would replace this with actual logic
                    st.success("✅ This food is safe for you!")
                elif safety_status == "Yellow": 
                    st.warning("⚠️ This food is moderately safe. Consume in limited quantities.")
                elif safety_status == "Red": 
                    st.error("❌ This food is not safe for you.")
        
                st.subheader("Recommendations/Alternatives")
                st.write(recommendations_alternatives(ingredients, nutriments, ailments)) 
                    
            else: 
                st.error("Please enter a barcode to test food safety.")
