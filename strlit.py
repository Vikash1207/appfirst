import streamlit as st

st.title("Interactive Streamlit App")

name = st.text_input("Enter your name:")
age = st.slider("Select your age", 1, 100)

if st.button("Submit"):
    st.write(f"Hello {name}, you are {age} years old!")
