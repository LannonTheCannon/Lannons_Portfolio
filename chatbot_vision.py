import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = st.secrets['OPENAI_API_KEY']

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

def get_assistant_response(user_input):
    try:
        # Append the user's message to the conversation
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Get the assistant's response
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=st.session_state.messages,
        )

        assistant_message = response.choices[0].message['content']

        # Append the assistant's response to the conversation
        st.session_state.messages.append({"role": "assistant", "content": assistant_message})

        return assistant_message
    except openai.error.OpenAIError as e:
        st.error(f"Error getting assistant response: {e}")
        return "I'm sorry, but an error occurred while processing your request."

def analyze_image(file):
    try:
        file.seek(0)
        # Send the image along with the message
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": "Please analyze the attached image.",
                    "image": file
                }
            ]
        )
        assistant_message = response.choices[0].message['content']

        # Append the assistant's response to the conversation
        st.session_state.messages.append({"role": "assistant", "content": assistant_message})

        return assistant_message
    except openai.error.OpenAIError as e:
        st.error(f"Error analyzing image: {e}")
        return "I'm sorry, but I couldn't process the image."

def get_avatar(role):
    if role == "user":
        return "https://www.themarysue.com/wp-content/uploads/2023/03/Tanjiro-Demon-Slayer.jpg"
    elif role == "assistant":
        return "https://ladygeekgirl.wordpress.com/wp-content/uploads/2015/10/mark-watney-matt-damon.jpg"
    else:
        return None  # Default to no avatar for other roles

def display_chatbot():
    st.title('Mark Watney Chatbot')

    # Display previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=get_avatar(message["role"])):
            if message.get("type") == "image":
                st.image(message["content"], caption="Uploaded Image", use_column_width=True)
            else:
                st.markdown(message["content"])

    # Input for text messages
    prompt = st.chat_input("Ask me anything!")

    if prompt:
        with st.chat_message("user", avatar=get_avatar("user")):
            st.markdown(prompt)
        assistant_response = get_assistant_response(prompt)
        with st.chat_message("assistant", avatar=get_avatar("assistant")):
            st.markdown(assistant_response)

    # File uploader for images
    uploaded_image = st.file_uploader('Upload an image for analysis', type=['png', 'jpg', 'jpeg'])
    if uploaded_image:
        # Display the uploaded image
        with st.chat_message("user", avatar=get_avatar("user")):
            st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)
        # Analyze the image
        image_analysis = analyze_image(uploaded_image)
        with st.chat_message("assistant", avatar=get_avatar("assistant")):
            st.markdown(image_analysis)

def main():
    st.set_page_config(page_title='Mark Watney Chatbot', layout='wide')
    display_chatbot()

if __name__ == '__main__':
    main()
