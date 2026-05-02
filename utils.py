import os
from openai import OpenAI
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from groq import Groq

client = Groq(api_key=os.environ["GROQ_API_KEY"])



# FILE HANDLING

def extract_text(file):
    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    else:
        return file.read().decode("utf-8")



# LLM CALL WRAPPER

def ask_llm(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content



# CORE FEATURES and functions

def summarize(text):
    prompt = f"""
    Summarize the following financial or audit document in a clear executive summary:

    {text[:12000]}
    """
    return ask_llm(prompt)


def extract_risks(text):
    prompt = f"""
    Identify key risks, issues, anomalies, or red flags in this document.
    Provide bullet points with short explanations:

    {text[:12000]}
    """
    return ask_llm(prompt)


def generate_report(text):
    prompt = f"""
    Create a structured business report with:
    - Executive Summary
    - Key Findings
    - Risks & Issues
    - Recommendations

    {text[:12000]}
    """
    return ask_llm(prompt)



# ADVANCED: USE CASE PRIORITIZATION & GOVERNANCE CHECK

def prioritize_use_case(description):
    prompt = f"""
    Evaluate this Gen AI use case using:
    - Impact (High/Medium/Low)
    - Effort (High/Medium/Low)
    - Recommendation

    Use case:
    {description}
    """
    return ask_llm(prompt)


def governance_check(text):
    prompt = f"""
    Analyze this content for governance and risk:
    - Does it contain sensitive financial/audit data?
    - Risk Level (Low/Medium/High)
    - Should human review be required?

    Content:
    {text[:8000]}
    """
    return ask_llm(prompt)
