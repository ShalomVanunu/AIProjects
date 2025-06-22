from certifi import contents
from google import genai
import os
from dotenv import load_dotenv

# import API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

list_responses = ""


def create_prompt(prompt):
    return f"""
    answer the question below.

    Here is the conversation history : {list_responses}

    answer the question {prompt}

    """


while True:
    # Prompt
    prompt = input(" Enter Prompt")
    prompt = create_prompt(prompt)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt)

    print(response.text)
    list_responses += response.text + "\n"

