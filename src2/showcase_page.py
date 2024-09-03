# showcase_page.py

import streamlit as st
from datetime import datetime, timedelta
import base64
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def display_showcase():
    # Custom CSS
    st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #4b6cb7, #182848);
        color: white;
    }
    .stApp {
        background: linear-gradient(to right, #4b6cb7, #182848);
    }
    .showcase-header {
        font-size: 4rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
        color: white;
    }
    .showcase-subheader {
        font-size: 1.5rem;
        text-align: center;
        margin-bottom: 2rem;
        color: #f0f0f0;
    }
    .project-card {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .project-title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .countdown {
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        margin-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("<h1 class='showcase-header'>The Future of AI: Student Showcase 2024</h1>", unsafe_allow_html=True)
    st.markdown("<p class='showcase-subheader'>Witness the dawn of a new era in technology, crafted by the brilliant minds of tomorrow.</p>", unsafe_allow_html=True)

    lottie_url = "https://lottie.host/ff71fae2-6389-4e83-a288-e7df17008c71/cgVtQ60dJp.json"  # Space-themed animation
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st.markdown("<div class='lottie-container'>", unsafe_allow_html=True)
        st_lottie(lottie_json, speed=1, height=200, key="lottie")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("Failed to load Lottie animation.")


    # Countdown to event
    event_date = datetime(2024, 9, 9, 18, 0)  # September 9, 2024, 6:00 PM
    time_left = event_date - datetime.now()
    days, hours = time_left.days, time_left.seconds // 3600
    st.markdown(f"<p class='countdown'>Countdown: {days} days, {hours} hours</p>", unsafe_allow_html=True)

    # Featured Projects
    st.subheader("Featured Projects")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="project-card">
            <div class="project-title">AI in Agriculture</div>
            <p>."" -Shawn Zhu (9th grader)</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="project-card">
            <div class="project-title">MediAssist AI</div>
            <p>."" -Stanley Zhu (7th grader)</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="project-card">
            <div class="project-title">Ai Integration Tech</div>
            <p>"" .-Bailey Tang (10th grader)</p>
        </div>
        """, unsafe_allow_html=True)

    # What to Expect
    st.subheader("What to Expect")
    st.write("""
    - Live demonstrations of cutting-edge AI chatbots
    - Interactive web applications solving real-world problems
    - Insights into the future of technology and its impact on various industries
    - Networking opportunities with budding tech innovators and industry professionals
    """)

    # Call to Action
    st.markdown("### Join the AI Revolution!")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.button("Reserve Your Spot Now!", key="reserve_spot")

    # Testimonials
    st.subheader("What People Are Saying")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="project-card">
            "The level of innovation displayed by these students is mind-blowing. Can't wait to see what they come up with this year!"
            <br>- Tech Innovator Magazine
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="project-card">
            "Last year's showcase was a game-changer. This event is a must-attend for anyone interested in the future of technology."
            <br>- AI Weekly
        </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("Don't miss this opportunity to witness the future of AI and support the next generation of tech innovators!")

if __name__ == "__main__":
    display_showcase()
