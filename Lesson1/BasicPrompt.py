from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
# See more models at: https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash",
    contents="Explain in a sentence what is Electric CAR")

print(response.text)

