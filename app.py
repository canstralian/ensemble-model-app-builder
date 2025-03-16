import os
import time

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

from ui.streamlit_ui import (
    load_css,
    render_code_display,
    render_footer,
    render_framework_selector,
    render_generate_button,
    render_header,
    render_task_selector,
)

# Initialize session state
if "api_key" not in st.session_state:
    st.session_state["api_key"] = None
if "generated_code" not in st.session_state:
    st.session_state["generated_code"] = None
if "selected_framework" not in st.session_state:
    st.session_state["selected_framework"] = None

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
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load custom CSS
load_css()

# Load environment variables
load_dotenv()

# Configure Google Generative AI
api_key = os.getenv("GOOGLE_API_KEY")
if api_key and api_key != "your_api_key_here":
    try:
        with st.spinner("Configuring API connection..."):
            with_retry(lambda: genai.configure(api_key=api_key))
        st.session_state["api_key"] = api_key
        st.success("Google API key configured successfully!")
    except Exception as e:
        st.error(f"Error configuring Google API key: {e}")
        st.info("The app will continue to run with limited functionality.")
else:
    st.sidebar.warning(
        "Google API key not configured. Please add your API key to the .env file as GOOGLE_API_KEY."
    )
    st.sidebar.info("You can get a Google API key from https://ai.google.dev/")
    api_key_input = st.sidebar.text_input(
        "Or enter your Google API key here:", type="password"
    )
    if api_key_input:
        try:
            with st.spinner("Configuring API connection..."):
                with_retry(lambda: genai.configure(api_key=api_key_input))
            st.session_state["api_key"] = api_key_input
            st.success("Google API key configured successfully!")
        except Exception as e:
            st.error(f"Error configuring Google API key: {e}")
            st.session_state["api_key"] = None

def generate_app_code(framework, task):
    if not st.session_state.get("api_key"):
        return "API key not configured. Please provide a Google API key to generate code."

    try:
        prompt = (
            f"Create a {framework} app for the following task: {task}. "
            "Provide the full Python code and ensure it is functional."
        )

        def get_response():
            model = genai.GenerativeModel("gemini-1.5-flash")
            return model.generate_content(prompt)

        response = with_retry(get_response)
        if hasattr(response, "text"):
            return response.text
        return "Error: Unable to generate code. Invalid response format."
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    render_header()

    col1, col2 = st.columns([2, 1])

    with col1:
        framework = render_framework_selector()
        st.session_state["selected_framework"] = framework
        task = render_task_selector()

        if render_generate_button():
            with st.spinner("Generating code with AI..."):
                app_code = generate_app_code(framework, task)
                if app_code:
                    st.session_state["generated_code"] = app_code
                    st.success("Code generated successfully!")
                else:
                    st.error("Failed to generate the app code. Please try again.")

    with col2:
        st.markdown("### App Preview")
        st.info(
            f"Framework: {st.session_state['selected_framework'] if st.session_state['selected_framework'] else 'Not selected'}"
        )
        st.markdown("### Sample Apps")
        st.image(
            "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png",
            width=200,
        )
        st.image("https://gradio.app/images/logo.svg", width=200)

        st.markdown("### Tips")
        st.info(
            "• Be specific in your task description\n• Run the generated code in a new file\n• Experiment with different frameworks"
        )

    if st.session_state["generated_code"]:
        render_code_display(st.session_state["generated_code"])

    render_footer()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")