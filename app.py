import streamlit as st
from pipeline import pipe

st.title("AI Law Assistant")

@st.cache_resource
def get_chain():
    return pipe()

chain = get_chain()

question = st.text_input("Ask a question regarding AI EU laws")

if st.button("Ask") and question:
    st.write(chain.invoke(question))