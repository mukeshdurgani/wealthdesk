from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Access the Groq API key
groq_key = os.getenv("GROQ_API_KEY")
print("Groq API Key loaded:", groq_key[:6] + "...")