import streamlit as st
from streamlit_chat import message
from utils import get_initial_message, get_chatgpt_response, update_chat
import os
from dotenv import load_dotenv
load_dotenv()
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

st.title("Alyncyn AI")
st.subheader("Ask Anything !")

# Hardcode the model selection
model = "gpt-3.5-turbo"  # Change to "gpt-4" if needed

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

query = st.text_input("Query: ", key="input")

if 'messages' not in st.session_state:
    st.session_state['messages'] = get_initial_message()

uploaded_files = st.file_uploader("Upload your PDF, CSV, XLSX, or DOC files", type=["pdf", "csv", "xlsx", "doc"], accept_multiple_files=True)

if uploaded_files:
    st.write("You have uploaded:", ", ".join([f.name for f in uploaded_files]))

if query:
    with st.spinner("Generating..."):
        messages = st.session_state['messages']
        messages = update_chat(messages, "user", query)
        response = get_chatgpt_response(messages, model)
        messages = update_chat(messages, "assistant", response)
        st.session_state.past.append(query)
        st.session_state.generated.append(response)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))
