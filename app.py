# Import necessary libraries
import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

# Load environment variables
load_dotenv()  # Load environment variables from .env file

# Configure Google Generative AI with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to generate a response from Gemini-Pro
def get_gemini_response(input):
    """
    Generates a response from the Gemini-Pro model using the provided input text.

    Args:
        input: The text input to be sent to the model.

    Returns:
        The generated text response from the model.
    """
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

# Function to extract text from a PDF file
def input_pdf_text(uploaded_file):
    """
    Extracts text from a PDF file.

    Args:
        uploaded_file: The uploaded PDF file.

    Returns:
        The extracted text from the PDF file.
    """
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Define the prompt template for Gemini-Pro
input_prompt = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Job Description and the summery of the skills of the submitted resume.
resume:{text}
description:{jd}

I want the response in one single string having the structure
"Job Description Match":"%"
"Profile Summary":""
"""

# Create the Streamlit app
st.title("Smart ATS")

# Input fields for job description and resume
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

# Submit button to trigger evaluation
submit = st.button("Submit")

if submit:
 if uploaded_file is not None:
    # Extract text from the uploaded resume
    text = input_pdf_text(uploaded_file)

    # Generate a response from Gemini-Pro
    response = get_gemini_response(input_prompt)

    # Display the response in a text area
    st.text_area(label="", value=response, height=200)
