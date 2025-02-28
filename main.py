import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# Set page configuration
st.set_page_config(page_title="Multi-Model App Builder", layout="wide")

# Load environment variables
load_dotenv()

# Configure Google Generative AI
api_key = os.getenv("GOOGLE_API_KEY")
if api_key and api_key != "your_api_key_here":
    genai.configure(api_key=api_key)
else:
    st.warning("Google API key not configured. Please add your API key to the .env file as GOOGLE_API_KEY.")
    st.info("You can get a Google API key from https://ai.google.dev/")
    if st.button("I've added my API key"):
        st.info("Please refresh the page to continue.")

def generate_app_code(framework, task):
    # Function implementation remains the same
    ...

def main():
    st.title("Multi-Model App Builder")
    # Rest of the main function remains the same
    ...

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.error(f"An error occurred: {str(e)}"