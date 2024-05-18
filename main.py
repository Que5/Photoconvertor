import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Convertor")


uploaded_image = st.file_uploader("Upload image")


with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")


if camera_image:
    # pillow image instance
    img = Image.open(camera_image)

    # convert the image to grayscale
    gray_img = img.convert("L")

    # Render the greyscale image on the web page
    st.image(gray_img)


if uploaded_image:
    img = Image.open("uploaded_image")
    converted_image = img.convert("L")
    st.image(converted_image)


