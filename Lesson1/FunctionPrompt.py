from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

def ask_gemini(request: str) -> str :
    response = client.models.generate_content(
        #gemini-2.5-flash-preview-05-20
        #gemini-2.0-flash
        model="gemini-2.0-flash", #
        contents=request,
        config=types.GenerateContentConfig(
            max_output_tokens=50,
            temperature=0
        )
    )
    return response.text



