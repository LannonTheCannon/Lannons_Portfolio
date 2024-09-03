import streamlit as st
from PIL import Image
import os

def display_projects():
    st.title("My Projects")

    # Custom CSS for project cards with updated color scheme
    st.markdown("""
    <style>
    .project-card {
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        background-color: #ffffff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .project-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #333333;
    }
    .project-description {
        font-size: 16px;
        margin-bottom: 15px;
        color: #555555;
    }
    .project-tech {
        font-style: italic;
        color: #777777;
        margin-bottom: 15px;
    }
    .project-link {
        display: inline-block;
        padding: 8px 16px;
        background-color: white;
        color: white;
        text-decoration: none;
        border-radius: 4px;
        transition: background-color 0.3s ease;
    }
    .project-link:hover {
        background-color: #2c3e50;
    }
    </style>
    """, unsafe_allow_html=True)

    # List of projects
    projects = [
        {
            "title": "ExoExplorer: Machine Learning and AI-Enhanced Exoplanet Analysis",
            "description": "Developed a predictive model for exoplanet habitability scores with 85% accuracy using advanced machine learning techniques.",
            "image": "exoexplorer.jpg",
            "tech": "Python, Scikit-learn, TensorFlow, NASA Exoplanet Archive API",
            "link": "https://github.com/LannonTheCannon/Exoplanets_Prediction_Model.git"
        },
        {
            "title": "AI-Powered Real Estate Chatbot",
            "description": "Engineered a sophisticated AI chatbot processing over 500 unique real estate queries weekly with a 94% accuracy rate.",
            "image": "real-estate-chatbot.jpg",
            "tech": "Python, OpenAI API, Flask, React",
            "link": "https://github.com/LannonTheCannon/A_Plus_Realty_and_Mortgage_Chatbot.git"
        },
        {
            "title": "Chiropractic Patient Management System",
            "description": "Designed a SOAP notes system handling 200+ daily entries, improving documentation efficiency by 30%.",
            "image": "chiro-management.jpg",
            "tech": "Python, Django, PostgreSQL, React",
            "link": "https://github.com/LannonTheCannon/Body_RES_SOAP_Reporting.git"
        }
    ]

    # Display projects
    for project in projects:
        with st.container():
            st.markdown(f"""
            <div class="project-card">
                <div class="project-title">{project['title']}</div>
                <div class="project-description">{project['description']}</div>
                <div class="project-tech">Technologies: {project['tech']}</div>
                <a class="project-link" href="{project['link']}" target="_blank">View Project</a>
            </div>
            """, unsafe_allow_html=True)
            
##            # Display project image if it exists
##            image_path = os.path.join(os.path.dirname(__file__), "assets", project['image'])
##            if os.path.exists(image_path):
##                image = Image.open(image_path)
##                st.image(image, use_column_width=True)
##            else:
##                st.warning(f"Image not found for {project['title']}")

if __name__ == "__main__":
    st.set_page_config(page_title="My Projects", layout="wide")
    display_projects()
