import streamlit as st

st.markdown("""
    <style>
    .st-emotion-cache-1r4qj8v {
        color: purple !important; 
    }
    </style>
""", unsafe_allow_html=True)

with st.expander("Click me to expand"):
    st.markdown("<p style='color: red;'>This is the content inside the expander.</p>", unsafe_allow_html=True)