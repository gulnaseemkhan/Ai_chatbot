import streamlit as st
from PyPDF2 import PdfReader
import re

st.set_page_config(page_title="AI PDF Chatbot", layout="centered")

st.title("📄 AI Powered PDF Chatbot")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:

    # Read PDF
    pdf = PdfReader(uploaded_file)
    text = ""

    for page in pdf.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    st.success("PDF uploaded successfully!")

    # User Question
    question = st.text_input("Ask a question from the PDF")

    if question:

        st.subheader("Answer")

        # Split PDF text into sentences
        sentences = re.split(r'(?<=[.!?]) +', text)

        matched_sentences = []

        # Check matching words
        for sentence in sentences:
            for word in question.lower().split():
                if word in sentence.lower():
                    matched_sentences.append(sentence)

        # Remove duplicates
        matched_sentences = list(set(matched_sentences))

        if matched_sentences:
            for ans in matched_sentences[:5]:
                st.write("👉", ans)
        else:
            st.write("No related answer found in the PDF.")