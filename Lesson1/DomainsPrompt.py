from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
# See more models at: https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash",
    contents="""Act like a cybersecurity expert.
     I'll give you the domain name of a website,
    just write me the names of five identical websites that could be phishing.
    onl the domains name!
    the domain of clothes web online shop is :hoodies
    """)

print(response.text)


