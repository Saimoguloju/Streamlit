import streamlit as st
from PIL import Image
import cv2
import numpy as np

st.title("Image Annotation Tool")

uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    # Convert PIL image to OpenCV format
    opencv_image = np.array(image.convert("RGB"))
    opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_RGB2BGR)

    # Allow users to draw rectangles and annotate
    st.write("Use the tools below to annotate the image:")
    x = st.slider("X coordinate", 0, opencv_image.shape[1], 50)
    y = st.slider("Y coordinate", 0, opencv_image.shape[0], 50)
    width = st.slider("Width", 0, opencv_image.shape[1], 100)
    height = st.slider("Height", 0, opencv_image.shape[0], 100)
    annotation = st.text_input("Annotation text:")

    # Draw the rectangle and add annotation
    annotated_image = opencv_image.copy()
    cv2.rectangle(annotated_image, (x, y), (x + width, y + height), (0, 255, 0), 2)
    cv2.putText(annotated_image, annotation, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Convert back to PIL format for display
    annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
    annotated_image = Image.fromarray(annotated_image)

    st.image(annotated_image, caption="Annotated Image", use_column_width=True)
