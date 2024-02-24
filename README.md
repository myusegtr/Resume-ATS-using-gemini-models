# Resume Tracking LLM app

## Aim of Project

The aim of this project is to develop an Intelligent Resume Application Tracking System (ATS) using Streamlit and Google's Generative AI models. The system aims to assist job seekers in improving their resumes by providing tailored feedback based on job descriptions, evaluating the match percentage, and identifying missing keywords.

## Steps involved

 #### Setup Environment: 
 Load necessary libraries and configure environment variables using .env files.

#### Text Extraction from PDF:
Extract text from the uploaded PDF resume using PyPDF2 library.
Generate Prompt: Construct a prompt template for the Generative AI model, incorporating job description and resume text.

#### Model Interaction: 
Utilize Google's Generative AI models (Gemini-pro and Gemini-pro-vision) to generate responses based on the provided input.

#### Streamlit Application: 
Develop a user-friendly interface using Streamlit for users to input job descriptions, upload resumes, and trigger the analysis process.

#### Feedback Display: 
Present the generated responses to users, providing insights on resume improvements, matching percentage, and missing keywords.


## Tools/Tech Stack Required

Python: Programming language used for backend logic.
Streamlit: Framework for building interactive web applications.
PyPDF2: Library for extracting text from PDF documents.
Google's Generative AI: AI models used for generating responses based on input.
python-dotenv: Library for loading environment variables from .env files.


## Conclusion

This project offers a user-friendly solution for job seekers to enhance their resumes by leveraging AI-driven analysis. By providing tailored feedback, matching percentage, and highlighting missing keywords, the system assists users in optimizing their job applications and improving their chances in the competitive job market.

## What Extra Can Be Done in This Project

#### Enhanced Resume Analysis: 
Integrate more sophisticated AI models for deeper resume analysis, such as sentiment analysis, skills matching, and semantic understanding.

#### User Authentication: 
Implement user authentication to personalize the feedback and store previous analysis results securely.

#### Resume Template Suggestions: 
Provide suggestions for resume templates based on the job description and industry standards.

#### Integration with Job Portals: 
Integrate with job portals to directly fetch job descriptions and streamline the analysis process.

#### Natural Language Processing (NLP) Enhancements: 
Incorporate advanced NLP techniques for better understanding of job descriptions and resumes, enabling more accurate matching and recommendations.