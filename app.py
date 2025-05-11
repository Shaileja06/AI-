from dotenv import load_dotenv
import os

load_dotenv()  
import streamlit as st
from vector_utils import create_vector_from_pdf
from agent_runner import get_agent
import os

st.set_page_config(page_title="RAG-powered Multi-Tool Assistant")
st.title("RAG-powered Multi-Tool Assistant")

# Ensure API key is set
if "OPENAI_API_KEY" not in os.environ:
    st.error("OPENAI_API_KEY not found in environment. Please set it.")

uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file:
    st.success("Document uploaded successfully!")
    vectorstore = create_vector_from_pdf(uploaded_file)
    agent = get_agent(vectorstore)

    user_input = st.text_input("Ask a question about your document or general knowledge:")

    if user_input:
        with st.spinner("Processing..."):
            response = agent.run(user_input)
            st.markdown("### Answer")
            st.write(response)
            st.markdown("---")
            st.text("Routing logic and relevant steps are printed in terminal logs.")

