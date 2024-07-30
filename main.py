import streamlit as st
import base64
import os


def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .profile-pic {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        background-position: center;
        width: 200px;
        height: 200px;
        border-radius: 50%%;
        margin: 0 auto;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


def main():
    st.set_page_config(page_title='Lannon Khau - Portfolio', layout='wide')

    # Get the path to the image
    image_path = os.path.join(os.path.dirname(__file__), "images", "profile.jpg")

    # Set the image as background for the profile-pic div
    set_png_as_page_bg(image_path)

    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            background-image: url('https://media.discordapp.net/attachments/1109716744978837587/1267714200621285446/wood.jpg?ex=66a9ca5a&is=66a878da&hm=d661e01658071bee5f2caf6418bf2d7ebbef8d3eeab10a0be2142750ff27fbfb&=&format=webp&width=936&height=936');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        [data-testid="stSidebar"] > div:first-child {
            background-color: rgba(0, 0, 0, 0.3);  /* Adds a dark overlay for better text visibility */
        }
        [data-testid="stSidebar"] .sidebar-content {
            color: white;  /* Makes text white for better visibility */
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
    # Custom CSS for the section box
    # Hero Section
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