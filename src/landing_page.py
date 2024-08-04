# home_page.py
# This script will handle all the functions related to the home page, including:
# 1. Hero Section
# 2. Skills Package
# 3. Student Projects
# 4. Services Provided
#
################################################################################################################
import streamlit as st
import base64
import os
from utils.styles import get_styles_landing

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def display_home():
    # Get the path to the images
    about_image_path = os.path.join(os.path.dirname(__file__), "../images", "profile.jpg")
    project_image_path = os.path.join(os.path.dirname(__file__), "../images", "boy_and_dog.png")
    project_image_path1 = os.path.join(os.path.dirname(__file__), "../images", "boy_and_dog.png")
    project_image_path2 = os.path.join(os.path.dirname(__file__), "../images", "boy_and_dog.png")
    project_image_path3 = os.path.join(os.path.dirname(__file__), "../images", "boy_and_dog.png")

    # Encode the images
    about_image_base64 = get_base64_of_bin_file(about_image_path)
    project_image_base64 = get_base64_of_bin_file(project_image_path)
    project_image_base64 = get_base64_of_bin_file(project_image_path)
    project_image_base64 = get_base64_of_bin_file(project_image_path)
    project_image_base64 = get_base64_of_bin_file(project_image_path)

    st.markdown(get_styles_landing(), unsafe_allow_html=True)

    # Use a container to add padding around the headers
    with st.container():
        st.markdown('<h1 class="main-header">Empower Your Child\'s Future: Code, Create, and Innovate with AI 🌟</h1>', unsafe_allow_html=True)
        st.markdown('<p class="sub-header">6-Month Web Development Bootcamp with Personalized AI Chatbot Integration</p>', unsafe_allow_html=True)

    st.markdown("""
    <style>
    .centered-button {
        display: flex;
        justify-content: center;
    }
    .custom-button {
        font-size: 18px;
        padding: 12px 24px;
        border-radius: 5px;
        background-color: #3498db;  /* Change this to match your color scheme */
        color: white;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3), 0 1px 3px rgba(0, 0, 0, 0.08);
    }
    .custom-button:hover {
        background-color: #2980b9;  /* Darker shade for hover effect */
        box-shadow: 0 7px 14px rgba(0, 0, 0, 0.1), 0 3px 6px rgba(0, 0, 0, 0.08);
        transform: translateY(-1px);
    }
    .custom-button:active {
        background-color: #2573a7;  /* Even darker shade for click effect */
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
        transform: translateY(1px);
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="centered-button">
        <button class="custom-button" onclick="showMessage()">Get Started</button>
    </div>
    <script>
    function showMessage() {
        alert("Get Started!");
    }
    </script>
    """, unsafe_allow_html=True)

    # About Me
    st.markdown('<h2 class="section-header"> Beyond Coding 🌠</h2>', unsafe_allow_html=True)
    about_me_html = f"""
    <div class="card">
        <div class="row-container">
            <div class="image-container">
                <img src="data:image/png;base64,{about_image_base64}" class="custom-image">
            </div>
            <div class="text-container">
                <p>
                As a Streamlit enthusiast and AI specialist, I create data-driven websites 
                with integrated AI chatbots tailored for businesses. Currently, I work as a 
                Data Quality Analyst at Scale AI, training cutting-edge AI models. 
                Additionally, I'm passionate about educating the next generation of coders, 
                helping students master Python and prepare for the PCEP exam.
                </p>
            </div>
        </div>
    </div>
    """
    st.markdown(about_me_html, unsafe_allow_html=True)

    # Skills
    st.markdown("""
    <div style="background-color: #2c3e50; padding: 40px 0; margin: 40px -5rem;">
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
            <h2 style="color: white; text-align: center; margin-bottom: 30px; font-size: 2.5rem;">Skills Package 🧰</h2>
            <div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
                <div style="width: 22%; background-color: white; border-radius: 10px; padding: 20px; margin-bottom: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);">
                    <h3 style="color: #3d405b; margin: 0; font-size: 1.4rem;">Python</h3>
                    <p style="font-size: 2rem; font-weight: bold; color: #e07a5f; margin: 10px 0;">95%</p>
                    <p style="color: #3d405b; font-size: 0.9rem; margin-top: 10px;">Proficient in data analysis, web development, and automation.</p>
                </div>
                <div style="width: 22%; background-color: white; border-radius: 10px; padding: 20px; margin-bottom: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);">
                    <h3 style="color: #3d405b; margin: 0; font-size: 1.4rem;">Streamlit</h3>
                    <p style="font-size: 2rem; font-weight: bold; color: #e07a5f; margin: 10px 0;">90%</p>
                    <p style="color: #3d405b; font-size: 0.9rem; margin-top: 10px;">Expert in creating interactive web applications and dashboards.</p>
                </div>
                <div style="width: 22%; background-color: white; border-radius: 10px; padding: 20px; margin-bottom: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);">
                    <h3 style="color: #3d405b; margin: 0; font-size: 1.4rem;">AI/ML</h3>
                    <p style="font-size: 2rem; font-weight: bold; color: #e07a5f; margin: 10px 0;">85%</p>
                    <p style="color: #3d405b; font-size: 0.9rem; margin-top: 10px;">Experienced in developing and implementing machine learning models.</p>
                </div>
                <div style="width: 22%; background-color: white; border-radius: 10px; padding: 20px; margin-bottom: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);">
                    <h3 style="color: #3d405b; margin: 0; font-size: 1.4rem;">Data Analysis</h3>
                    <p style="font-size: 2rem; font-weight: bold; color: #e07a5f; margin: 10px 0;">88%</p>
                    <p style="color: #3d405b; font-size: 0.9rem; margin-top: 10px;">Skilled in data visualization, statistical analysis, and insights generation.</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Featured Projects
    st.markdown('<h2 class="section-header">Student Projects 👨‍💻</h2>', unsafe_allow_html=True)
    projects = [
        ("Chiropractor Health Records", project_image_base64),
        ("News Nerd Hacker Bot", project_image_base64),
        ("Professional Portfolio App", project_image_base64)
    ]
    project_cols = st.columns(len(projects))
    for col, (title, image) in zip(project_cols, projects):
        col.markdown(f"""
        <div class="card">
            <img src="data:image/png;base64,{image}" style="width:100%;">
            <h3>{title}</h3>
        </div>
        """, unsafe_allow_html=True)

    # Services
    st.markdown('<h2 class="section-header">Services 🛠️</h2>', unsafe_allow_html=True)
    services = ["🤖 AI Chatbot Development", "📊 Data Website Creation", "🐍 Python Tutoring"]
    service_cols = st.columns(len(services))
    for col, service in zip(service_cols, services):
        col.markdown(f"""
        <div class="card">
            <h3>{service}</h3>
        </div>
        """, unsafe_allow_html=True)
