# RAG-Powered Multi-Agent Q&A Assistant

This project implements a simple yet powerful Retrieval-Augmented Generation (RAG) based knowledge assistant using LangChain, FAISS, Groq LLM (LLaMA 3), and Streamlit. It enables users to upload PDFs and ask questions, leveraging both document retrieval and general-purpose tools like a calculator and Wikipedia search.

---

## ✨ Features

- 🔍 RAG-based retrieval from user-uploaded PDF documents.
- 🤖 Natural language generation using Groq's LLaMA 3.1 model.
- 🧠 Agentic decision-making with tool routing:
  - "calculate" → math tool
  - "define" → Wikipedia
  - Else → document-based RAG + LLM
- 📄 Document chunking and vector indexing via FAISS.
- 🖥️ Interactive web app using Streamlit.
- 📜 Execution trace logs to debug or understand agent routing.

---

## 📁 Project Structure

| File            | Purpose                                                       |
|-----------------|---------------------------------------------------------------|
| app.py          | Streamlit frontend for uploading PDFs and asking questions    |
| vector_utils.py | Ingests and chunks PDFs, builds FAISS vector index            |
| tools.py        | Custom tools (math evaluator & Wikipedia search)              |
| agent_runner.py | Initializes agent with tools and routes logic accordingly     |
| .env            | Stores environment variables (e.g., API keys)                 |
| README.md       | Project documentation (this file)                             |

---

## 🛠️ Setup Instructions

### 1. Clone the Repository


git clone https://github.com/your-username/rag-multi-agent-assistant.git
cd rag-multi-agent-assistant

2. Create and Activate a Virtual Environment

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

4. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Sample requirements.txt:

text
langchain
langchain-groq
openai
streamlit
faiss-cpu
wikipedia
python-dotenv

4. Add Environment Variables
Create a .env file in the root directory:


OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key

🚀 Running the App

streamlit run app.py

Upload a PDF and ask questions like:

"What are the specs of the product?"

"Calculate 12 * (4 + 3)"

"Define artificial intelligence"

🧠 Architecture Overview
PDF uploaded → split into chunks (500 chars) with 50 overlap

FAISS vector store built from chunk embeddings (OpenAI)

LangChain retriever fetches top-3 relevant chunks

Agent routes based on keyword:

calculator tool

Wikipedia tool

else: retrieval → Groq LLM (RAG)

Decision steps and retrieved docs are printed in terminal logs

✅ Agentic Logic Example
Query: "Define computer vision"

Keyword match: "define"

Routed to: Wikipedia Tool

Answer returned: Summary from Wikipedia

Query: "What’s the refund policy?"

No tool keyword detected

Routed to: RAG → Groq LLM

Top 3 relevant chunks retrieved from PDF

Answer generated from retrieved context

📌 Notes
Ensure your PDF is clean and readable (non-scanned preferred).

Wikipedia and eval are used via LangChain tools. Wrap securely for production use.
