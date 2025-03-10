
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Generative AI
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("Google API key not found. Please add it to your .env file as GOOGLE_API_KEY.")

def generate_app_code(framework, task):
    """
    Generate code for a Streamlit or Gradio app based on the selected task.
    
    Args:
        framework (str): The framework to use ('Streamlit' or 'Gradio')
        task (str): The task description
        
    Returns:
        str: The generated code
    """
    try:
        # Initialize the Gemini model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Construct the prompt
        prompt = f"""
        Create a Python {framework} application that accomplishes the following task:
        {task}
        
        Requirements:
        1. The code should be complete and runnable
        2. Include necessary imports
        3. Use best practices for {framework}
        4. Include comments explaining the code
        5. Handle errors gracefully
        
        Return only the Python code without any explanation or markdown formatting.
        """
        
        # Generate the response
        response = model.generate_content(prompt)
        
        # Extract the code from the response
        if hasattr(response, 'text'):
            return response.text.strip()
        else:
            return None
            
    except Exception as e:
        st.error(f"Error generating code: {str(e)}")
        return None

def main():
    """
    The main function that sets up the Streamlit app and handles user interactions.
    
    This function:
    1. Sets the page configuration for the Streamlit app.
    2. Displays the app title and an information expander.
    3. Allows the user to select a framework (Streamlit or Gradio) and a predefined task or enter a custom task.
    4. Generates the app code based on the user's selections and displays it.
    5. Handles any exceptions that may occur during the code generation process.
    """
    st.set_page_config(page_title="Multi-Model App Builder", layout="wide")
    
    st.title("Multi-Model App Builder")
    
    with st.expander("ℹ️ About"):
        st.write(
            "This tool generates Python code for a Streamlit or Gradio app based on a selected task. "
            "It uses the Gemini 1.5 flash model to generate the code. "
            "You can select a predefined task or enter a custom one."
        )
        st.write("This project is based on the initial work of:")
        st.markdown(
            "Louie F. Cervantes, M.Eng (Information Engineering) \n\n"
            "West Visayas State University"
        )
        st.write("This version has been created and expanded upon by **WhackTheJacker** to utilize multiple models for enhanced code generation.")

    # Step 1: Select the framework
    framework = st.selectbox("Select a framework:", ["Streamlit", "Gradio"])

    # Step 2: Select a task or enter a custom one
    predefined_tasks = [
        "Interactive Data Explorer",
        "Simple Linear Regression",
        "Image Classification with Pre-trained Model",
        "Text Summarizer",
        "Sentiment Analysis Tool",
        "Interactive Quiz App",
        "Basic Calculator",
        "Unit Converter",
        "Color Mixer",
        "Simple Game (e.g., Number Guessing)",
    ]
    task = st.selectbox("Select a predefined task:", predefined_tasks)
    custom_task = st.text_input("Or enter a custom task:")
    # Use the custom task if provided
    task = custom_task if custom_task.strip() else task

    # Step 3: Generate the app code
    if st.button("Generate App Code"):
        with st.spinner("Generating code..."):
            app_code = generate_app_code(framework, task)
            if app_code:
                st.subheader("Generated Code")
                st.code(app_code, language="python")
            else:
                st.error("Failed to generate the app code. Please try again.")

    st.markdown("""
    ## Acknowledgements

    * Hugging Face for providing the Spaces platform and Transformers library.
    * Google for Gemini Pro.
    * Salesforce for CodeT5.
    * BigScience for T0.
    * Streamlit and Gradio communities.
    * Louie F. Cervantes, M.Eng for the foundational work.
    """)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Handle exceptions gracefully
        st.error(f"An error occurred: {str(e)}")
