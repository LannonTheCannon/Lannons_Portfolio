import streamlit as st
import base64
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def main():
    st.set_page_config(
        page_title="Your App Title",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': None,
            'Report a bug': None,
            'About': None
        }
    )

    st.markdown(
        """
        <style>
        /* Existing styles... */

        /* Style for the top bar */
        div[data-testid="stToolbar"] {
            background-color: white !important;
            background-image: none !important;
        }

        /* Style for the top bar's buttons and icons */
        div[data-testid="stToolbar"] button,
        div[data-testid="stToolbar"] svg {
            color: #d6ccc2 !important;
            fill: #d6ccc2 !important;
        }

        /* Remove the border under the top bar */
        div[data-testid="stToolbar"]::after {
            background-color: transparent !important;
        }

        /* Hide default Streamlit header */
        header[data-testid="stHeader"] {
            display: none !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Get the path to the sidebar image
    sidebar_image_path = os.path.join(os.path.dirname(__file__), "images", "boy_and_dog.png")

    # Encode the sidebar image
    sidebar_image_base64 = get_base64_of_bin_file(sidebar_image_path)

    st.markdown(
        """
        <style>
        /* Style for the sidebar title */
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1 {
            color: white !important;
            font-weight: bold;
            font-size: 2.0rem;
            margin-top: -5rem;
            margin-bottom: 7.5rem;
            padding-top: 0;
        }

        /* Adjust the top padding of the sidebar content */
        [data-testid="stSidebar"] .sidebar-content {
            padding-top: 0rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

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
            padding-top: 2rem;  /* Add some space at the top of the sidebar */
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
            margin-bottom: 1rem;  /* Add some space below headers */
        }}
        
        
        /* Style for radio buttons container */
        [data-testid="stSidebar"] .stRadio {{
            margin-top: 0px;  /* Add some space above the radio group */
            
        }}
        /* Style for radio buttons text */
        [data-testid="stSidebar"] .stRadio label {{
            color: white !important;
            width: 100%;
            text-align: center;
            padding: 0.2rem 0;  /* Add minimal vertical padding */
            margin: 0.1rem 0;  /* Add minimal vertical margin */
        }}
        /* Additional styles for radio buttons */
        [data-testid="stSidebar"] .stRadio div[role="radiogroup"] {{
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        [data-testid="stSidebar"] .stRadio div[role="radiogroup"] > div {{
            margin: 0.1rem 0;  /* Minimal space between buttons */
        }}
        /* Force all text in sidebar to be white */
        [data-testid="stSidebar"] * {{
            color: white !important;
        }}
        /* Style for the title */
        [data-testid="stSidebar"] .sidebar-content [data-testid="stMarkdownContainer"] p {{
            color: white !important;
            font-weight: bold;
            margin-bottom: 1rem;  /* Add some space below the title */
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
            background: linear-gradient(to top, #FFFAF0, #FFFAF0, #FAEBD7);
        }
        </style>
        """, unsafe_allow_html=True)

    # Main portfolio sidebar
    with st.sidebar:
        st.markdown("<h1 style='text-align: center; color: white;'>Coder's University</h1>", unsafe_allow_html=True)

        # Profile picture
        profile_image_path = os.path.join(os.path.dirname(__file__), "images", "logo2.png")
        profile_image_base64 = get_base64_of_bin_file(profile_image_path)
        st.markdown(f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{profile_image_base64}"
                 style="width:auto; height:130px; object-fit:cover; 
                 margin-bottom: -1205px; margin-right: -15px; border-radius: 50%;">
                 
        </div>
        """, unsafe_allow_html=True)

        sections = [
            'Home',
            'Ask Me Anything',
            'Course Curriculum',
            'Projects',
            'Resume',
        ]

    selected_section = st.sidebar.radio('', sections)

    if selected_section == 'Home':
        display_home()
    elif selected_section == 'Ask Me Anything':
        display_chatbot()
    elif selected_section == 'Course Curriculum':
        display_course_curriculum()
    elif selected_section == 'Projects':
        display_projects()
    elif selected_section == 'Resume':
        display_resume()


def display_home():
    # Get the path to the images
    about_image_path = os.path.join(os.path.dirname(__file__), "images", "profile.jpg")
    project_image_path = os.path.join(os.path.dirname(__file__), "images", "boy_and_dog.png")
    project_image_path1 = os.path.join(os.path.dirname(__file__), "images", "boy_and_dog.png")
    project_image_path2 = os.path.join(os.path.dirname(__file__), "images", "boy_and_dog.png")
    project_image_path3 = os.path.join(os.path.dirname(__file__), "images", "boy_and_dog.png")


    # Encode the images
    about_image_base64 = get_base64_of_bin_file(about_image_path)
    project_image_base64 = get_base64_of_bin_file(project_image_path)
    project_image_base64 = get_base64_of_bin_file(project_image_path)
    project_image_base64 = get_base64_of_bin_file(project_image_path)
    project_image_base64 = get_base64_of_bin_file(project_image_path)

    st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        color: #3d405b;
        margin-bottom: 0;
        text-align: center;  /* Center the main header */
    }
    .sub-header {
        font-size: 1.5rem;
        color: #81b29a;
        margin-top: 0;
        text-align: center;  /* Center the sub-header */
    }
    /* ... rest of your CSS ... */
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    .main-header {
        font-size: 3.5rem;
        font-weight: 700;
        color: #3d405b;
        margin-top: -150px;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #3d405b;
        margin-top: 0;
    }
    .section-header {
        font-size: 1.5rem;
        color: #3d405b;
    }
    
    .full-width-section {
        background-color: #1E1E1E;  /* Dark background color */
        color: white;
        padding: 40px 0;
        margin: 40px -5rem;  /* Negative margin to extend beyond the main content area */
    }
    .full-width-content {
        max-width: 1200px;  /* Or whatever max-width you prefer */
        margin: 0 auto;
        padding: 0 20px;
    }
    
    .skills-section {
        background-color: #2c3e50;  /* Dark gray background */
        color: white;
        padding: 40px;
        border-radius: 10px;
    }
    
    .card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }
    .skill-metric {
        text-align: center;
        padding: 10px;
    }
    .skill-metric h3 {
        margin: 0;
        color: #3d405b;
    }
    .skill-metric .value {
        font-size: 1.5rem;
        font-weight: bold;
        color: #e07a5f;
    }
    </style>
    """, unsafe_allow_html=True)

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
        background-color: #3498db;  /* Change this to match your color scheme */
        color: white;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3), 0 1px 3px rgba(0, 0, 0, 0.08);
    }
    .custom-button:hover {
        background-color: #2980b9;  /* Darker shade for hover effect */
        box-shadow: 0 7px 14px rgba(0, 0, 0, 0.1), 0 3px 6px rgba(0, 0, 0, 0.08);
        transform: translateY(-1px);
    }
    .custom-button:active {
        background-color: #2573a7;  /* Even darker shade for click effect */
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

    # About Me
    st.markdown('<h2 class="section-header"> Beyond Coding 🌠</h2>', unsafe_allow_html=True)
    about_me_html = f"""
    <div class="card">
        <div class="row-container">
            <div class="image-container">
                <img src="data:image/png;base64,{about_image_base64}" class="custom-image">
            </div>
            <div class="text-container">
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
    st.markdown("""
    <div style="background-color: #2c3e50; padding: 40px 0; margin: 40px -5rem;">
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
            <h2 style="color: white; text-align: center; margin-bottom: 30px; font-size: 2.5rem;">Skills Package 🧰</h2>
            <div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
                <div style="width: 22%; background-color: white; border-radius: 10px; padding: 20px; margin-bottom: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);">
                    <h3 style="color: #3d405b; margin: 0; font-size: 1.4rem;">Python</h3>
                    <p style="font-size: 2rem; font-weight: bold; color: #e07a5f; margin: 10px 0;">95%</p>
                    <p style="color: #3d405b; font-size: 0.9rem; margin-top: 10px;">Proficient in data analysis, web development, and automation.</p>
                </div>
                <div style="width: 22%; background-color: white; border-radius: 10px; padding: 20px; margin-bottom: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);">
                    <h3 style="color: #3d405b; margin: 0; font-size: 1.4rem;">Streamlit</h3>
                    <p style="font-size: 2rem; font-weight: bold; color: #e07a5f; margin: 10px 0;">90%</p>
                    <p style="color: #3d405b; font-size: 0.9rem; margin-top: 10px;">Expert in creating interactive web applications and dashboards.</p>
                </div>
                <div style="width: 22%; background-color: white; border-radius: 10px; padding: 20px; margin-bottom: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);">
                    <h3 style="color: #3d405b; margin: 0; font-size: 1.4rem;">AI/ML</h3>
                    <p style="font-size: 2rem; font-weight: bold; color: #e07a5f; margin: 10px 0;">85%</p>
                    <p style="color: #3d405b; font-size: 0.9rem; margin-top: 10px;">Experienced in developing and implementing machine learning models.</p>
                </div>
                <div style="width: 22%; background-color: white; border-radius: 10px; padding: 20px; margin-bottom: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);">
                    <h3 style="color: #3d405b; margin: 0; font-size: 1.4rem;">Data Analysis</h3>
                    <p style="font-size: 2rem; font-weight: bold; color: #e07a5f; margin: 10px 0;">88%</p>
                    <p style="color: #3d405b; font-size: 0.9rem; margin-top: 10px;">Skilled in data visualization, statistical analysis, and insights generation.</p>
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
            <h3>{title}</h3>
        </div>
        """, unsafe_allow_html=True)

    # Services
    st.markdown('<h2 class="section-header">Services 🛠️</h2>', unsafe_allow_html=True)
    services = ["🤖 AI Chatbot Development", "📊 Data Website Creation", "🐍 Python Tutoring"]
    service_cols = st.columns(len(services))
    for col, service in zip(service_cols, services):
        col.markdown(f"""
        <div class="card">
            <h3>{service}</h3>
        </div>
        """, unsafe_allow_html=True)


def display_chatbot():
    st.title('Ask Me Anything')

    # 1. Prepare your data
    # Assume you have a CSV file with 'question' and 'answer' columns
    data = pd.read_csv('./data/linkedin_qa_data.csv')

    # 2. Create and train a simple model
    vectorizer = TfidfVectorizer()
    question_vectors = vectorizer.fit_transform(data['question'])

    def get_response(user_input):
        user_vector = vectorizer.transform([user_input])
        similarities = cosine_similarity(user_vector, question_vectors)
        most_similar_idx = similarities.argmax()
        return data.loc[most_similar_idx, 'answer']

    # 3. Create Streamlit interface
    st.title("Your Chatbot")

    # Initialize chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is your question?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = get_response(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

def display_course_curriculum():
    st.title('Course Curriculum')

def display_projects():
    st.title('Projects')

def display_resume():
    st.title('Resume')


if __name__ == "__main__":
    main()