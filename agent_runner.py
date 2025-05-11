from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env into environment
from langchain.agents import initialize_agent, Tool
from langchain_groq import ChatGroq
from tools import math_tool, wiki_tool
import re

def get_agent(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    def rag_tool(query: str) -> str:
        """Retrieves relevant information from uploaded documents."""
        docs = retriever.get_relevant_documents(query)
        context = "\n".join([doc.page_content for doc in docs])
        print("[RAG] Retrieved Context:\n", context)
        return context

    def router_tool(query: str) -> str:
        # Route based on keywords
        print("[Router] Received Query:", query)
        if any(word in query.lower() for word in ["calculate", "eval", "what is", "solve"]):
            print("[Router] Routing to: Calculator")
            return math_tool.run(query)
        elif any(word in query.lower() for word in ["define", "who is", "what is"]):
            print("[Router] Routing to: Wikipedia")
            return wiki_tool.run(query)
        else:
            print("[Router] Routing to: RAG Document Retriever")
            context = rag_tool(query)
            return llm.predict(context + "\n\nAnswer the question: " + query)

    # Dummy LLM for routing use, real LLM for RAG handled in router_tool
    llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

    tools = [
        Tool(name="SmartRouter", func=router_tool, description="Decides the best method to answer a question."),
    ]

    agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
    return agent
