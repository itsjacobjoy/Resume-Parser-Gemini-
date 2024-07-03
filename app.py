import streamlit as st
from langchain_community.document_loaders import PyMuPDFLoader
import getpass
import os
from langchain_google_genai import ChatGoogleGenerativeAI 
from prompt_template import prompt_template
from prompt_template_2 import prompt_template_2
import json


#Converting json string data to a json file
def json_string_to_json(json_string, file_name='output.json'):
    try:
        # Parse JSON string into a dictionary
        data = json.loads(json_string)
        
        # Write the dictionary to a JSON file
        # with open(file_name, 'w') as json_file:
        #     json.dump(data, json_file, indent=4)
        
        # print(f"JSON data has been written to {file_name}")
        return data
    
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")

#Loading PDF and parsing content to JSON fromat
def load_and_parse(path):

    loader = PyMuPDFLoader(path)

    data = loader.load()
    resume_content = ""
    for page in data:
        resume_content += page.page_content


    os.environ["GOOGLE_API_KEY"] = "API_KEY"
    llm = ChatGoogleGenerativeAI(model="gemini-pro")

    prompt = prompt_template(resume_content)
    result = llm.invoke(prompt)

    prompt_2 = prompt_template_2(result.content)
    result_fin = llm.invoke(prompt_2)

    data = json_string_to_json(result_fin.content, 'resume.json')
    return data


st.header("Resume Parser")
st.markdown(
    """
        Resume Parser
    """
)

path = st.text_input(label="Enter the file path to your resume")
if path:
    print("pdf path", path)
    data = load_and_parse(path)
    data        


