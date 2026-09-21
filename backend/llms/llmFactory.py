from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_xai import ChatXAI
from langchain_groq import ChatGroq
from utils.logger import logging
import os
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
GROQ_API_KEY=os.getenv("GROQ_API_KEY")
GROK_API_KEY=os.getenv("GROK_API_KEY")

logging.info(f"API keys loaded successfully")

class LLMFactory:

    @staticmethod
    def gemini(model:str="gemini-3.5-flash"):

        return ChatGoogleGenerativeAI(
            model=model,
            temperature=0.2,
            api_key=GOOGLE_API_KEY,
            verbose=True
        )

    @staticmethod
    def grok(model:str="x-ai/grok-4.1-fast:free"):
        return ChatXAI(
            model=model,
            temperature=0.2,
            verbose=True,
            api_key=GROK_API_KEY,
        )
    
    @staticmethod
    def groq(model:str="llama-3.3-70b-versatile"):
        return ChatGroq(
            model=model,
            temperature=0.2,
            verbose=True,
            api_key=GROQ_API_KEY,
        )

    @staticmethod
    def get_all_providers():
        """Return available LLM providers, skipping any whose API key is missing."""
        providers = []
        if GROQ_API_KEY:
            providers.append(LLMFactory.groq())
        if GOOGLE_API_KEY:
            providers.append(LLMFactory.gemini())
        if GROK_API_KEY:
            providers.append(LLMFactory.grok())
        if not providers:
            raise Exception(
                "No LLM provider configured. Set at least one of "
                "GOOGLE_API_KEY, GROQ_API_KEY, or GROK_API_KEY in the environment."
            )
        return providers