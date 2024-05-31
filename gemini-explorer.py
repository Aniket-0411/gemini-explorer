import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, ChatSession

# Initialize Vertex AI
project = "light-trail-424903-r1"
vertexai.init(project=project)

# Set up the generation configuration
config = generative_models.GenerationConfig(
    temperature=0.4
)
model = GenerativeModel(
    "gemini-pro",
    generation_config=config
)
chat = model.start_chat()

def llm_function(chat, query):
    # Send the user's query to the chat session
    response = chat.send_message(query)
     
    # Retrieve and process the response from the chat session
    processed_response = process_response(response)
    
    # Update the session state with the processed response
    st.session_state.messages.append({"role": "assistant", "content": processed_response})

def process_response(response):
    # Process the response by extracting relevant content
    processed_response = response.candidates[0].content.parts[0].text
    return processed_response

# Streamlit app title
st.title("Gemini Explorer")

# Initialize the chat history and username in the Streamlit session state if they do not already exist
if "messages" not in st.session_state:
    st.session_state.messages = []
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# Display the username input only if it has not been provided yet
if st.session_state.user_name == "":
    user_name = st.text_input("Please enter your name")
    if user_name:
        st.session_state.user_name = user_name
        initial_prompt = f"Introduce yourself as Rex AI. Use the emogis to be creative and introduce in pirate speak language. Keep it short below 20-30 words and single paragraph, greet me using {st.session_state.user_name}"
        llm_function(chat,initial_prompt)
else:
    # Once the username is provided, display the chat interface
    query = st.chat_input("Type your message here...")
    if query:
        # Add the user's message to the session state
        st.session_state.messages.append({"role": "user", "content": query})
        # Process the user's input
        llm_function(chat, query)

    # Display the chat messages
    for index, message in enumerate(st.session_state.messages):
        if message["role"] == "user":
            st.write(f"**You:** {message['content']}")
        else:
            st.write(f"**ReX:** {message['content']}")
