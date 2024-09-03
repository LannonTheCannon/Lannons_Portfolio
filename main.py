import streamlit as st
import os
import openai
from src2.home_page import display_home
from src2.resume_page2 import display_resume
from src2.project_page import display_projects
from src2.showcase_page import display_showcase
import time


ASSISTANT_ID = 'asst_OUgnR5TbpMHivgAvdaG28t3I'
THREAD_ID = 'thread_Ph5I8HpBIDb3rrIieBLfimlJ'
client = openai.OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

if "messages" not in st.session_state:
    st.session_state.messages = []

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
        background: linear-gradient(to top, #466365, #DAE3E5, #DAE3E5);
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
            ':toolbox: My Projects',
            ':goggles: Project Showcase',
        ]

    selected_section = st.sidebar.radio('Navigation', sections)

    if selected_section == ':house_with_garden: Home':
        display_home()
    elif selected_section == '🤖 Lannon\'s Chatbot':
        display_chatbot() 
    elif selected_section == ':page_with_curl: Resume':
        display_resume()
    elif selected_section == ':toolbox: My Projects':
        display_projects()
    elif selected_section == ':goggles: Project Showcase':
        display_showcase()

if __name__ == "__main__":
    main()
