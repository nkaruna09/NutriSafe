import streamlit as st
import pandas as pd

# Sample data for user history
data = {
    "Barcode": ["123456789", "987654321", "456789123"],
    "Product Name": ["T-Shirt", "Sneakers", "Backpack"],
    "Color Received": ["Red", "Blue", "Black"],
    "Recommendation": ["Try White next time!", "Consider Green for variety.", "Explore Navy Blue options."],
}

# Convert data to a DataFrame
user_history_df = pd.DataFrame(data)

# Streamlit app
st.header("Barcode History Page")

# Display the table
st.markdown("### User Activity Table")
st.table(user_history_df)

st.markdown("### Insights")
st.write(
    "This table shows the user's purchase history and recommendations. Use this data to "
    "personalize their shopping experience or suggest future products."
)

# Caching the data transformation function
@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

# Prepare the CSV for download
csv = convert_df_to_csv(user_history_df)

st.download_button(
    label="Download History as CSV",
    data=csv,
    file_name="user_history.csv",
    mime="text/csv",
)
