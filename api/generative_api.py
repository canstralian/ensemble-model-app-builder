import os

import google.generativeai as genai


def initialize_gemini_api():
    """Initialize the Gemini API with the API key from environment variables."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key and api_key != "your_api_key_here":
        genai.configure(api_key=api_key)
        return True
    return False


def generate_code_with_gemini(framework, task):
    """
    Generate code using Gemini model.

    Args:
        framework (str): The selected framework ('Streamlit' or 'Gradio').
        task (str): The task description.

    Returns:
        str: Generated code or error message.
    """
    try:
        prompt = (
            f"Create a {framework} app for the following task: {task}. "
            "Provide the full Python code and ensure it is functional."
        )
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating code with Gemini: {str(e)}"
