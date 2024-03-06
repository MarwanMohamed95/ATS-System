# Smart ATS

Smart ATS is an application built to assist in evaluating resumes based on a provided job description. It utilizes advanced AI technology to analyze resumes and provide feedback on their suitability for a given job.

## Features

- **Resume Evaluation**: Upload a resume and paste a job description to evaluate the resume's suitability for the job.
- **AI-Powered Analysis**: Leveraging Google's Generative AI, the application provides detailed feedback on the match between the resume and job description.

## Getting Started

To use Smart ATS, follow these steps:

1. Clone this repository to your local machine.
2. Install the necessary dependencies by running `pip install -r requirements.txt`.
3. Set up your environment variables by creating a `.env` file and adding your Google API key.
4. Run the application by executing `streamlit run app.py` in your terminal.
5. Paste the job description into the provided text area and upload the resume you want to evaluate.
6. Click the "Submit" button to trigger the evaluation process.

## Prerequisites

Before running the application, you'll need the following:

- Python 3.10 installed on your machine.
- Google API key for access to Google's Generative AI service.

## Technologies Used

- Streamlit: For building the web application.
- Google Generative AI: Powering the resume evaluation with advanced AI capabilities.
- PyPDF2: For extracting text from PDF resumes.
