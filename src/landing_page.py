# landing_page.py
import streamlit as st
import plotly.graph_objects as go

def display_home():
    st.title("🚀 Welcome to Coder's University")
    
    st.markdown("""
    Embark on a transformative journey into the world of technology with Coder's University. 
    Our comprehensive 9-month program is designed to turn high school students into skilled tech professionals, 
    ready to shape the digital future.
    """)

    st.divider()

    # Program Highlights
    st.header("🌟 Program Highlights")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(label="Program Duration", value="9 Months")
    with col2:
        st.metric(label="Total Projects", value="12+")
    with col3:
        st.metric(label="Topics Covered", value="22+")
    with col4:
        st.metric(label="Professional Certification", value="1")

    st.divider()

    # Quick Overview of Skills
    st.header("🛠️ Core Competencies & Their Professional Applications")

    skills = {
        "Python Programming": {
            "icon": "💻",
            "applications": [
                "Software Engineering: Master Python fundamentals and prepare for the PCEP certification.",
                "Application Development: Design and build robust desktop applications.",
                "Process Automation: Develop scripts to streamline repetitive tasks and increase efficiency."
            ],
            "future_benefit": "A versatile foundation for diverse tech careers and advanced academic pursuits in computer science and beyond."
        },
        "Web Development": {
            "icon": "🌐",
            "applications": [
                "Interactive Web Design: Create engaging, user-centric websites with modern frameworks.",
                "Full-Stack Development: Construct scalable, multi-page web applications.",
                "Digital Portfolio Creation: Craft a compelling online presence to showcase your skills and projects."
            ],
            "future_benefit": "Essential skills for tech entrepreneurship, digital marketing, and modern business operations across industries."
        },
        "Data Analysis": {
            "icon": "📊",
            "applications": [
                "Data Acquisition: Extract and compile data from authoritative sources like data.gov and Kaggle.",
                "Data Transformation: Convert raw data into structured, analysis-ready formats using industry-standard tools.",
                "Data Visualization: Develop interactive dashboards to communicate insights effectively."
            ],
            "future_benefit": "Crucial for data-driven decision-making in business, research, and policy-making roles."
        },
        "AI Integration": {
            "icon": "🤖",
            "applications": [
                "Conversational AI: Develop and deploy intelligent chatbots for various applications.",
                "Recommendation Systems: Implement machine learning algorithms to create personalized user experiences.",
                "Predictive Modeling: Apply AI techniques to forecast trends and outcomes in diverse fields."
            ],
            "future_benefit": "Cutting-edge expertise for driving innovation and solving complex problems across multiple industries."
        }
    }

    for skill, details in skills.items():
        with st.expander(f"{details['icon']} {skill}"):
            st.write(f"**Real-World Applications:**")
            for app in details['applications']:
                st.write(f"- {app}")
            st.write(f"**Future Benefit:** {details['future_benefit']}")

    st.info("""
    💡 **Why These Skills Matter:** 
    Our curriculum is designed to equip students with versatile, in-demand skills that open doors to numerous career paths and academic opportunities. These skills not only prepare students for the tech industry but also enhance their problem-solving abilities and analytical thinking, which are valuable in any field.
    """)

    st.divider()

    # Program Structure
    st.header("📚 Program Structure")
    st.write("Our curriculum is divided into four comprehensive levels:")
    
    levels = {
        "Level 1: Foundation": "Master Python fundamentals and earn PCEP certification",
        "Level 2: Web Development": "Create dynamic web applications with Streamlit",
        "Level 3: Data Analysis": "Harness the power of data with advanced visualization",
        "Level 4: AI Integration": "Develop and integrate AI chatbots for real-world applications"
    }

    #st.divider()
    
    for level, description in levels.items():
        st.markdown(f"**{level}:** {description}")

    st.divider()


    # Why Choose Us
    st.header("🏆 Why Choose Coder's University?")
    st.markdown("""
    - 🎓 **Industry-Aligned Curriculum**: Our program is designed to meet current industry demands.
    - 💼 **Career-Ready Skills**: Gain practical experience with tools used by leading tech companies.
    - 🚀 **Project-Based Learning**: Build a impressive portfolio showcasing your skills.
    - 👥 **Expert Mentorship**: Learn from experienced professionals in the field.
    - 🌐 **Networking Opportunities**: Connect with peers and industry leaders.
    """)

    st.divider()

    # Testimonial
    st.header("💬 Student Success Story")
    st.markdown("""
    <div style="background-color: #f0f2f6; border-left: 5px solid #4CAF50; padding: 10px;">
        <p style="color: black; margin-bottom: 5px;">
        "Coder's University transformed my future. I went from knowing little about programming to building my own AI-powered web apps. Now, I'm confidently pursuing a tech major in college!"
        </p>
        <p style="color: #555; font-style: italic; margin-top: 0;">
        - Sarah, Recent Graduate
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Call to Action
    st.header("🌟 Ready to Start Your Tech Journey?")
    st.write("Join Coder's University and set yourself on the path to tech success!")
    if st.button("Enroll Now"):
        st.success("Thank you for your interest! Our team will contact you shortly with enrollment details.")

if __name__ == "__main__":
    display_home()
