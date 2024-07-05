
#IMPORTING STREAMLIT AND OLLAMA 
import streamlit as st
import ollama

#TITLE FOR THE BASIC APP
st.title("Local LLMBot")

#INITIALIZING THE RESPONSE AS PER NEED AND PROMPT
default_prompt = """You are a Q"&"A assistant. 
                        Your goal is to answer questions as accurately as possible based 
                        on the instructions, context provided."""

st.session_state["messages"] = [{"role": "assistant", "content": default_prompt}]

#A FUNCTION GENERATE RESPONSE

def generate_response():
    response = ollama.chat(model='llama3', stream=True, messages=st.session_state.messages)
    for partial_resp in response:
        token = partial_resp["message"]["content"]
        st.session_state["full_message"] += token
        yield token

if "full_message" not in st.session_state:
    st.session_state["full_message"] = ""

#ADDING USER INPUT AND GENERATING RESPONSE

if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    st.session_state["full_message"] = ""
    st.chat_message("assistant").write_stream(generate_response)
    st.session_state.messages.append({"role": "assistant", "content": st.session_state["full_message"]})
