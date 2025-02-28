---
title: Ensemble Model App Builder
emoji: 👀
colorFrom: purple
colorTo: gray
sdk: streamlit
sdk_version: 1.42.2
app_file: app.py
pinned: false
license: apache-2.0
short_description: An AI-powered App Builder for Streamlit and Gradio Apps
models:
  - gemini-pro-2.0
  - Salesforce/codet5-small
  - bigscience/T0_3B
---
# Multi-Model App Builder

[![Hugging Face Spaces - SDK](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces%20SDK-blue)](https://huggingface.co/spaces/whackthejacker/ensemble-model-app-builder)
[![Streamlit App](https://img.shields.io/badge/Streamlit-App-orange.svg)](https://streamlit.io/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Models: Gemini Pro 2.0, CodeT5-small, T0_3B](https://img.shields.io/badge/Models-Gemini%20Pro%202.0%2C%20CodeT5--small%2C%20T0_3B-green)](https://huggingface.co/whackthejacker/ensemble-model-app-builder)

👀 **A Multi-Model AI-Powered App Builder for Streamlit and Gradio Apps**

This Hugging Face Space provides a user-friendly interface to generate Streamlit and Gradio applications using the combined power of multiple large language models. With this tool, you can quickly prototype and build interactive web applications without extensive coding knowledge.

## About

This tool generates Python code for a Streamlit or Gradio app based on a selected task. It uses a combination of Gemini Pro 2.0, Salesforce/codet5-small, and bigscience/T0_3B models to generate the code. You can select a predefined task or enter a custom one.
This project is based on the initial work of:
**Louie F. Cervantes, M.Eng (Information Engineering)**
West Visayas State University
This version has been created and expanded upon by **WhackTheJacker** to utilize multiple models for enhanced code generation.
## Features
* **Multi-Model Code Generation:** Leverages Gemini Pro 2.0, Salesforce/codet5-small, and bigscience/T0_3B for robust code generation.
* **Intuitive Interface:** Easily describe your desired application functionality, and let the AI generate the code for you.
* **Streamlit and Gradio Support:** Choose between generating Streamlit or Gradio applications based on your preference.
* **Rapid Prototyping:** Accelerate your development process by quickly generating and iterating on application ideas.

## How to Use

1.  **Describe Your App:** Enter a clear and concise description of the application you want to build.
2.  **Select Framework:** Choose whether you want to generate a Streamlit or Gradio app.
3.  **Generate Code:** Click the "Generate" button to let the AI create the Python code.
4.  **Review and Customize:** Review the generated code and make any necessary adjustments.
5.  **Run the App:** Copy the generated code and run it in your local environment or deploy it to a platform like Streamlit Sharing or Hugging Face Spaces.

## Models Used

* **Gemini Pro 2.0:** For general-purpose code generation and understanding natural language descriptions.
* **Salesforce/codet5-small:** For code-specific tasks and improving the quality of the generated code.
* **bigscience/T0_3B:** For natural language understanding and instruction following.
## Example Usage
"Create a Streamlit app that displays a simple text input and outputs the entered text in uppercase."
## Getting Started Locally
1.  Clone this repository.
2.  Install the required dependencies: `pip install streamlit gradio transformers`
3.  Run the Streamlit app: `streamlit run app.py`
## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
## License
This project is licensed under the Apache 2.0 License.
## Acknowledgements
* Hugging Face for providing the Spaces platform and Transformers library.
* Google for Gemini Pro.
* Salesforce for CodeT5.
* BigScience for T0.
* Streamlit and Gradio communities.
* Louie F. Cervantes, M.Eng for the foundational work.
## Contact
If you have any questions or feedback, please feel free to contact me.