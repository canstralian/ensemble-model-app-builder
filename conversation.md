## import streamlit as stimport google.generativeai as genaiimport osAPI_KEY = os.getenv("GEMINI_API_KEY")genai.configure(api_key=API_KEY)def generate_app_code(framework, task):    """    Generates Python code for the selected framework and task using the AI model.    Args:        framework (str): The selected framework ('Streamlit' or 'Gradio').        task (str): The task for which the app will be generated.    Returns:        str: Generated Python code or an error message.    """    try:        # Construct the prompt        prompt = (            f"Create a {framework} app for the following task: {task}. "            "Provide the full Python code and ensure it is functional."        )        # Send the prompt to the model        model = genai.GenerativeModel("gemini-1.5-flash")        response = model.generate_content(prompt)        return response.text    except Exception as e:        return f"An error occurred: {e}"def main():        # Streamlit UI    st.title("App Builder: Streamlit or Gradio")    with st.expander("ℹ️ About"):        st.write(            "This tool generates Python code for a Streamlit or Gradio app based on a selected task. "            "It uses the Gemini 1.5 flash model to generate the code. "            "You can select a predefined task or enter a custom one.")        st.markdown("Programmed by: \n\n \        Louie F. Cervantes, M.Eng (Information Engineering) \n\n\        West Visayas State University")    # Step 1: Select the framework    framework = st.selectbox("Select a framework:", ["Streamlit", "Gradio"])    # Step 2: Select a task or enter a custom one    predefined_tasks = [        "Interactive Data Explorer",        "Simple Linear Regression",        "Image Classification with Pre-trained Model",        "Text Summarizer",        "Sentiment Analysis Tool",        "Interactive Quiz App",        "Basic Calculator",        "Unit Converter",        "Color Mixer",        "Simple Game (e.g., Number Guessing)"    ]    task = st.selectbox("Select a predefined task:", predefined_tasks)    custom_task = st.text_input("Or enter a custom task:")    # Use the custom task if provided    task = custom_task if custom_task.strip() else task    # Step 3: Generate the app code    if st.button("Generate App Code"):        with st.spinner("Generating code..."):            app_code = generate_app_code(framework, task)            if app_code:                st.subheader("Generated Code")                st.code(app_code, language="python")            else:                st.error("Failed to generate the app code. Please try again.")if __name__ == "__main__":    main()

```python
import streamlit as st
import google.generativeai as genai
import os

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

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
    # Streamlit UI
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
    main()
```

**Changes Made:**

1.  **Title Update:**
    * `st.title("App Builder: Streamlit or Gradio")` changed to `st.title("Multi-Model App Builder")`
2.  **About Section Modification:**
    * The `st.expander("ℹ️ About")` section now includes the acknowledgment of Louie F. Cervantes's work and WhackTheJacker's adaptation.
    * Specifically, I added `st.write("This project is based on the initial work of:")` and `st.write("This version has been created and expanded upon by **WhackTheJacker** to utilize multiple models for enhanced code generation.")`
3.  **Acknowledgements Section Addition:**
    * Added an `st.markdown()` block at the end of the `main()` function to include the acknowledgments.
4.  **Formatting:**
    * Improved the formatting of the markdown for better readability.
    * Used `st.write()` for simple text and `st.markdown()` for formatted text, including line breaks.
5.  **Model Update:**
    * Please note that the code still only uses the gemini-1.5-flash model. If you wish to use the other models, you will need to modify the generate_app_code function.
