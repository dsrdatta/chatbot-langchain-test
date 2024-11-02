import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

#init Streamlit
st.set_page_config(page_title="Conversational chatbot")
st.header("Hi, Whatssup!!")

chatllm = ChatOpenAI(temperature=0.6, openai_api_key=os.getenv('OPEN_API_KEY'))

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content='Act as Food Delivery AI Agent')
    ]

def get_oi_response(question):

    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chatllm(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))

    return answer.content

input = st.text_input("Input: ",key="input")
response = get_oi_response(input)

submit=st.button("How can I help!")

if submit:
    st.subheader("Chat assisstant: ")
    st.write(response)
    


