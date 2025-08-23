import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-pro')



# print(response.content)
st.header("Research Assistant")

user_input = st.text_input("Enter your message")

if st.button("Summarize"):
    response = model.invoke(user_input)
    st.write(response.content)

#
