import streamlit as st


st.set_page_config(page_title="Chatbot Admin")
st.title("🤖 Chatbot Admin")

# with st.chat_message("assistant"):
#     st.write("Hi! How can I help you?")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role":"assistant",
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

    response = f"Response: {prompt}"
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append(
        {
            "role": "assistant",
            "text": response
        }
    )


