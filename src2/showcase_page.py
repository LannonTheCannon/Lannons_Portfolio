import streamlit as st
from datetime import datetime, timedelta
import base64
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url: str):
    r = requests.get(url, timeout=60)
    if r.status_code != 200:
        return None
    return r.json()

def display_contact_info():
    if 'show_contact' not in st.session_state:
        st.session_state.show_contact = False
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button('Contact Me', key='contact_button'):
            st.session_state.show_contact = not st.session_state.show_contact

    if st.session_state.show_contact:
        st.markdown("""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; margin-top: 20px; color: #333;">
            <h3 style="color: #182848;">Contact Information</h3>
            <p><strong>Email:</strong> khaulannon@instack.live</p>
            <p><strong>Phone:</strong> (626) 977-3921</p>
            <p><strong>GitHub:</strong> <a href="https://github.com/LannonTheCannon" target="_blank" style="color: #4b6cb7;">https://github.com/LannonTheCannon</a></p>
        </div>
        """, unsafe_allow_html=True)

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def display_showcase():
    # Custom CSS
    st.markdown("""
    <style>
    .main, .stApp {
        background: linear-gradient(to right, #4b6cb7, #182848);
        color: white;
    }
    .showcase-header {
        font-size: 3.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1.5rem;
        color: white;
    }
    .showcase-subheader {
        font-size: 1.3rem;
        text-align: center;
        margin-bottom: 1.5rem;
        color: #f0f0f0;
    }
    .project-card {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        transition: transform 0.3s ease-in-out;
    }
    .project-card:hover {
        transform: scale(1.05);
    }
    .project-title {
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .countdown {
        font-size: 3.5rem;
        font-weight: bold;
        text-align: center;
        margin-top: 2rem;
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .subheader {
        color: white;
        font-size: 2rem;
        font-weight: bold;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .stButton > button {
        background-color: #4ECDC4;
        color: #182848;
        font-weight: bold;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease-in-out;
        display: block;
        margin: 0 auto;
    }
    .stButton > button:hover {
        background-color: #45B7AA;
    }
    .lottie-container {
        background-color: transparent !important;
    }
    .stLottie {
        background-color: transparent !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("<h1 class='showcase-header'>AI Innovation: Student Showcase 2024</h1>", unsafe_allow_html=True)
    st.markdown("<p class='showcase-subheader'>Discover groundbreaking AI projects crafted by tomorrow's tech leaders.</p>", unsafe_allow_html=True)

    # Lottie Animation
    lottie_url = "https://lottie.host/ff71fae2-6389-4e83-a288-e7df17008c71/cgVtQ60dJp.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st.markdown("<div class='lottie-container'>", unsafe_allow_html=True)
        st_lottie(
            lottie_json,
            speed=1,
            reverse=False,
            loop=True,
            quality="low",
            height=200,
            width=None,
            key="lottie"
        )
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("Failed to load Lottie animation.")

    # Countdown to event
    event_date = datetime(2024, 9, 9, 18, 0)
    time_left = event_date - datetime.now()
    days, hours, minutes, seconds = time_left.days, time_left.seconds // 3600, (time_left.seconds // 60) % 60, time_left.seconds % 60
    st.markdown(f"<p class='countdown'>Countdown: {days}d {hours}h {minutes}m</p>", unsafe_allow_html=True)

    # Featured Projects
    st.markdown("<h2 class='subheader'>Featured Projects</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="project-card">
            <div class="project-title">EcoFarm AI</div>
            <p>"Revolutionizing agriculture with AI-driven crop optimization and resource management." -Shawn Zhu (9th grade)</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="project-card">
            <div class="project-title">HealthMate AI</div>
            <p>"An AI-powered personal health assistant for early disease detection and lifestyle recommendations." -Stanley Zhu (7th grade)</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="project-card">
            <div class="project-title">EduTech AI</div>
            <p>"Personalizing education through AI-adaptive learning platforms and virtual tutors." -Bailey Tang (10th grade)</p>
        </div>
        """, unsafe_allow_html=True)

    # What to Expect
    st.markdown("<h2 class='subheader'>What to Expect</h2>", unsafe_allow_html=True)
    st.write("""
    - Hands-on demos of student-developed AI applications
    - Interactive workshops on emerging AI technologies
    - Panel discussions on AI ethics and societal impact
    - Networking sessions with industry professionals and academic experts
    """)

    # Call to Action
    st.markdown("<h2 class='subheader'>Be Part of the AI Revolution!</h2>", unsafe_allow_html=True)
    display_contact_info()

    # Testimonials
    st.markdown("<h2 class='subheader'>What People Are Saying</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="project-card">
            "The creativity and technical prowess of these young innovators never cease to amaze. A glimpse into the future of AI!"
            <br>- Tech Innovator Magazine
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="project-card">
            "An inspiring showcase of young talent pushing the boundaries of AI. A must-attend event for anyone interested in the future of technology."
            <br>- AI Weekly
        </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("Join us in celebrating the next generation of AI innovators and exploring the transformative power of technology!")

if __name__ == "__main__":
    display_showcase()
