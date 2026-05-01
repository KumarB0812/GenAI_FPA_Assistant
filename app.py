import streamlit as st
from utils import (
    extract_text,
    summarize,
    extract_risks,
    generate_report,
    prioritize_use_case,
    governance_check
)

st.set_page_config(page_title="Gen AI FP&A Assistant", layout="wide")

st.title("📊 Gen AI FP&A & Audit Assistant")

st.markdown("Upload a financial or audit document to analyze using Generative AI.")


# FILE UPLOAD (PDF/TXT SUPPORTED)

uploaded_file = st.file_uploader("Upload PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    text = extract_text(uploaded_file)

    st.success("Document loaded successfully!")

    # ANALYSIS BUTTON

    if st.button("Run Analysis"):
        with st.spinner("Analyzing document..."):

            st.subheader("📌 Executive Summary")
            st.write(summarize(text))

            st.subheader("⚠️ Key Risks & Issues")
            st.write(extract_risks(text))

            st.subheader("📄 Generated Business Report")
            st.write(generate_report(text))

            st.subheader("🛡️ Governance Check")
            st.write(governance_check(text))


# USE CASE PRIORITIZATION

st.markdown("---")
st.header("🧠 Gen AI Use Case Prioritization")

use_case = st.text_area("Describe a workflow/use case (e.g., 'Automate financial report summarization')")

if st.button("Evaluate Use Case"):
    if use_case:
        st.write(prioritize_use_case(use_case))
    else:
        st.warning("Please enter a use case description.")