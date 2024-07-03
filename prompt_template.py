#Creating a prompt template to parse resume into json format
def prompt_template(resume):
  template = f'''
  System : Parse this text content in json format, seperating the content into defined sections , for example, personal information, education, work experience, etc.
  
  System: Following are examples of correctly extracting inforation and parsing as json

  Resume: "John Doe 123 Main Street, Anytown, USA Email: john.doe@example.com Phone: (123) 456-7890 Professional Summary Software engineer with 3 years of experience in web development. 
  Experience
  Software Engineer
  XYZ Tech Solutions
  2021 - Present

  Developed web applications using JavaScript and React.
  Improved user experience through new features.
  Junior Developer
  ABC Software Inc.
  2019 - 2021

  Assisted in developing internal tools.
  Contributed to code reviews.
  Education
  B.Sc. in Computer Science
  University of Somewhere
  2019

  Skills
  JavaScript, Python
  React, Node.js
  Git, Docker
  "

  json output: 
  {{
  "personal_information": {{
    "name": "John Doe",
    "address": "123 Main Street, Anytown, USA",
    "email": "john.doe@example.com",
    "phone": "(123) 456-7890"
  }},
  "professional_summary": "Software engineer with 3 years of experience in web development.",
  "experience": [
    {{
      "job_title": "Software Engineer",
      "company": "XYZ Tech Solutions",
      "start_date": "2021",
      "end_date": "Present",
      "responsibilities": [
        "Developed web applications using JavaScript and React.",
        "Improved user experience through new features."
      ]
    }},
    {{
      "job_title": "Junior Developer",
      "company": "ABC Software Inc.",
      "start_date": "2019",
      "end_date": "2021",
      "responsibilities": [
        "Assisted in developing internal tools.",
        "Contributed to code reviews."
      ]
    }}
  ],
  "education": [
    {{
      "degree": "B.Sc. in Computer Science",
      "institution": "University of Somewhere",
      "graduation_date": "2019"
    }}
  ],
  "skills": {{
    "programming_languages": ["JavaScript", "Python"],
    "frameworks": ["React", "Node.js"],
    "tools_technologies": ["Git", "Docker"]
  }}
}}


  System: Parse this text content in json format, seperating the content into defined sections. Follow the format specified in the example.

  Resume: {resume}
  
  json output: '''

  return template
