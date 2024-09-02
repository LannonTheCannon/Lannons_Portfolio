import streamlit as st
import base64
import os
import openai
from src2.resume_page2 import display_resume
from src2.project_page import display_projects
from src2.showcase_page import display_showcase
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

    # Skills and Technologies
    st.header('Skills & Technologies')
    
    skills = [
        {
            "category": "Programming Languages",
            "items": [
                {"name": "Python", "details": "4 years experience, expert in data analysis, web dev, and AI"},
                {"name": "SQL", "details": "3 years experience, proficient in complex queries and database design"},
                {"name": "JavaScript", "details": "2 years experience, used in web development projects"}
            ]
        },
        {
            "category": "Frameworks & Libraries",
            "items": [
                {"name": "Streamlit", "details": "Created 10+ data apps, including this portfolio"},
                {"name": "TensorFlow", "details": "Implemented in 5 machine learning projects"},
                {"name": "Pandas", "details": "Used extensively in data analysis and cleaning"}
            ]
        },
        {
            "category": "Tools & Technologies",
            "items": [
                {"name": "Git", "details": "Daily use for version control and collaboration"},
                {"name": "Docker", "details": "Used for containerizing and deploying applications"},
                {"name": "AWS", "details": "Experience with EC2, S3, and Lambda services"}
            ]
        }
    ]

    # Custom CSS for skills section
    st.markdown("""
    <style>
    .skill-category {
        font-size: 20px;
        font-weight: bold;
        margin-top: 0px;
        margin-bottom: 10px;
    }
    .skill-item {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .skill-name {
        font-weight: bold;
        font-size: 16px;
    }
    .skill-details {
        font-size: 16px;
        color: #555;
        margin-top: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Display skills
    for category in skills:
        st.markdown(f"<div class='skill-category'>{category['category']}</div>", unsafe_allow_html=True)
        for item in category['items']:
            st.markdown(f"""
            <div class="skill-item">
                <div class="skill-name">{item['name']}</div>
                <div class="skill-details">{item['details']}</div>
            </div>
            """, unsafe_allow_html=True)


    # Featured Projects
    st.header('Featured Projects')

    projects = [
        {
            "title": "NASA Exoplanet Archive",
            "image": "Exoplanets.jpg",
            "description": "Analysis and visualization of exoplanet data from NASA's archive, providing insights into planetary systems beyond our solar system.",
            "tech_stack": ["Python", "Pandas", "Matplotlib", "Streamlit"]
        },
        {
            "title": "Real Estate AI Integration",
            "image": "Real_Estate.png",
            "description": "AI-powered platform for real estate market analysis, predicting property values and identifying investment opportunities.",
            "tech_stack": ["TensorFlow", "Scikit-learn", "React", "Node.js"]
        },
        {
            "title": "Medical AI Diagnostics",
            "image": "Health_AI.jpg",
            "description": "Machine learning model for early detection of diseases using medical imaging, improving diagnostic accuracy and speed.",
            "tech_stack": ["PyTorch", "OpenCV", "Flask", "Docker"]
        }
    ]

    # Custom CSS for project section
    st.markdown("""
    <style>
    .project-card {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        height: 100%;
    }
    .project-image {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .project-title {
        font-weight: bold;
        font-size: 18px;
        margin-bottom: 10px;
    }
    .project-description {
        font-size: 16px;
        color: #555;
        margin-bottom: 10px;
    }
    .project-tech {
        font-size: 16px;
        color: #888;
    }
    .tech-tag {
        background-color: #e0e0e0;
        padding: 3px 7px;
        border-radius: 3px;
        margin-right: 5px;
        display: inline-block;
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Display projects side by side
    cols = st.columns(3)
    for idx, project in enumerate(projects):
        with cols[idx]:
            image_path = os.path.join(os.path.dirname(__file__), "images", project["image"])
            image_base64 = get_base64_of_bin_file(image_path)
            
            st.markdown(f"""
            <div class="project-card">
                <img src="data:image/png;base64,{image_base64}" class="project-image">
                <div class="project-title">{project['title']}</div>
                <div class="project-description">{project['description']}</div>
                <div class="project-tech">
                    {"".join(f'<span class="tech-tag">{tech}</span>' for tech in project['tech_stack'])}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Services
    st.header('Services')
    
    services = [
        {
            "name": "AI Chatbot Development",
            "icon": "🤖",
            "description": "Custom AI chatbot solutions for businesses, integrating natural language processing and machine learning for enhanced customer interactions.",
            "key_points": [
                "Tailored chatbot development using state-of-the-art AI technologies",
                "Integration with existing business systems and workflows",
                "Continuous improvement and learning capabilities"
            ]
        },
        {
            "name": "Data Website Creation",
            "icon": "📊",
            "description": "Developing interactive, data-driven websites and dashboards using Streamlit and other modern web technologies.",
            "key_points": [
                "Custom data visualization and interactive elements",
                "Real-time data processing and display",
                "User-friendly interfaces for complex data analysis"
            ]
        },
        {
            "name": "Python Skills Development",
            "icon": "🐍",
            "description": "Comprehensive Python training programs for individuals and teams, focusing on practical applications in data science and AI.",
            "key_points": [
                "Customized curriculum based on skill level and goals",
                "Hands-on projects and real-world problem solving",
                "Preparation for Python certification exams (e.g., PCEP)"
            ]
        }
    ]

    # Custom CSS for services section
    st.markdown("""
    <style>
    .service-container {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .service-header {
        display: flex;
        align-items: center;
        margin-bottom: 10px;
    }
    .service-icon {
        font-size: 24px;
        margin-right: 10px;
    }
    .service-name {
        font-weight: bold;
        font-size: 18px;
    }
    .service-description {
        font-size: 16px;
        color: #555;
        margin-bottom: 10px;
    }
    .service-key-points {
        font-size: 14px;
        margin-left: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Display services
    for service in services:
        st.markdown(f"""
        <div class="service-container">
            <div class="service-header">
                <span class="service-icon">{service['icon']}</span>
                <span class="service-name">{service['name']}</span>
            </div>
            <div class="service-description">{service['description']}</div>
            <ul class="service-key-points">
                {"".join(f"<li>{point}</li>" for point in service['key_points'])}
            </ul>
        </div>
        """, unsafe_allow_html=True)

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
