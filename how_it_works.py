import streamlit as st

# Display how it works section
st.subheader("How NutriSafe Works")

st.write("1. **Select your ailment/disease** and any **allergens** from the options.")

# First video demonstration 
ailment_video = open("assets/select_your_ailment_disease.mp4", "rb")
ailment_vid_bytes = ailment_video.read()
st.video(ailment_vid_bytes)

# Second video demonstration 
allergy_video = open("assets/select_allergy.mp4", "rb")
allergy_vid_bytes = allergy_video.read()
st.video(allergy_vid_bytes)

st.write("2. **Enter or upload a picture of the barcode** of the food product you want to check.")

# Third video demonstration 
barcode_video = open("assets/barcode.mp4", "rb")
barcode_vid_bytes = barcode_video.read()
st.video(barcode_vid_bytes)

st.write("3. **Get the safety status** along with recommendations or alternatives.")

# Fourth video demonstration 
status_video = open("assets/safety_status.mp4", "rb")
status_vid_bytes = status_video.read()
st.video(status_vid_bytes)

# Button to start checking food safety
if st.button("Start Checking Food Safety"):
    st.switch_page("check_food_safety.py")
