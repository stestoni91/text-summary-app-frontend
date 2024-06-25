import streamlit as st
from summarize import summarize

st.title("Welcome to Summerize-It")
st.header("The app that will make you forget about reading loooooong boring text 🥱... and save your time! 😎")
st.write("")
st.write("")

st.subheader("Enter the long text that you can't bother reading 👇")
text = st.text_area(label='Label', placeholder="Long boring text 🥱", key='text', label_visibility='hidden')

button = st.button(label="Summarize it!", type="primary")
if button:
    with st.spinner('Writing your summary...'):
        summary = summarize(text)
    st.divider()
    st.subheader("Here is your summary ✨")
    st.write(summary)
