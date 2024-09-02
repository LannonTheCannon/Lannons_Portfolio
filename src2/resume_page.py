import streamlit as st
from streamlit_timeline import st_timeline
import base64
import os

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{bin_file}">Download {file_label}</a>'
    return href

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
        color: #2563EB;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        font-weight: 600;
        color: #4B5563;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    .normal-text {
        font-size: 1rem;
        color: #1F2937;
    }
    .highlight-text {
        color: #2563EB;
        font-weight: 600;
    }
    .card {
        border-radius: 0.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        padding: 1rem;
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown('<h1 class="main-header">Lannon Khau - Resume</h1>', unsafe_allow_html=True)
    st.markdown('<p class="normal-text">San Dimas, CA 91773 | (626) 977-3921 | khaulannon@gmail.com</p>', unsafe_allow_html=True)

    # Professional Summary
    st.markdown('<h2 class="section-header">Professional Summary</h2>', unsafe_allow_html=True)
    st.markdown('<div class="card"><p class="normal-text">Data Scientist and Software Engineer with expertise in data analysis, visualization, and application development. Proven track record in delivering data-driven solutions from ideation to completion.</p></div>', unsafe_allow_html=True)

    # Skills
    st.markdown('<h2 class="section-header">Skills</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<h3 class="sub-header">Technical Skills</h3>', unsafe_allow_html=True)
        skills = [
            "Programming: Python, JavaScript, HTML, CSS",
            "Web Development: Streamlit, RESTful API, Flask, Django",
            "Data Analysis: Pandas, NumPy, Seaborn, Matplotlib",
            "Machine Learning & AI: Scikit-learn, TensorFlow, OpenAI API, NLP"
        ]
        for skill in skills:
            st.markdown(f'<p class="normal-text">• {skill}</p>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<h3 class="sub-header">Other Skills</h3>', unsafe_allow_html=True)
        other_skills = [
            "Database Management: MySQL, PostgreSQL, SQLite",
            "Version Control: Git, GitHub",
            "Data Visualization: Seaborn, Matplotlib, Nivo, Plotly",
            "Development Tools: Jupyter, TKinter, Streamlit"
        ]
        for skill in other_skills:
            st.markdown(f'<p class="normal-text">• {skill}</p>', unsafe_allow_html=True)

    # Work History
    st.markdown('<h2 class="section-header">Work History</h2>', unsafe_allow_html=True)

    jobs = [
        {
            "title": "Data Quality Analyst",
            "company": "Scale AI – San Francisco, CA",
            "date": "04/2024 - Current",
            "responsibilities": [
                "Analyzed performance metrics of AI language models, focusing on code generation and problem-solving capabilities.",
                "Increased efficiency in data analysis by 40% through creation of custom Python scripts automating 15+ repetitive tasks and saving estimated 20 hours per week across team."
            ]
        },
        {
            "title": "Software Developer",
            "company": "InStack AI Solutions – Rowland Heights, CA",
            "date": "06/2022 - Current",
            "responsibilities": [
                "Engineered and deployed comprehensive learning management system utilizing Python Flask, REST APIs, PostgreSQL, and Heroku, which streamlined operational processes and improved data-driven decision-making.",
                "Innovated data visualization techniques using advanced data science libraries, achieving client metric dashboard that enhanced user experience and contributed to 90% increase in customer retention."
            ]
        },
        {
            "title": "Data Analyst",
            "company": "Robotogie LLC – Pasadena, CA",
            "date": "05/2021 - 02/2023",
            "responsibilities": [
                "Developed advanced data visualizations that uncovered hidden trends in student performance, resulting in 3 policy changes that improved overall student achievement scores by 15% within one academic year.",
                "Conducted A/B testing on new teaching methodologies, analyzing results from 250+ students, which led to the implementation of a new curriculum that boosted standardized test scores by an average of 10 percentile points."
            ]
        }
    ]

    for job in jobs:
        with st.expander(f"{job['title']} at {job['company']}"):
            st.markdown(f'<p class="highlight-text">{job["date"]}</p>', unsafe_allow_html=True)
            for responsibility in job["responsibilities"]:
                st.markdown(f'<p class="normal-text">• {responsibility}</p>', unsafe_allow_html=True)

    # Education
    st.markdown('<h2 class="section-header">Education</h2>', unsafe_allow_html=True)
    st.markdown('''
    <div class="card">
        <h3 class="sub-header">Bachelor of Arts: Information Systems and Decision Sciences</h3>
        <p class="normal-text">California State University - Fullerton, CA | 08/2021</p>
    </div>
    ''', unsafe_allow_html=True)

    # Professional Projects
    st.markdown('<h2 class="section-header">Professional Projects</h2>', unsafe_allow_html=True)

    projects = [
        {
            "name": "ExoExplorer: Machine Learning and AI-Enhanced Exoplanet Analysis",
            "details": [
                "Applied advanced machine learning techniques, specifically multi-variate regression, to analyze 4,000+ confirmed exoplanets from NASA's Exoplanet Archive.",
                "Developed a predictive model for habitability scores with 85% accuracy, utilizing 8 key habitability indicators including atmospheric composition, planetary mass, and Goldilocks zone."
            ]
        },
        {
            "name": "AI-Powered Real Estate Chatbot | A+ Realty & Mortgage Solutions",
            "details": [
                "Engineered a sophisticated AI chatbot utilizing OpenAI's API, processing over 500 unique real estate queries weekly with a 94% accuracy rate in understanding and responding to complex questions."
            ]
        },
        {
            "name": "Chiropractic Patient Management System | Body RES",
            "details": [
                "Designed a SOAP notes system handling 200+ daily entries, improving documentation efficiency from 10 minutes to 7 minutes per note (30% faster).",
                "Integrated a treatment plan tracker monitoring 15 different therapy types, boosting patient adherence from 70% to 84% (20% increase)."
            ]
        }
    ]

    for project in projects:
        with st.expander(project["name"]):
            for detail in project["details"]:
                st.markdown(f'<p class="normal-text">• {detail}</p>', unsafe_allow_html=True)

    # Career Timeline
    st.markdown('<h2 class="section-header">Career Timeline</h2>', unsafe_allow_html=True)

    timeline_items = [
        {"id": 1, "content": "Data Quality Analyst at Scale AI", "start": "2024-04-01", "end": "2024-08-31"},
        {"id": 2, "content": "Software Developer at InStack AI Solutions", "start": "2022-06-01", "end": "2024-08-31"},
        {"id": 3, "content": "Data Analyst at Robotogie LLC", "start": "2021-05-01", "end": "2023-02-28"},
        {"id": 4, "content": "Graduated from California State University - Fullerton", "start": "2021-08-01"},
    ]

    timeline = st_timeline(timeline_items, groups=[], options={
        "zoomable": False,
        "height": "300px",
        "stack": True,
        "showCurrentTime": True,
    })

    if timeline:
        st.markdown(f'<p class="highlight-text">Selected: {timeline}</p>', unsafe_allow_html=True)

    # Display details of the selected timeline item
    if timeline:
        selected_job = next((job for job in jobs if job["title"] in timeline), None)
        if selected_job:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown(f'<h3 class="sub-header">{selected_job["title"]}</h3>', unsafe_allow_html=True)
            st.markdown(f'<p class="normal-text">{selected_job["company"]}</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="highlight-text">{selected_job["date"]}</p>', unsafe_allow_html=True)
            for responsibility in selected_job["responsibilities"]:
                st.markdown(f'<p class="normal-text">• {responsibility}</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)


        # Add Download Resume button
    st.markdown('<h2 class="section-header">Download Resume</h2>', unsafe_allow_html=True)
    
    # Assuming your PDF is named 'Lannon_Khau_Resume.pdf' and is in the same directory as this script
    resume_path = os.path.join(os.path.dirname(__file__), "assets", "Lannon_Khau_Resume.pdf")
    
    with open(resume_path, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="Download Resume",
                       data=PDFbyte,
                       file_name="/assets/Lannon_Khau_Resume.pdf",
                       mime='application/octet-stream')

if __name__ == "__main__":
    st.set_page_config(page_title="Lannon Khau - Resume", layout="wide")
    display_resume()
