import streamlit as st

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