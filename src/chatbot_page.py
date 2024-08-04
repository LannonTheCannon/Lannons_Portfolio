import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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
