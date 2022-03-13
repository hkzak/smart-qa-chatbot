import streamlit as st
import requests
from typing import Dict


st.set_page_config(page_title="NLB BOT", page_icon="🤖")
st.sidebar.title("NLP Bot")
st.title("""
NLP Bot  
NLP Bot is an NLP conversational chatbot that answers your qustions based on the data that you train it with. 
""")
menu = {"Ask Bot", "Train Bot"}
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Ask Bot":
  st.subheader("Ask Bot")
  with st.form("form"):
    user_input = st.text_input("You: ","Enter your Query here.....")

    submit = st.form_submit_button("Ask")

    if submit:
      with st.spinner("Processing..."):
            url = "http://127.0.0.1:8001/askQuestion/"
            payload = {'query': user_input}
            response = requests.post(url, json=payload)
            response_json = response.json()
            print(response_json["Answer"])
            if response:
              st.text_area("Bot:", value= response_json["Answer"], height=200, max_chars=None, key=None)
            else:
                st.text_area("Bot:", value="Please enter your question and click the Ask Button", height=200, max_chars=None, key=None)

if choice == "Train Bot":
  st.subheader("Train Bot")

  training_data = st.file_uploader("Upload File",type=['txt'], accept_multiple_files=True)
  if st.button("Process"):
    for uploaded_file in training_data:
       value = uploaded_file.read()
       st.write(value)

     