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
        background-color: #3498db; 
        color: white;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3), 0 1px 3px rgba(0, 0, 0, 0.08);
    }
    .custom-button:hover {
        background-color: #2980b9; 
        box-shadow: 0 7px 14px rgba(0, 0, 0, 0.1), 0 3px 6px rgba(0, 0, 0, 0.08);
        transform: translateY(-1px);
    }
    .custom-button:active {
        background-color: #2573a7;  
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

    st.write('')

    # Camp Overview
    st.markdown('<h2 class="section-header">Empowering Future Innovators 🚀</h2>', unsafe_allow_html=True)
    camp_overview_html = f"""
    <div class="card">
        <div class="row-container">
            <div class="text-container">
                <p>
                Our <strong>innovative coding camp</strong> is meticulously designed to transform <strong>high school students</strong> into <strong>tech-savvy professionals</strong> through <strong>four comprehensive levels</strong>:
                </p>
                <ol>
                    <li><strong>Foundation:</strong> Master Python fundamentals and earn PCEP certification</li>
                    <li><strong>Application:</strong> Develop dynamic web applications using Streamlit</li>
                    <li><strong>Analysis:</strong> Harness the power of data with advanced visualization techniques</li>
                    <li><strong>Innovation:</strong> Create and integrate AI chatbots for real-world applications</li>
                </ol>
                <p>
                This <strong>Structured Approach</strong> not only builds <strong>critical coding skills</strong> but also cultivates <strong>problem-solving abilities</strong> and <strong>creative thinking</strong> – essential qualities for success in the digital age.
                </p>
                <p>
                Throughout the camp, students will create tangible, impressive projects that form a <strong>professional portfolio</strong>. This portfolio showcases their skills to <strong>potential employers or college admissions</strong>, giving them a significant <strong>competitive edge</strong> in their future endeavors.
                </p>
                <p>
                Our <strong>curriculum</strong> is aligned with <strong>current industry demands</strong>, preparing students for <strong>high-growth careers</strong> in tech. From Python programming to AI integration, students gain <strong>practical experience</strong> with tools and technologies used by <strong>leading tech companies</strong>, positioning them for success in a rapidly evolving digital landscape.
                </p>
            </div>
        </div>
    </div>
    """
    st.markdown(camp_overview_html, unsafe_allow_html=True)

    # Skills
    st.markdown("""
        <div style="background-color: #2c3e50; padding: 40px 0; margin: 40px -5rem;">
            <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
                <h2 style="color: white; text-align: center; margin-bottom: 30px; font-size: 2.5rem;">Skills Package 🧰</h2>
                <div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
                    <div style="width: 22%; background-color: white; border-radius: 10px; padding: 20px; margin-bottom: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);">
                        <h3 style="color: #3d405b; margin: 0; font-size: 1.4rem;">Python Programming</h3>
                        <p style="font-size: 2rem; font-weight: bold; color: #e07a5f; margin: 10px 0;">Level 1</p>
                        <p style="color: #3d405b; font-size: 0.9rem; margin-top: 10px;">Comprehensive curriculum covering PCEP-1 Certification objectives.</p>
                    </div>
                    <div style="width: 22%; background-color: white; border-radius: 10px; padding: 20px; margin-bottom: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);">
                        <h3 style="color: #3d405b; margin: 0; font-size: 1.4rem;">Streamlit Web Development</h3>
                        <p style="font-size: 2rem; font-weight: bold; color: #e07a5f; margin: 10px 0;">Level 2</p>
                        <p style="color: #3d405b; font-size: 0.9rem; margin-top: 10px;">Advanced techniques for creating responsive, data-driven web applications.</p>
                    </div>
                    <div style="width: 22%; background-color: white; border-radius: 10px; padding: 20px; margin-bottom: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);">
                        <h3 style="color: #3d405b; margin: 0; font-size: 1.4rem;">Data Analysis & Visualization</h3>
                        <p style="font-size: 2rem; font-weight: bold; color: #e07a5f; margin: 10px 0;">Level 3</p>
                        <p style="color: #3d405b; font-size: 0.9rem; margin-top: 10px;">Proficiency in constructing and maintaining professional-grade analytical dashboards.</p>
                    </div>
                    <div style="width: 22%; background-color: white; border-radius: 10px; padding: 20px; margin-bottom: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);">
                        <h3 style="color: #3d405b; margin: 0; font-size: 1.4rem;">AI Chatbot Integration</h3>
                        <p style="font-size: 2rem; font-weight: bold; color: #e07a5f; margin: 10px 0;">Level 4</p>
                        <p style="color: #3d405b; font-size: 0.9rem; margin-top: 10px;">Expertise in developing and training customized AI-powered chatbots.</p>
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
            <h3 style="color: #444444;">{title}</h3>
        </div>
        """, unsafe_allow_html=True)

    st.write('')
    st.markdown('<h2 class="section-header">Other Services 🛠️</h2>', unsafe_allow_html=True)
    services = ["🤖 AI Chatbot Development", "📊 Data Website Creation", "🐍 Python Coaching"]
    service_cols = st.columns(len(services))
    for col, service in zip(service_cols, services):
        col.markdown(f"""
        <div class="card">
            <h3 style="color: #444444;">{service}</h3>
        </div>
        """, unsafe_allow_html=True)
