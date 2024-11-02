from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st

#load OpenAI model
def get_oi_response(question):
    llm=OpenAI(temperature=0.5, openai_api_key=os.getenv('OPEN_API_KEY'))
    response=llm(question)
    return response

##init streamlit
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain chatbot")

input = st.text_input("Input: ",key="input")
response = get_oi_response(input)

submit=st.button("Ask a Question")

if submit:
    st.subheader("The Ai says")
    st.write(response)
    