import google.generativeai as genai
import streamlit as st

# Set up the Streamlit app
st.title("Gemini Chatbot Clone")

# Initialize the Google Gemini client
genai.configure(api_key=st.secrets["AIzaSyA16M5z1kV3sLdqeNETvTzZyt3BJmrvvcY"])

# Select the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Maintain chat history in Streamlit session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "model", "content": "Hello! I'm your AI assistant. How can I help you today?"}
    ]

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field for user to send a message
if prompt := st.chat_input("Type your question here..."):
    # Add user's message to the chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send the user's input to Gemini and get the response
    with st.chat_message("model"):
        st.markdown("_Generating response..._")
        chat_history = [
            {"role": msg["role"], "content": msg["content"]}
            for msg in st.session_state.messages
        ]
        chat = model.start_chat(history=chat_history)
        response = chat.send_message(prompt)

        # Display the model's response
        st.markdown(response.text)
        st.session_state.messages.append({"role": "model", "content": response.text})
