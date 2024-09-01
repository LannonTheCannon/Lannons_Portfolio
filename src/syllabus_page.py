import streamlit as st
import plotly.graph_objects as go
from streamlit_timeline import st_timeline
from datetime import datetime, timedelta

def display_syllabus():
    st.title("🚀 Your Journey to Tech Mastery")
    st.markdown("### 36-Week Comprehensive Curriculum")

    # Allow user to input start date
    default_start_date = datetime(2024, 8, 13)
    start_date = st.date_input("Select your program start date:", default_start_date)

    # Set the start date to August 13, 2024
    start_date = datetime.combine(start_date, datetime.min.time())

    # Create a timeline of the course
    timeline_items = [
        {"id": 1, "content": "Python Fundamentals", "start": start_date.strftime("%Y-%m-%d"), "end": (start_date + timedelta(weeks=10)).strftime("%Y-%m-%d")},
        {"id": 2, "content": "PCEP Exam Prep", "start": (start_date + timedelta(weeks=8)).strftime("%Y-%m-%d"), "end": (start_date + timedelta(weeks=10)).strftime("%Y-%m-%d")},
        {"id": 3, "content": "Web Development Basics", "start": (start_date + timedelta(weeks=10)).strftime("%Y-%m-%d"), "end": (start_date + timedelta(weeks=14)).strftime("%Y-%m-%d")},
        {"id": 4, "content": "Advanced Web Development", "start": (start_date + timedelta(weeks=14)).strftime("%Y-%m-%d"), "end": (start_date + timedelta(weeks=18)).strftime("%Y-%m-%d")},
        {"id": 5, "content": "Data Structuring Fundamentals", "start": (start_date + timedelta(weeks=11)).strftime("%Y-%m-%d"), "end": (start_date + timedelta(weeks=18)).strftime("%Y-%m-%d")},
        {"id": 6, "content": "Advanced Python & Data Structures", "start": (start_date + timedelta(weeks=18)).strftime("%Y-%m-%d"), "end": (start_date + timedelta(weeks=27)).strftime("%Y-%m-%d")},
        {"id": 7, "content": "Advanced Data Structuring", "start": (start_date + timedelta(weeks=18)).strftime("%Y-%m-%d"), "end": (start_date + timedelta(weeks=27)).strftime("%Y-%m-%d")},
        {"id": 8, "content": "Web App Integration", "start": (start_date + timedelta(weeks=18)).strftime("%Y-%m-%d"), "end": (start_date + timedelta(weeks=27)).strftime("%Y-%m-%d")},
        {"id": 9, "content": "AI Fundamentals", "start": (start_date + timedelta(weeks=24)).strftime("%Y-%m-%d"), "end": (start_date + timedelta(weeks=30)).strftime("%Y-%m-%d")},
        {"id": 10, "content": "Advanced AI & Integration", "start": (start_date + timedelta(weeks=30)).strftime("%Y-%m-%d"), "end": (start_date + timedelta(weeks=36)).strftime("%Y-%m-%d")},
        {"id": 11, "content": "Final Projects & Integration", "start": (start_date + timedelta(weeks=33)).strftime("%Y-%m-%d"), "end": (start_date + timedelta(weeks=36)).strftime("%Y-%m-%d")}
    ]

    options = {
        "zoomable": True,
        "moveable": True,
        "tooltip": {
            "followMouse": True,
            "overflowMethod": "cap"
        }
    }

    timeline = st_timeline(timeline_items, groups=[], options=options, height="400px")
    
    st.subheader("Selected Course Module")
    st.write(timeline)

    # Calculate end date
    end_date = start_date + timedelta(weeks=36)
    # Program Timeline Overview explanation
    st.markdown("""
    ### Program Timeline Overview

    - **Weeks 1-10**: Focus on Python fundamentals, culminating in PCEP exam preparation.
    - **Weeks 11-18**: Introduction to Web Development and basic Data Structuring.
    - **Weeks 19-27**: Advanced Python, Data Structuring, and Web Application integration.
    - **Weeks 25-36**: Introduction and progression of AI skills, alongside continued development of other skills.
    - **Weeks 34-36**: Final projects integrating all learned skills.

    This timeline illustrates how skills are introduced and developed throughout the program, with each new concept building upon previously learned skills.
    """)

    # Course overview metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Duration", "36 Weeks")
    col2.metric("Projects", "4+")
    col3.metric("Skills Covered", "20+")
    col4.metric("Certifications", "2")

    # Module progression chart
    modules = ['Python', 'Web Dev', 'Data Analysis', 'AI']
    proficiency = [85, 90, 80, 75]
    
    fig = go.Figure(go.Bar(
        x=modules,
        y=proficiency,
        marker_color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'],
        text=proficiency,
        textposition='auto',
    ))
    fig.update_layout(
        title='Skill Proficiency by End of Each Module',
        yaxis_title='Proficiency (%)',
        height=400
    )
    st.plotly_chart(fig)

    # Detailed syllabus
    st.header("📚 Detailed Course Structure")
    syllabus = {
        "Module 1: Python Fundamentals (Weeks 1-10)": [
            {"week": 1, "topic": "Introduction to Programming & Python Basics", "description": "Set up development environment, learn basic syntax, variables, and data types."},
            {"week": 2, "topic": "Control Structures & Functions", "description": "Master if-statements, loops, and create reusable code with functions."},
            {"week": 3, "topic": "Data Structures: Lists & Dictionaries", "description": "Work with complex data using Python's built-in data structures."},
            {"week": 4, "topic": "File I/O & Exception Handling", "description": "Read/write files and handle errors gracefully in your programs."},
            {"week": 5, "topic": "Object-Oriented Programming I", "description": "Understand classes, objects, and basic OOP principles."},
            {"week": 6, "topic": "Object-Oriented Programming II", "description": "Explore inheritance, polymorphism, and advanced OOP concepts."},
            {"week": 7, "topic": "Modules & Packages", "description": "Organize code efficiently and use Python's extensive standard library."},
            {"week": 8, "topic": "Introduction to Algorithms", "description": "Learn basic sorting and searching algorithms."},
            {"week": 9, "topic": "Python for Data Science: NumPy & Pandas Basics", "description": "Introduction to scientific computing and data manipulation with Python."},
            {"week": 10, "topic": "PCEP Exam Preparation & Project Week", "description": "Review key concepts and work on a capstone project to solidify Python skills."},
        ],
        "Module 2: Web Development with Streamlit (Weeks 11-18)": [
            {"week": 11, "topic": "Introduction to Web Development & Streamlit", "description": "Understand web basics and set up your first Streamlit app."},
            {"week": 12, "topic": "Streamlit Components & Layouts", "description": "Learn to create interactive web elements and structure your app."},
            {"week": 13, "topic": "Data Visualization with Streamlit", "description": "Integrate charts and graphs into your web applications."},
            {"week": 14, "topic": "Building Interactive Dashboards", "description": "Create dynamic, user-responsive dashboards."},
            {"week": 15, "topic": "Database Integration", "description": "Connect your Streamlit app to databases for data persistence."},
            {"week": 16, "topic": "Authentication & User Management", "description": "Implement user login and manage user sessions in your app."},
            {"week": 17, "topic": "Deployment & Cloud Hosting", "description": "Learn to deploy your Streamlit app to cloud platforms."},
            {"week": 18, "topic": "Web Development Project Week", "description": "Apply your skills to create a fully functional web application."},
        ],
        "Module 3: Data Analysis & Visualization (Weeks 19-27)": [
            {"week": 19, "topic": "Advanced Python for Data Analysis", "description": "Deepen your Python skills with a focus on data manipulation."},
            {"week": 20, "topic": "Data Cleaning & Preprocessing", "description": "Learn techniques to clean and prepare data for analysis."},
            {"week": 21, "topic": "Exploratory Data Analysis", "description": "Discover patterns and insights in data using statistical methods."},
            {"week": 22, "topic": "Data Visualization with Matplotlib & Seaborn", "description": "Create impactful visualizations to communicate data insights."},
            {"week": 23, "topic": "Introduction to Machine Learning", "description": "Understand basic ML concepts and implement simple models."},
            {"week": 24, "topic": "Supervised Learning: Regression & Classification", "description": "Apply ML algorithms to predict outcomes and classify data."},
            {"week": 25, "topic": "Unsupervised Learning: Clustering & Dimensionality Reduction", "description": "Explore patterns in data without predefined categories."},
            {"week": 26, "topic": "Time Series Analysis", "description": "Analyze and forecast time-dependent data."},
            {"week": 27, "topic": "Data Analysis Project Week", "description": "Work on a comprehensive data analysis project using real-world datasets."},
        ],
        "Module 4: AI Integration & Advanced Topics (Weeks 28-36)": [
            {"week": 28, "topic": "Introduction to Natural Language Processing", "description": "Learn the basics of processing and analyzing text data."},
            {"week": 29, "topic": "Building Chatbots with Python", "description": "Develop a simple chatbot using NLP techniques."},
            {"week": 30, "topic": "Advanced NLP: Sentiment Analysis & Named Entity Recognition", "description": "Apply advanced NLP techniques to extract insights from text."},
            {"week": 31, "topic": "Introduction to Neural Networks", "description": "Understand the fundamentals of deep learning."},
            {"week": 32, "topic": "Convolutional Neural Networks for Image Processing", "description": "Apply deep learning to image classification tasks."},
            {"week": 33, "topic": "Recurrent Neural Networks for Sequence Data", "description": "Work with time-series and text data using RNNs."},
            {"week": 34, "topic": "Generative AI & Transformers", "description": "Explore cutting-edge AI models like GPT for text generation."},
            {"week": 35, "topic": "AI Ethics & Responsible AI Development", "description": "Understand the ethical implications of AI and best practices for responsible development."},
            {"week": 36, "topic": "Final Capstone Project", "description": "Integrate all learned skills into a comprehensive AI-driven application."},
        ]
    }

    for module, weeks in syllabus.items():
        with st.expander(module):
            for week in weeks:
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.markdown(f"**Week {week['week']}**")
                with col2:
                    st.markdown(f"**{week['topic']}**")
                    st.write(week['description'])
                st.markdown("---")

    # Key learning outcomes
    st.header("🎯 Key Learning Outcomes")
    outcomes = [
        "Master Python programming and earn PCEP certification",
        "Build and deploy interactive web applications",
        "Conduct advanced data analysis and create insightful visualizations",
        "Develop AI-powered applications and chatbots"
    ]
    for outcome in outcomes:
        st.markdown(f"- {outcome}")

    # Call to action
    st.header("🌟 Ready to Start Your Tech Journey?")
    if st.button("Enroll Now"):
        st.success("Thanks for your interest! We'll contact you with enrollment details.")

    # Footer note
    st.info("""
    💡 **Note:** This curriculum is designed to provide a comprehensive journey from programming basics to advanced AI applications. 
    Topics may be adjusted based on industry trends and emerging technologies.
    """)

# Make sure to install streamlit-timeline: pip install streamlit-timeline
