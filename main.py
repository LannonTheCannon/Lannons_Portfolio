import streamlit as st
import base64
import os
import openai
from src2.resume_page import display_resume
from src2.project_page import display_projects
from src2.hobbies_page import display_hobbies
import time

ASSISTANT_ID = 'asst_OUgnR5TbpMHivgAvdaG28t3I'
THREAD_ID = 'thread_Ph5I8HpBIDb3rrIieBLfimlJ'
client = openai.OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

if "messages" not in st.session_state:
    st.session_state.messages = []

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background_images(profile_pic, sidebar_bg):
    profile_pic_str = get_base64_of_bin_file(profile_pic)
    sidebar_bg_str = get_base64_of_bin_file(sidebar_bg)
    
    background_images = f'''
    <style>
    .profile-pic {{
        background-image: url("data:image/png;base64,{profile_pic_str}");
        background-size: cover;
        background-position: center;
        width: 200px;
        height: 200px;
        border-radius: 50%;
        margin: 0 auto;
        box-shadow: 5px 0px 5px rgba(0,0,0,0.8); 
    }}

    [data-testid="stSidebar"] {{
        background-image: url("data:image/png;base64,{sidebar_bg_str}");
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
    [data-testid="stSidebar"] .sidebar-content h1,
    [data-testid="stSidebar"] .sidebar-content h2,
    [data-testid="stSidebar"] .sidebar-content h3 {{
        color: white;
    }}
    </style>
    '''
    st.markdown(background_images, unsafe_allow_html=True)

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

def get_current_date_info():
    current_date = datetime.datetime.now(pytz.timezone('America/Los_Angeles'))
    return {
        'current_date': current_date.strftime('%Y-%m-%d'),
        'current_day':  current_date.strftime('%A'),
        'current_time': current_date.strftime('%H:%M:%S'),
        'datetime_obj': current_date
    }

def get_assistant_response(assistant_id, thread_id, user_input):
    try:
        # Add the user's message to the thread
        client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=user_input
        )
        # Create a run
        run = client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id
        )
        # Wait for the run to complete
        while True:
            run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
            if run_status.status == 'completed':
                break
            time.sleep(1)
        # Retrieve the assistant's messages
        messages = client.beta.threads.messages.list(thread_id=thread_id)

        # Return the latest assistant message
        return messages.data[0].content[0].text.value
    except Exception as e:
        st.error(f"Error getting assistant response: {str(e)}")
        return "I'm sorry, but an error occurred while processing your request."

def display_chatbot():
    st.title('Mark Watney Chatbot')
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask me anything!")
    
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = get_assistant_response(
                ASSISTANT_ID,
                THREAD_ID,  
                prompt
            )
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

def main():
    st.set_page_config(page_title='Lannon Khau - Portfolio', layout='wide')

    # Get the path to the image
    profile_pic_path = os.path.join(os.path.dirname(__file__), "images", "profile.jpg")
    sidebar_bg_path = os.path.join(os.path.dirname(__file__), 'images', 'natural_wood.png')
    # Set the image as background for the profile-pic div
    set_background_images(profile_pic_path, sidebar_bg_path)

    st.markdown(
        """
        <style>
        /* Existing styles... */

        /* Style for radio buttons text */
        [data-testid="stSidebar"] .stRadio label {
            color: white !important;
        }

        /* Additional styles for radio buttons */
        [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
            color: white !important;
        }

        [data-testid="stSidebar"] .stRadio div[role="radiogroup"] div {
            color: white !important;
        }

        /* Force all text in sidebar to be white */
        [data-testid="stSidebar"] * {
            color: white !important;
        }
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
        st.markdown("""
        <div style="text-align: center;">
            <div class="profile-pic"></div>
        </div>
        """, unsafe_allow_html=True)

        sections = [
            ':house_with_garden: Home',
            '🤖 Lannon\'s Chatbot',
            ':page_with_curl: Resume',
            ':toolbox: Projects',
            ':goggles: Hobbies',
        ]

    selected_section = st.sidebar.radio('Navigation', sections)

    if selected_section == ':house_with_garden: Home':
        display_home()
    elif selected_section == '🤖 Lannon\'s Chatbot':
        display_chatbot() 
    elif selected_section == ':page_with_curl: Resume':
        display_resume()
    elif selected_section == ':toolbox: Projects':
        display_projects()
    elif selected_section == ':goggles: Hobbies':
        display_hobbies()

if __name__ == "__main__":
    main()
