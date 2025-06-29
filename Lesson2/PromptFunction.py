from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")


MODEL = "gemini-2.0-flash-lite"
client = genai.Client(api_key=api_key)

def ask_gemini(request: str) -> str:
    response = client.models.generate_content(
        model=MODEL,
        contents=request,
        config=types.GenerateContentConfig(
            max_output_tokens=10000,
            temperature=0.9)
        )
    return response.text
