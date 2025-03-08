
import streamlit as st

def load_css():
    """Load custom CSS"""
    with open("ui/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def render_header():
    """Render the app header with improved styling"""
    st.markdown("""
    <div class="title-container">
        <h1 class="header-title">Multi-Model App Builder</h1>
        <p class="app-description">Generate Python code for interactive web applications using AI models</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ About This Tool"):
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
    """Render the framework selection UI with cards"""
    st.markdown("<h3>Step 1: Choose Your Framework</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        streamlit_selected = st.button("Streamlit", use_container_width=True)
        st.markdown("""
        <div class="framework-card">
            <h4>Streamlit</h4>
            <p>Build data apps with Python in minutes</p>
            <ul>
                <li>Simple Python syntax</li>
                <li>Great for data visualization</li>
                <li>Fast prototyping</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        gradio_selected = st.button("Gradio", use_container_width=True)
        st.markdown("""
        <div class="framework-card">
            <h4>Gradio</h4>
            <p>Create UIs for your machine learning models</p>
            <ul>
                <li>ML model interfaces</li>
                <li>Audio/image processing</li>
                <li>Simple API deployment</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Return the selected framework
    if streamlit_selected:
        return "Streamlit"
    elif gradio_selected:
        return "Gradio"
    else:
        return st.selectbox("Select a framework:", ["Streamlit", "Gradio"], key="framework_fallback")

def render_task_selector():
    """Render the task selection UI with improved styling"""
    st.markdown("<h3>Step 2: Select Your Task</h3>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="task-container">
        <p>Choose from our predefined tasks or describe your own custom application</p>
    </div>
    """, unsafe_allow_html=True)
    
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
    
    st.markdown("<p>Or describe your custom application:</p>", unsafe_allow_html=True)
    custom_task = st.text_area("Custom task description:", 
                              placeholder="Example: A dashboard to visualize stock market data with interactive charts...")
    
    # Use the custom task if provided
    return custom_task if custom_task.strip() else task

def render_generate_button():
    """Render a styled generate button"""
    return st.button("Generate App Code", type="primary", use_container_width=True)

def render_code_display(code):
    """Render the generated code with styling"""
    st.markdown("""
    <div class="code-container">
        <h3>Generated Code</h3>
        <p>Copy and run this code to create your application</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.code(code, language="python")
    
    # Add download button
    st.download_button(
        label="Download Code",
        data=code,
        file_name="generated_app.py",
        mime="text/plain",
    )

def render_footer():
    """Render the app footer with improved styling"""
    st.markdown("""
    <div class="footer-container">
        <h3>Powered By</h3>
        <div>
            <span class="model-badge">Gemini 1.5 Flash</span>
            <span class="model-badge">CodeT5</span>
            <span class="model-badge">T0_3B</span>
        </div>
        <p>© 2023 Multi-Model App Builder</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("Acknowledgements"):
        st.markdown("""
        ## Acknowledgements

        * Hugging Face for providing the Spaces platform and Transformers library.
        * Google for Gemini Pro.
        * Salesforce for CodeT5.
        * BigScience for T0.
        * Streamlit and Gradio communities.
        """)
