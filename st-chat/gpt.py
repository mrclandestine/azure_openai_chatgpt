import streamlit as st
from streamlit_chat import message
import requests
import openai
import toml

with open('secrets.toml', 'r') as f:
    config = toml.load(f)

openai.api_type = "azure"
openai.api_key = config['66ec211e97de438d9a7f6882f2c80d10']
openai.api_base = "https://we-ww-secdev-openai-ai.openai.azure.com"
openai.api_version = "2023-03-15-preview"


st.set_page_config(page_title="Custom ChatGPT", page_icon="💬")

st.markdown("# Custom ChatGPT")
st.sidebar.header("Custom ChatGPT")

#generating 2 empty lists to store past and generated value in the conversation

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

    user_input = st.text_input("You: ","Hello, how are you?", key="input")

if user_input:
    output = openai.Completion.create(
          engine="test1",
          prompt=user_input,
          temperature=0,
          max_tokens=1041,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0,
          best_of=1,
          stop=None)

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output["choices"][0]["text"].strip())

    if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], avatar_style = 'bottts', key=str(i))
        message(st.session_state['past'][i], avatar_style = 'big-ears',is_user=True, key=str(i) + '_user')

        if user_input:
    output = openai.Completion.create(
          engine="test1",
          prompt=f"{st.session_state.past}\n{user_input}",
          temperature=0,
          max_tokens=1041,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0,
          best_of=1,
          stop=None)

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output["choices"][0]["text"].strip())
