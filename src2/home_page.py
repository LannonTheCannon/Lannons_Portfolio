# home_page.py
import streamlit as st
import os
import base64
from datetime import datetime, date

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def display_contact_info():
    if 'show_contact' not in st.session_state:
        st.session_state.show_contact = False
    
    if st.button('Contact Me'):
        st.session_state.show_contact = not st.session_state.show_contact

    if st.session_state.show_contact:
        st.markdown("""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; margin-top: 20px;">
            <h3>Contact Information</h3>
            <p><strong>Email:</strong> khaulannon@instack.live</p>
            <p><strong>Phone:</strong> (626) 977-3921</p>
            <p><strong>GitHub:</strong> <a href="https://github.com/LannonTheCannon" target="_blank">https://github.com/LannonTheCannon</a></p>
        </div>
        """, unsafe_allow_html=True)

def display_home():
    # Custom CSS for the section box
    # Hero Section
    st.title('Welcome to Lannon\'s Portfolio')
    st.subheader('Slow is smooth. Smooth is fast.')

    # Get the path to the image for the About Me section
    about_image_path = os.path.join(os.path.dirname(__file__), "images", "boy_and_dog.png")

    # Encode the image
    about_image_base64 = get_base64_of_bin_file(about_image_path)

    # About Me
    about_me_html = f"""
    <div class="custom-container">
        <div class="row-container">
            <div class="image-container">
                <img src="data:image/png;base64,{about_image_base64}" class="custom-image">
            </div>
            <div class="text-container">
                <h3>About Me</h3>
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

      # Custom CSS for the timeline
    st.markdown("""
    <style>
    .timeline {
        position: relative;
        max-width: 800px;
        margin: 0 auto;
        background: rgba(70, 99, 101, 0.1);  /* Lighter shade of #466365 with transparency */
        padding: 20px 0;
        border-radius: 10px;
    }
    .timeline::after {
        content: '';
        position: absolute;
        width: 4px;
        background-color: #466365;  /* Darker shade from the gradient */
        top: 0;
        bottom: 0;
        left: 50%;
        margin-left: -2px;
    }
    .container {
        padding: 5px 10px;
        position: relative;
        background-color: inherit;
        width: 50%;
    }
    .container::after {
        content: '';
        position: absolute;
        width: 16px;
        height: 16px;
        right: -8px;
        background-color: #DAE3E5;  /* Light color from the gradient */
        border: 3px solid #466365;  /* Darker shade from the gradient */
        top: 15px;
        border-radius: 50%;
        z-index: 1;
    }
    .left {
        left: 0;
    }
    .right {
        left: 50%;
    }
    .left::before {
        content: " ";
        height: 0;
        position: absolute;
        top: 18px;
        width: 0;
        z-index: 1;
        right: 20px;
        border: medium solid #DAE3E5;
        border-width: 8px 0 8px 8px;
        border-color: transparent transparent transparent #DAE3E5;
    }
    .right::before {
        content: " ";
        height: 0;
        position: absolute;
        top: 18px;
        width: 0;
        z-index: 1;
        left: 20px;
        border: medium solid #DAE3E5;
        border-width: 8px 8px 8px 0;
        border-color: transparent #DAE3E5 transparent transparent;
    }
    .right::after {
        left: -8px;
    }
    .content {
        padding: 10px 15px;
        background-color: #DAE3E5;  /* Light color from the gradient */
        position: relative;
        border-radius: 6px;
        font-size: 0.9em;
    }
    .content h2 {
        color: #466365;  /* Darker shade from the gradient */
        margin-bottom: 5px;
        font-size: 1.5em;
    }
    .content .date {
        color: #466365;  /* Darker shade from the gradient */
        font-style: italic;
        font-size: 1.2em;
        margin-bottom: 5px;
    }
    .content p {
        margin: 0;
        line-height: 1.2;
        color: #333;  /* Darker text for better readability */
    }
    @media screen and (max-width: 600px) {
        /* ... (mobile styles remain the same) ... */
    }
    </style>
    """, unsafe_allow_html=True)

    st.subheader('Career Timeline')

    # Timeline HTML
    timeline_html = """
    <div class="timeline">
        <div class="container right">
            <div class="content">
                <h2>Data Quality Analyst at Scale AI</h2>
                <p class="date">April 2024 - Present</p>
                <p>Training cutting-edge AI models and ensuring data quality.</p>
            </div>
        </div>
        <div class="container left">
            <div class="content">
                <h2>Software Developer at InStack AI Solutions</h2>
                <p class="date">June 2022 - Present</p>
                <p>Developing AI-powered solutions and data-driven websites.</p>
            </div>
        </div>
        <div class="container right">
            <div class="content">
                <h2>Data Analyst at Logic Labs LLC</h2>
                <p class="date">May 2021 - February 2023</p>
                <p>Conducted data analysis for business decision-making.</p>
            </div>
        </div>
        <div class="container left">
            <div class="content">
                <h2>Graduated from CSU Fullerton</h2>
                <p class="date">August 2021</p>
                <p>Earned a degree in Computer Science (AI and Data Science).</p>
            </div>
        </div>
    </div>
    """

    st.markdown(timeline_html, unsafe_allow_html=True)

    # Skills and Technologies
    st.header('Skills & Technologies')
    
    skills = [
        {
            "category": "Programming Languages",
            "items": [
                {"name": "Python", "details": "4 years experience, expert in data analysis, web dev, and AI"},
                {"name": "SQL", "details": "3 years experience, proficient in complex queries and database design"},
                {"name": "JavaScript", "details": "2 years experience, used in web development projects"}
            ]
        },
        {
            "category": "Frameworks & Libraries",
            "items": [
                {"name": "Streamlit", "details": "Created 10+ data apps, including this portfolio"},
                {"name": "TensorFlow", "details": "Implemented in 5 machine learning projects"},
                {"name": "Pandas", "details": "Used extensively in data analysis and cleaning"}
            ]
        },
        {
            "category": "Tools & Technologies",
            "items": [
                {"name": "Git", "details": "Daily use for version control and collaboration"},
                {"name": "Docker", "details": "Used for containerizing and deploying applications"},
                {"name": "AWS", "details": "Experience with EC2, S3, and Lambda services"}
            ]
        }
    ]

    # Custom CSS for skills section
    st.markdown("""
    <style>
    .skill-category {
        font-size: 20px;
        font-weight: bold;
        margin-top: 0px;
        margin-bottom: 10px;
    }
    .skill-item {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .skill-name {
        font-weight: bold;
        font-size: 16px;
    }
    .skill-details {
        font-size: 16px;
        color: #555;
        margin-top: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Display skills
    for category in skills:
        st.markdown(f"<div class='skill-category'>{category['category']}</div>", unsafe_allow_html=True)
        for item in category['items']:
            st.markdown(f"""
            <div class="skill-item">
                <div class="skill-name">{item['name']}</div>
                <div class="skill-details">{item['details']}</div>
            </div>
            """, unsafe_allow_html=True)


    # Featured Projects
    st.header('Featured Projects')

    projects = [
        {
            "title": "NASA Exoplanet Archive",
            "image": "Exoplanets.jpg",
            "description": "Analysis and visualization of exoplanet data from NASA's archive, providing insights into planetary systems beyond our solar system.",
            "tech_stack": ["Python", "Pandas", "Tensorflow", "Scikit-learn" ,"Matplotlib", "Streamlit"]
        },
        {
            "title": "Real Estate AI Integration",
            "image": "Real_Estate.png",
            "description": "AI-powered platform for real estate market analysis, predicting property values and identifying investment opportunities.",
            "tech_stack": ["Streamlit", "OpenAI API", "LangChain", "NL2SQL", "PostGres", "Python"]
        },
        {
            "title": "Medical AI Diagnostics",
            "image": "Health_AI.jpg",
            "description": "Machine learning model for early detection of diseases using medical imaging, improving diagnostic accuracy and speed.",
            "tech_stack": ["Streamlit", "Python", "Postgres"]
        }
    ]

    # Custom CSS for project section
    st.markdown("""
    <style>
    .project-card {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        height: 100%;
    }
    .project-image {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .project-title {
        font-weight: bold;
        font-size: 18px;
        margin-bottom: 10px;
    }
    .project-description {
        font-size: 16px;
        color: #555;
        margin-bottom: 10px;
    }
    .project-tech {
        font-size: 16px;
        color: #888;
    }
    .tech-tag {
        background-color: #e0e0e0;
        padding: 3px 7px;
        border-radius: 3px;
        margin-right: 5px;
        display: inline-block;
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Display projects side by side
    cols = st.columns(3)
    for idx, project in enumerate(projects):
        with cols[idx]:
            image_path = os.path.join(os.path.dirname(__file__), "images", project["image"])
            image_base64 = get_base64_of_bin_file(image_path)
            
            st.markdown(f"""
            <div class="project-card">
                <img src="data:image/png;base64,{image_base64}" class="project-image">
                <div class="project-title">{project['title']}</div>
                <div class="project-description">{project['description']}</div>
                <div class="project-tech">
                    {"".join(f'<span class="tech-tag">{tech}</span>' for tech in project['tech_stack'])}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Services
    st.header('Services')
    
    services = [
        {
            "name": "AI Chatbot Development",
            "icon": "🤖",
            "description": "Custom AI chatbot solutions for businesses, integrating natural language processing and machine learning for enhanced customer interactions.",
            "key_points": [
                "Tailored chatbot development using state-of-the-art AI technologies",
                "Integration with existing business systems and workflows",
                "Continuous improvement and learning capabilities"
            ]
        },
        {
            "name": "Data Website Creation",
            "icon": "📊",
            "description": "Developing interactive, data-driven websites and dashboards using Streamlit and other modern web technologies.",
            "key_points": [
                "Custom data visualization and interactive elements",
                "Real-time data processing and display",
                "User-friendly interfaces for complex data analysis"
            ]
        },
        {
            "name": "Python Skills Development",
            "icon": "🐍",
            "description": "Comprehensive Python training programs for individuals and teams, focusing on practical applications in data science and AI.",
            "key_points": [
                "Customized curriculum based on skill level and goals",
                "Hands-on projects and real-world problem solving",
                "Preparation for Python certification exams (e.g., PCEP)"
            ]
        }
    ]

    # Custom CSS for services section
    st.markdown("""
    <style>
    .service-container {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .service-header {
        display: flex;
        align-items: center;
        margin-bottom: 10px;
    }
    .service-icon {
        font-size: 24px;
        margin-right: 10px;
    }
    .service-name {
        font-weight: bold;
        font-size: 18px;
    }
    .service-description {
        font-size: 16px;
        color: #555;
        margin-bottom: 10px;
    }
    .service-key-points {
        font-size: 14px;
        margin-left: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Display services
    for service in services:
        st.markdown(f"""
        <div class="service-container">
            <div class="service-header">
                <span class="service-icon">{service['icon']}</span>
                <span class="service-name">{service['name']}</span>
            </div>
            <div class="service-description">{service['description']}</div>
            <ul class="service-key-points">
                {"".join(f"<li>{point}</li>" for point in service['key_points'])}
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Call to Action
    st.header('Get in Touch')
    display_contact_info()
