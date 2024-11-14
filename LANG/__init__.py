from dotenv import load_dotenv,find_dotenv
import os

load_dotenv(find_dotenv())


GROQ_API_KEY=os.getenv("GROQ_API_KEY")
LANGCHAIN_API_KEY=os.getenv("LANGCHAIN_API_KEY")
TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")