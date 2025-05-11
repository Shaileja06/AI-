from langchain.agents import tool
import wikipedia

@tool
def math_tool(query: str) -> str:
    """Evaluates mathematical expressions."""
    try:
        return str(eval(query))
    except Exception as e:
        return f"Error: {str(e)}"

@tool
def wiki_tool(topic: str) -> str:
    """Fetches a summary from Wikipedia."""
    try:
        return wikipedia.summary(topic, sentences=2)
    except Exception as e:
        return f"Error: {str(e)}"
