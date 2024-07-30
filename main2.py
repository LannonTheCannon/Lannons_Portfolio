import streamlit as st
import base64
import os

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def main():
    st.set_page_config(
        page_title="Lannon Khau - Portfolio",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': None,
            'Report a bug': None,
            'About': None
        }
    )

    # Get the path to the sidebar image
    sidebar_image_path = os.path.join(os.path.dirname(__file__), "images", "boy_and_dog.png")

    # Encode the sidebar image
    sidebar_image_base64 = get_base64_of_bin_file(sidebar_image_path)

    # Set the sidebar background
    st.markdown(
        f"""
        <style>
        [data-testid="stSidebar"] {{
            background-image: url("data:image/png;base64,{sidebar_image_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        [data-testid="stSidebar"] > div:first-child {{
            background-color: rgba(0, 0, 0, 0.3);
            box-shadow: 5px 0px 5px rgba(0,0,0,0.8); 
        }}
        [data-testid="stSidebar"] .sidebar-content {{
            color: white;
        }}
        /* Style for all text elements in the sidebar */
        [data-testid="stSidebar"] {{
            color: white !important;
        }}
        /* Style specifically for headers in the sidebar */
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] h4,
        [data-testid="stSidebar"] h5,
        [data-testid="stSidebar"] h6 {{
            color: white !important;
        }}
        /* Style for radio buttons text */
        [data-testid="stSidebar"] .stRadio label {{
            color: white !important;
        }}
        /* Additional styles for radio buttons */
        [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {{
            color: white !important;
        }}
        [data-testid="stSidebar"] .stRadio div[role="radiogroup"] div {{
            color: white !important;
        }}
        /* Force all text in sidebar to be white */
        [data-testid="stSidebar"] * {{
            color: white !important;
        }}
        /* Style for the title */
        [data-testid="stSidebar"] .sidebar-content [data-testid="stMarkdownContainer"] p {{
            color: white !important;
            font-weight: bold;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
    <style>
    .custom-container {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .row-container {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: flex-start;
    }
    .image-container {
        flex: 1;
        margin-right: 20px;
    }
    .text-container {
        flex: 2;
        font_color: black;
    }
    .custom-image {
        width: 100%;
        max-width: 285px;   
        height: auto;
    }
    .stApp {
        background: linear-gradient(to top, white, #d6ccc2, white);
    }
    </style>
    """, unsafe_allow_html=True)

    # Main portfolio sidebar
    with st.sidebar:
        st.title('Lannon Khau')

        # Profile picture
        profile_image_path = os.path.join(os.path.dirname(__file__), "images", "profile.jpg")
        profile_image_base64 = get_base64_of_bin_file(profile_image_path)
        st.markdown(f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{profile_image_base64}" 
                 style="width:200px; height:200px; border-radius:50%; object-fit:cover;">
        </div>
        """, unsafe_allow_html=True)

        sections = [
            ':house_with_garden: Home',
            ':page_with_curl: Resume',
            ':toolbox: Projects',
            ':goggles: Hobbies',
        ]

    selected_section = st.sidebar.radio('Navigation', sections)

    if selected_section == ':house_with_garden: Home':
        display_home()
    elif selected_section == ':page_with_curl: Resume':
        display_resume()
    elif selected_section == ':toolbox: Projects':
        display_projects()
    elif selected_section == ':goggles: Hobbies':
        display_hobbies()

def display_home():
    st.title('Lannon Khau')
    st.subheader('Empowering Businesses with AI-Driven Data Solutions')

    # Get the path to the image for the About Me section
    about_image_path = os.path.join(os.path.dirname(__file__), "images", "profile.jpg")

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

    # Skills
    st.header('Skills')
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Python", "95%")
    col2.metric("Streamlit", "90%")
    col3.metric("AI/ML", "85%")
    col4.metric("Data Analysis", "88%")

    # Featured Projects
    st.header('Featured Projects')
    proj1, proj2, proj3 = st.columns(3)

    # Get the path to the image for projects
    project_image_path = os.path.join(os.path.dirname(__file__), "images", "profile.jpg")
    project_image_base64 = get_base64_of_bin_file(project_image_path)

    project_image_html = f'<img src="data:image/png;base64,{project_image_base64}" style="width:100%;">'

    with proj1:
        st.markdown(project_image_html, unsafe_allow_html=True)
        st.subheader('AI Chatbot for E-commerce')
    with proj2:
        st.markdown(project_image_html, unsafe_allow_html=True)
        st.subheader('Data Visualization Dashboard')
    with proj3:
        st.markdown(project_image_html, unsafe_allow_html=True)
        st.subheader('Predictive Analytics Tool')

    # Services
    st.header('Services')
    serv1, serv2, serv3 = st.columns(3)
    serv1.write('🤖 AI Chatbot Development')
    serv2.write('📊 Data Website Creation')
    serv3.write('🐍 Python Tutoring')

    # Call to Action
    st.button('Contact Me', on_click=lambda: st.write('Contact form or details here'))

def display_resume():
    st.title('Resume')

def display_projects():
    st.title('Projects')

def display_hobbies():
    st.title('Hobbies')

if __name__ == "__main__":
    main()