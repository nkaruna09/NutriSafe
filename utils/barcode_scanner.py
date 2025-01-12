import streamlit as st
from pyzbar.pyzbar import decode
from PIL import Image

# File uploader for image
# uploaded_file = st.file_uploader("Upload a barcode image", type=["png", "jpg", "jpeg"])

def scan_barcode(uploaded_file):
    if uploaded_file is not None:
        # Load the image directly from the uploaded file
        image = Image.open(uploaded_file)

        # Display the image in Streamlit
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Decode the barcode(s) from the image
        barcodes = decode(image)

        # Process and display the barcode data
        if barcodes:
            for barcode in barcodes:
                barcode_data = barcode.data.decode('utf-8')  # Convert byte data to string
                return barcode_data
        else:
            st.error("No barcodes found in the uploaded image.")
            return "Error."
