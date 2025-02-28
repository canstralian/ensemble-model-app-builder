
import streamlit as st

def render_header():
    """Render the app header"""
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
        st.write("This version has been created and expanded upon to utilize multiple models for enhanced code generation.")

def render_framework_selector():
    """Render the framework selection UI"""
    return st.selectbox("Select a framework:", ["Streamlit", "Gradio"])

def render_task_selector():
    """Render the task selection UI"""
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
    return custom_task if custom_task.strip() else task

def render_footer():
    """Render the app footer"""
    st.markdown("""
    ## Acknowledgements

    * Hugging Face for providing the Spaces platform and Transformers library.
    * Google for Gemini Pro.
    * Salesforce for CodeT5.
    * BigScience for T0.
    * Streamlit and Gradio communities.
    """)
