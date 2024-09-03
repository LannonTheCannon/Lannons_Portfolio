import streamlit as st

import base64
import os
from PIL import Image


def display_resume():
    # Custom CSS
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 1rem;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: 600;
        color: #1E3A8A;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .stImage > img {
        width: 100%;
        margin-bottom: 2rem;
    }
    .highlight-text {
        color: #2563EB;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    #st.markdown('<h1 class="main-header">Lannon Khau - Resume</h1>', unsafe_allow_html=True)
    st.title('Lannon Khau - Resume')
    # Display resume images
    resume_image_path_1 = os.path.join(os.path.dirname(__file__), "assets", "_assets_Lannon_Khau_Resume_1.jpg")
    resume_image_path_2 = os.path.join(os.path.dirname(__file__), "assets", "_assets_Lannon_Khau_Resume_2.jpg")

    if os.path.exists(resume_image_path_1) and os.path.exists(resume_image_path_2):
        image1 = Image.open(resume_image_path_1)
        st.image(image1, use_column_width=True, caption="Lannon Khau's Resume - Page 1", output_format="JPEG")
        
        image2 = Image.open(resume_image_path_2)
        st.image(image2, use_column_width=True, caption="Lannon Khau's Resume - Page 2", output_format="JPEG")
    else:
        st.error("One or both resume images not found. Please check the file paths.")

    # Add Download Resume button
    #st.markdown('<h2 class="section-header">Download Resume</h2>', unsafe_allow_html=True)
    st.subheader('Download Resume')
    resume_pdf_path = os.path.join(os.path.dirname(__file__), "assets", "Lannon_Khau_Resume.pdf")
    
    if os.path.exists(resume_pdf_path):
        with open(resume_pdf_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="Download Resume PDF",
                           data=PDFbyte,
                           file_name="Lannon_Khau_Resume.pdf",
                           mime='application/pdf')
    else:
        st.error("Resume PDF file not found. Please check the file path.")


if __name__ == "__main__":
    st.set_page_config(page_title="Lannon Khau - Resume", layout="wide")
    display_resume()
