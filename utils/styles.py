# styles.py
# This script gets the CSS styling and the image style
#
#######################################################################

def get_styles_main(sidebar_image_base64):
    return f"""
    <style>
    /* Sidebar background image */
    [data-testid="stSidebar"] {{
        background-image: url("data:image/png;base64,{sidebar_image_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    /* ++++++++++++++++++++++++++++ Rest of your CSS styles ++++++++++++++++++++++++++++ */
    div[data-testid="stToolbar"] {{
        background-color: white !important;
        background-image: none !important;
    }}

    /* Style for the top bar's buttons and icons */
    div[data-testid="stToolbar"] button,
    div[data-testid="stToolbar"] svg {{
        color: #d6ccc2 !important;
        fill: #d6ccc2 !important;
    }}

    /* Remove the border under the top bar */
    div[data-testid="stToolbar"]::after {{
        background-color: transparent !important;
    }}

    /* Hide default Streamlit header */
    header[data-testid="stHeader"] {{
        display: none !important;
    }}

    /* Style for the sidebar title */
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1 {{
        color: white !important;
        font-weight: bold;
        font-size: 2.0rem;
        margin-top: -5rem;
        margin-bottom: 7.5rem;
        padding-top: 0;
    }}

    /* Adjust the top padding of the sidebar content */
    [data-testid="stSidebar"] .sidebar-content {{
        padding-top: 0rem;
    }}

    [data-testid="stSidebar"] > div:first-child {{
        background-color: rgba(0, 0, 0, 0.3);
        box-shadow: 5px 0px 5px rgba(0,0,0,0.8); 
    }}

    [data-testid="stSidebar"] .sidebar-content {{
        color: white;
        padding-top: 2rem;
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
        margin-bottom: 1rem;
    }}

    /* Style for radio buttons container */
    [data-testid="stSidebar"] .stRadio {{
        margin-top: 0px;
    }}

    /* Style for radio buttons text */
    [data-testid="stSidebar"] .stRadio label {{
        color: white !important;
        width: 100%;
        text-align: center;
        padding: 0.2rem 0;
        margin: 0.1rem 0;
    }}

    /* Additional styles for radio buttons */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] {{
        margin-top: 50px;
        margin-left: 70px;
        justify-content: center; 
    }}

    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] > div {{
        margin: 0.1rem 0;
    }}

    /* Force all text in sidebar to be white */
    [data-testid="stSidebar"] * {{
        color: white !important;
    }}

    /* Style for the title */
    [data-testid="stSidebar"] .sidebar-content [data-testid="stMarkdownContainer"] p {{
        color: white !important;
        font-weight: bold;
        margin-top: 50px;
    }}

    /* Style for the main content */
    .custom-container {{
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
    }}

    .row-container {{
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: flex-start;
    }}

    .image-container {{
        flex: 1;
        margin-right: 20px;
    }}

    .text-container {{
        flex: 2;
        color: black;
    }}

    .custom-image {{
        width: 100%;
        max-width: 285px;   
        height: auto;
    }}

    .stApp {{
        background: linear-gradient(to top, #FFFAF0, #FFFAF0, #FAEBD7);
    }}
    </style>
    """

def get_profile_image_style(profile_image_base64):
    return f'''
        <div style="text-align: center;">
            <img src="data:image/png;base64,{profile_image_base64}"
                 style="width:auto; height:130px; object-fit:cover; 
                 margin-bottom: -1205px; margin-right: -15px; border-radius: 50%;">
        </div>
    '''

########### Landing Page Styling ###############

def get_styles_landing():
    return """
    <style>
    .main-header {
        font-size: 3.5rem;
        font-weight: 700;
        color: #3d405b;
        margin-top: -45px;
        margin-bottom: 0;
        text-align: center;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #3d405b;
        margin-top: 0px;
        text-align: center;
    }
    .section-header {
        font-size: 1.5rem;
        color: #3d405b;
    }
    
    .full-width-section {
        background-color: #1E1E1E;
        color: white;
        padding: 40px 0;
        margin: 40px -5rem;
    }
    .full-width-content {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }
    
    .skills-section {
        background-color: #2c3e50;
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
    
    .centered-button {
        display: flex;
        justify-content: center;
    }
    .custom-button {
        font-size: 18px;
        padding: 12px 24px;
        border-radius: 5px;
        background-color: #3498db;
        color: white;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3), 0 1px 3px rgba(0, 0, 0, 0.08);
    }
    .custom-button:hover {
        background-color: #2980b9;
        box-shadow: 0 7px 14px rgba(0, 0, 0, 0.1), 0 3px 6px rgba(0, 0, 0, 0.08);
        transform: translateY(-1px);
    }
    .custom-button:active {
        background-color: #2573a7;
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
        transform: translateY(1px);
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
        color: black;
    }
    .custom-image {
        width: 100%;
        max-width: 285px;   
        height: auto;
    }
    </style>
    """

