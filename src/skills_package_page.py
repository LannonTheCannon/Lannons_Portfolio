# skills_package_page.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

def display_syllabus():
    st.title("🚀 Comprehensive Skills Package: Journey to Tech Mastery")
    
    st.markdown("""
    Our innovative program is designed to transform high school students into tech-savvy professionals, 
    ready for the challenges of the digital age. Through four comprehensive levels, students will build 
    a robust skill set that's highly valued in today's job market.
    """)

    st.divider()

    # Improved Skill Progression Chart
    st.subheader("📈 Skill Progression Throughout the 9-Month Program")

    # Define the skills and their progression
    skills = {
        'Python': [0, 10, 25, 40, 50, 60, 65, 70, 75, 80, 82, 85],
        'Web Development': [0, 0, 5, 15, 30, 45, 60, 70, 75, 80, 85, 90],
        'Data Structuring': [0, 0, 0, 10, 15, 20, 25, 30, 40, 50, 55, 70],
        'AI Integration': [0, 0, 0, 0, 0, 0, 0, 10, 20, 30, 40, 45]
    }

    weeks = list(range(0, 37, 3))  # 0, 3, 6, ..., 33, 36
    week_labels = [f'Week {w}' for w in weeks]

    fig = go.Figure()

    for skill, progression in skills.items():
        fig.add_trace(go.Scatter(
            x=weeks, 
            y=progression,
            mode='lines+markers',
            name=skill,
            hovertemplate='Week %{x}: %{y}% proficiency'
        ))

    fig.update_layout(
        title='Skill Progression Throughout the 9-Month Program',
        xaxis_title='Program Duration',
        yaxis_title='Skill Proficiency (%)',
        xaxis=dict(tickmode='array', tickvals=weeks, ticktext=week_labels),
        yaxis=dict(range=[0, 100]),
        legend_title='Skills',
        hovermode='x unified'
    )

    st.plotly_chart(fig)

    # Add an explanation of the chart
    st.markdown("""
    **Understanding the Skill Progression:**
    - **Python**: Rapid initial growth, with steady progression throughout the program as more advanced concepts are introduced.
    - **Web Development**: Begins after initial Python fundamentals, showing quick acceleration once the basics are established.
    - **Data Analysis**: Introduced mid-program, building on Python skills and showing significant growth in later stages.
    - **AI Integration**: Introduced in the latter half of the program, demonstrating rapid growth as students apply previously learned skills.

    This chart illustrates how different skills are introduced and developed over the 36-week program, showcasing the comprehensive and well-structured nature of the curriculum.
    """)

    st.divider()

    # Detailed Level Breakdown
    st.header("🛠️ Program Levels: Your Path to Success")
    
    levels = {
        "Level 1: Foundation": {
            "Focus": "Python Fundamentals & PCEP Certification",
            "Duration": "10 weeks",
            "Key Outcomes": [
                "Master Python basics and advanced concepts",
                "Develop strong problem-solving skills",
                "Prepare for and pass the PCEP certification exam",
                "Build 3 foundational Python projects"
            ],
            "Why It Matters": "Python is the cornerstone of modern programming. This level ensures a solid foundation for all future tech endeavors."
        },
        "Level 2: Web Application Development": {
            "Focus": "Streamlit & Dynamic Web Apps",
            "Duration": "8 weeks",
            "Key Outcomes": [
                "Create interactive, data-driven web applications",
                "Master Streamlit framework for rapid prototyping",
                "Develop a personal portfolio website",
                "Learn version control with Git and GitHub"
            ],
            "Why It Matters": "Web development skills are crucial in today's digital landscape. Students will be able to bring their ideas to life on the web."
        },
        "Level 3: Data Analysis & Visualization": {
            "Focus": "Advanced Data Handling & Insights",
            "Duration": "8 weeks",
            "Key Outcomes": [
                "Manipulate and analyze complex datasets",
                "Create stunning data visualizations",
                "Develop a comprehensive data dashboard",
                "Learn statistical analysis and machine learning basics"
            ],
            "Why It Matters": "Data is the new oil. This level equips students with the skills to extract valuable insights from data, a critical skill in any industry."
        },
        "Level 4: AI Integration & Innovation": {
            "Focus": "AI Chatbots & Cutting-edge Tech",
            "Duration": "10 weeks",
            "Key Outcomes": [
                "Understand AI and machine learning fundamentals",
                "Develop and integrate AI chatbots",
                "Create a capstone project combining all learned skills",
                "Prepare for AI ethics and future tech trends"
            ],
            "Why It Matters": "AI is reshaping industries. This level prepares students to be at the forefront of technological innovation."
        }
    }

    for level, details in levels.items():
        with st.expander(level):
            st.subheader(f"Focus: {details['Focus']}")
            st.write(f"**Duration:** {details['Duration']}")
            st.write("**Key Outcomes:**")
            for outcome in details['Key Outcomes']:
                st.write(f"- {outcome}")
            st.write(f"**Why It Matters:** {details['Why It Matters']}")

    st.divider()

    # Career Prospects
    st.header("💼 Career Prospects")
    st.write("""
    Upon completion of this comprehensive program, students will be well-equipped for various high-demand tech careers, including:
    - Software Developer
    - Data Analyst
    - Web Application Developer
    - AI Specialist
    - Tech Entrepreneur
    
    Moreover, the skills acquired will give students a significant advantage in college applications and internship opportunities.
    """)

