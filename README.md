# Resume-Parser-Gemini

Overview
This Streamlit web application allows users to parse resume content into JSON format using the Google Gemini Large Language Model (LLM). Users can input the path to a resume file (PDF), which is then processed through the Gemini LLM model to generate structured JSON data representing different sections of the resume.

Features
Input Resume File Path: Users can provide the file path to the resume file (located on their local system or accessible via URL).

Parse to JSON: The application uses the Google Gemini LLM model to parse the resume content from the specified file path into structured JSON format.

Display JSON Output: The parsed JSON data is displayed on the web interface, showing sections such as Personal Information, Education, Work Experience, Skills, and Certifications.

##Requirements
Python 3.x
Streamlit
Google Gemini LLM model (API or hosted service)

##Usage
Provide Resume File Path

Enter the path to the resume file (e.g., /path/to/your/resume.pdf) into the designated input field on the web interface.
Parse and View JSON Output

After entering the file path, the application will use the Gemini LLM model to parse the resume content.
The parsed JSON data will be displayed on the same page, showing structured information from the resume.
