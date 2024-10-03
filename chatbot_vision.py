from streamlit as st
import os
import openai
import time
import base64

ASSISTANT_ID = 'asst_OUgnR5TbpMHivgAvdaG28t3I'
THREAD_ID = 'thread_Ph5I8HpBIDb3rrIieBLfimlJ'
client = openai.OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

if "messages" not in st.session_state:
    st.session_state.messages = []


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
        with st.chat_message(message["role"], avatar=get_avatar(message["role"])):
            st.markdown(message["content"])
    prompt = st.chat_input("Ask me anything!")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar=get_avatar("user")):
            st.markdown(prompt)
        with st.chat_message("assistant", avatar=get_avatar("assistant")):
            message_placeholder = st.empty()
            full_response = get_assistant_response(
                ASSISTANT_ID,
                THREAD_ID,
                prompt
            )
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})


def display_chatbot():
    st.title('Mark Watney Chatbot')

    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=get_avatar(message["role"])):
            st.markdown(message["content"])
    prompt = st.chat_input("Ask me anything!")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar=get_avatar("user")):
            st.markdown(prompt)
        with st.chat_message("assistant", avatar=get_avatar("assistant")):
            message_placeholder = st.empty()
            full_response = get_assistant_response(
                ASSISTANT_ID,
                THREAD_ID,
                prompt
            )
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

def get_avatar(role):
    if role == "user":
        return "https://www.themarysue.com/wp-content/uploads/2023/03/Tanjiro-Demon-Slayer.jpg"
    elif role == "assistant":
        return "https://ladygeekgirl.wordpress.com/wp-content/uploads/2015/10/mark-watney-matt-damon.jpg"
    else:
        return None  # Default to no avatar for other roles

def main():
    st.set_page_config(page_title='Lannon Khau - Portfolio', layout='wide')
    st.display_chatbot()

if __name__ == '__main__':
    main() 

