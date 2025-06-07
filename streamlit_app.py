import streamlit as st

# Set the title of the web app
st.title("Simple Streamlit App")

# Add a text input box
name = st.text_input("Enter your name:")

# When the user enters a name, display a greeting
if name:
    st.write(f"Hello, {name}! 👋 Welcome to Streamlit!")
