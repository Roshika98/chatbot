import streamlit
import streamlit as st
from src.gemini_client import GeminiClient

st.set_page_config(page_title="Chatbot Admin")
st.title("🤖 Chatbot Admin")


@streamlit.cache_resource
def load_genai_client():
    client = GeminiClient()
    return client.create_chat()


if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "text": "Hi! How can I help you?"
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

if prompt := st.chat_input():
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append(
        {
            "role": "user",
            "text": prompt
        }
    )

    chat = load_genai_client()
    model_response = GeminiClient.send_message(chat, prompt)

    response = f"Response: {prompt}"
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append(
        {
            "role": "assistant",
            "text": response
        }
    )
