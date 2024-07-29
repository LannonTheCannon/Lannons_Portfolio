# Entry Point

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Page configuration
st.set_page_config(page_title="Lannon Khau - Python Developer & AI Integrator", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .main-header {font-size:60px; font-weight:bold; color:#3498db;}
    .sub-header {font-size:30px; color:#34495e;}
    .section-header {font-size:24px; font-weight:bold; color:#2c3e50; margin-top:30px;}
    .project-card {background-color:#f8f9fa; border-radius:10px; padding:20px; margin-bottom:20px;}
    .skill-chip {background-color:#3498db; color:white; padding:5px 10px; border-radius:15px; display:inline-block; margin:5px;}
</style>
""", unsafe_allow_html=True)

# Main Header
st.markdown("<h1 class='main-header'>Lannon Khau</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Python Developer | AI Integrator | Streamlit Enthusiast | PCEP Trainer</p>", unsafe_allow_html=True)

# About Me
st.markdown("## About Me")
col1, col2 = st.columns([1, 2])
with col1:
    st.image("./images/profile.jpg", width=250)
with col2:
    st.markdown("""
    Hey! Lannon Khau here.

    Imagine this: Carving down a snowy slope, wind rushing past, adrenaline pumping. That's my happy place. 
    But you know what else gets me just as excited? Diving into a great book or having a mind-bending chat about AI. 
    I'm that guy who geeks out over chatbots one minute and plans wilderness adventures the next.

    People are my jam. I love connecting, hearing stories, and sharing laughs. There's nothing quite like making 
    a real connection, you know?

    When I'm not exploring trails or journaling, I'm probably tinkering with some new idea. I'm all about creating – 
    not just physical stuff, but experiences, solutions, memories. Life's all about what you make of it, right?

    I've got this knack for seeing potential in things. Give me a tricky situation, and I'll find a way to turn it 
    into something awesome. It's like I've got this mental snowboard, always looking for fresh ways to carve through 
    life's challenges.

    My Professional Side:
    - Python Developer & AI Enthusiast
    - Web Application Creator
    - PCEP Trainer
    - Problem Solver & Innovator

    So hey, if you're up for swapping stories, brainstorming the next big thing in tech, or just hanging out, 
    give me a shout. I'm always down for a good chat or a new adventure. Let's see what cool stuff we can cook up together!
    """)

# Skills
st.markdown("## Skills")
skills = [
    ("Python", 0.9), ("Streamlit", 0.85), ("Web Development", 0.8),
    ("AI/ML Integration", 0.75), ("Database Management", 0.8),
    ("API Development", 0.85), ("Data Visualization", 0.8),
    ("PCEP Training", 0.9)
]

fig = go.Figure([go.Bar(
    x=[skill[1] for skill in skills],
    y=[skill[0] for skill in skills],
    orientation='h'
)])
fig.update_layout(title="Skills Proficiency", xaxis_title="Proficiency", yaxis_title="Skill")
st.plotly_chart(fig)

# Featured Projects
st.markdown("## Featured Projects")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='project-card'>
        <h3>Body Res - Chiropractic Management System</h3>
        <p>A comprehensive patient management system for chiropractors. Features include SOAP notes, 
        treatment plans, and progress tracking with interactive visualizations.</p>
        <p><strong>Technologies:</strong> Python, Streamlit, SQLite, Plotly</p>
        <a href='#'>View Project</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='project-card'>
        <h3>AI-Powered Customer Service Bot</h3>
        <p>An intelligent chatbot integrated into a client's e-commerce platform. It handles customer 
        queries, processes orders, and provides personalized product recommendations.</p>
        <p><strong>Technologies:</strong> Python, TensorFlow, Flask, SQLAlchemy</p>
        <a href='#'>View Project</a>
    </div>
    """, unsafe_allow_html=True)

# PCEP Certification Training
st.markdown("## PCEP Certification Training")
st.write("""
I offer comprehensive training programs to help aspiring Python developers prepare for their PCEP 
(Certified Entry-Level Python Programmer) certification. My courses cover:

- Basic Concepts (Data Types, Variables, Operators)
- Flow Control (Conditional Blocks, Loops)
- Data Collections (Lists, Tuples, Dictionaries)
- Functions and Exceptions
- Hands-on coding exercises and mock exams
""")

# Interactive Demo
st.markdown("## Interactive Python Demo")
st.write("Try out this simple Python code snippet:")

code = st.text_area("Python Code",
"""
def greet(name):
    return f"Hello, {name}! Welcome to my portfolio."

name = "User"
greeting = greet(name)
print(greeting)
""")

if st.button("Run Code"):
    try:
        exec(code)
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Contact Form
st.markdown("## Let's Connect!")
st.write("Interested in working together or learning more about my projects? Get in touch!")

contact_form = """
<form action="https://formsubmit.co/YOUR_EMAIL@EXAMPLE.COM" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here"></textarea>
    <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("© 2024 Lannon Khau. All rights reserved.")