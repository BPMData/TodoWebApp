import streamlit as st
from PIL import Image

with st.expander("Start camera?"):
    camera_image = st.camera_input("Camera")

print(camera_image)

# UploadedFile(id=1, name='camera-input-2023-06-20T01_36_40.742Z.jpg', type='image/jpeg', size=347944)

if camera_image:
    # Create a Pillow image instance
    image = Image.open(camera_image)

    # Convert to greyscale
    gray_img = image.convert("L")

    # Display the image
    st.image(gray_img)

    st.write("This is what you would look like if u were hard-boiled O_o...")
    st.write("<b>Nothing personell, kid.......</b>", unsafe_allow_html=True)

# Coding Exercise on https://www.udemy.com/course/the-python-mega-course/learn/lecture/32954114#search

st.title("Wanna Ansel Adams your own picture? Select one here.")

uploaded = st.file_uploader("Upload Image to Anselize:", type=['png', 'jpg'])

if uploaded:
    upimg = Image.open(uploaded)
    upimg = upimg.convert("L")
    st.image(upimg)
    st.write("Woah...")