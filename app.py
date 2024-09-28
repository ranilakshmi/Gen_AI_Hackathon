import streamlit as st
import requests

st.title("ConsumeWise")
st.text(
    "This application has been created as part of the Gen AI Exchange Hackathon by Google"
)

ingredients = st.text_input("Ingredients")
if st.button("Submit"):
    if ingredients:
        st.write("Ingredients given :\n",ingredients)
