import streamlit as st

def main():
    st.set_page_config(page_title='Lannon Khau - Portfolio', layout='wide')

    # Main portfolio sidebar
    with st.sidebar:
        st.title('Lannon Khau')
        st.image('./images/profile.jpg', width=285)

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
    st.title('Home')

def display_resume():
    st.title('Resume')

def display_projects():
    st.title('Projects')

def display_hobbies():
    st.title('Hobbies')

if __name__ == "__main__":
    main()

