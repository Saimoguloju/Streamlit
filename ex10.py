import streamlit as st
from PIL import Image
import time

st.title("Progressive Image Loading")

# List of image files to load (replace with your own images)
image_files = ["i1.jpg", "i2.jpg", "i3.jpg"]

for image_file in image_files:
    image = Image.open(image_file)
    st.image(image, caption=image_file, use_column_width=True)
    time.sleep(2)  # Simulate loading time
