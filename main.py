
import os
import time
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from ui.streamlit_ui import render_header, render_framework_selector, render_task_selector, render_footer

# Add retry mechanism for better stability
def with_retry(func, max_retries=3, delay=1):
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise e
            time.sleep(delay)

# Set page configuration
st.set_page_config(
    page_title="Multi-Model App Builder", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load environment variables
load_dotenv()

# Configure Google Generative AI
api_key = os.getenv("GOOGLE_API_KEY")
if api_key and api_key != "your_api_key_here":
    try:
        with st.spinner("Configuring API connection..."):
            with_retry(lambda: genai.configure(api_key=api_key))
        st.success("Google API key configured successfully!")
    except Exception as e:
        st.error(f"Error configuring Google API key: {e}")
        st.info("The app will continue to run with limited functionality.")
else:
    st.warning("Google API key not configured. Please add your API key to the .env file as GOOGLE_API_KEY.")
    st.info("You can get a Google API key from https://ai.google.dev/")
    if st.button("I've added my API key"):
        st.info("Please refresh the page to continue.")

def generate_app_code(framework, task):
    """
    Generates Python code for the selected framework and task using the AI model.
    Args:
        framework (str): The selected framework ('Streamlit' or 'Gradio').
        task (str): The task for which the app will be generated.
    Returns:
        str: Generated Python code or an error message.
    """
    try:
        # Construct the prompt
        prompt = (
            f"Create a {framework} app for the following task: {task}. "
            "Provide the full Python code and ensure it is functional."
        )
        # Send the prompt to the model
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    # Render header using the UI module
    render_header()
    
    # Step 1: Select the framework
    framework = render_framework_selector()
    
    # Step 2: Select a task
    task = render_task_selector()
    
    # Step 3: Generate the app code
    if st.button("Generate App Code"):
        with st.spinner("Generating code..."):
            app_code = generate_app_code(framework, task)
            if app_code:
                st.subheader("Generated Code")
                st.code(app_code, language="python")
            else:
                st.error("Failed to generate the app code. Please try again.")
    
    # Render footer
    render_footer()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
