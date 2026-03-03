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

⸻

Ensemble Model App Builder

An AI-powered tool that streamlines the creation of Streamlit and Gradio applications by leveraging multiple large language models for efficient and accurate code generation.

⸻

Project Description

The Ensemble Model App Builder simplifies the development of interactive web applications by integrating the capabilities of multiple large language models. Users can describe the desired functionality, select their preferred framework (Streamlit or Gradio), and receive generated Python code tailored to their specifications. This approach accelerates prototyping and reduces the need for extensive coding knowledge.

⸻

Table of Contents
   •   Installation
   •   Usage
   •   Contributing
   •   License
   •   Roadmap
   •   Credits
   •   Support
   •   FAQ

⸻

Installation
	1.	Clone the Repository:

git clone https://github.com/canstralian/ensemble-model-app-builder.git
cd ensemble-model-app-builder


	2.	Set Up a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


	3.	Install Dependencies:

pip install -r requirements.txt


	4.	Run the Application:

streamlit run app.py



⸻

Usage
	1.	Provide an App Description:
Enter a clear and concise description of the application you wish to build.
	2.	Select a Framework:
Choose between Streamlit and Gradio as your preferred framework.
	3.	Generate Code:
Click the “Generate” button to initiate code generation using integrated language models.
	4.	Review and Customize:
Examine the generated code and make any necessary adjustments to fit your specific requirements.
	5.	Deploy or Run Locally:
Deploy the application using platforms like Streamlit Sharing or Hugging Face Spaces, or run it locally for testing.

⸻

Contributing

Contributions are welcome! To contribute:
	1.	Fork the Repository
	2.	Create a Feature Branch:

git checkout -b feature/YourFeature


	3.	Commit Your Changes:

git commit -m "Add YourFeature"


	4.	Push to the Branch:

git push origin feature/YourFeature


	5.	Open a Pull Request

Please ensure your code adheres to the project’s coding standards and includes appropriate tests.

⸻

License

This project is licensed under the MIT License.

⸻

Roadmap
   •   Enhance model integration for improved code generation accuracy.
   •   Expand support for additional frameworks beyond Streamlit and Gradio.
   •   Implement user authentication and project saving features.

⸻

Credits
   •   Original Concept: Louie F. Cervantes, M.Eng (Information Engineering), West Visayas State University
   •   Refinement and Expansion: WhackTheJacker

⸻

Support

For support or inquiries, please open an issue on the GitHub repository.

⸻

FAQ

Q: Which language models are integrated into the application?
A: The application utilizes Gemini Pro 2.0, Salesforce/codet5-small, and bigscience/T0_3B for code generation.

Q: Can I deploy the generated applications to platforms like Hugging Face Spaces?
A: Yes, the generated code is compatible with deployment platforms such as Hugging Face Spaces and Streamlit Sharing.

Q: Is there a way to save and manage multiple projects within the application?
A: Currently, project management features are in development. Future updates aim to include user authentication and project saving capabilities.

⸻

For more information and to explore the project further, visit the GitHub repository.

⸻
