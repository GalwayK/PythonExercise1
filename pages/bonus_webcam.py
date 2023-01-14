import streamlit as st
from PIL import Image
#
#
# def convert_image_greyscale(st_img):
#     image_img = Image.open(st_img)
#     return image_img.convert("L")
#
#
# uploaded_image = st.file_uploader("Upload file: ")
# if uploaded_image:
#     grey_upload_image = convert_image_greyscale(uploaded_image)
#     st.image(grey_upload_image)
#
# with st.expander("Start Camera"):
#     st_camera_image = st.camera_input("Camera")
# if st_camera_image:
#     grey_camera_img = convert_image_greyscale(st_camera_image)
#     st.image(grey_camera_img)
#
# st.slider("Amount", min_value=10, max_value=30)
#
# st.write("What is 15 * 2: ")
# user_choice = st.radio("Amount", options=[10, 20, 30])
# if user_choice == 30:
#     st.info("Correct!")
#
# # ----- #

def convert_image(input_image):
    """Gets a PIL image file and returns its grayscale version"""
    img = Image.open(input_image)
    gray_img = img.convert('L')
    return gray_img


st.subheader("Color to Grayscale Converter")

# Create a file uploader component allowing the user to upload a file
uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    # Supply camera_image to convert_image to get the grayscale version
    gray_camera_image = convert_image(camera_image)
    st.image(gray_camera_image)

# Check if the image exists meaning the user has uploaded a file
if uploaded_image:
    # Supply camera_image to convert_image to get the grayscale version
    gray_uploaded_image = convert_image(uploaded_image)
    st.image(gray_uploaded_image)
