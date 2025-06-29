import PromptFunction as AI
import random

prompt = """We are playing a game where someone needs to
guess a word I’m thinking about. Suggest 5 different words from Cyber subject like 
Network Devices as router , IPv4, Web, Encryption like TLS etc.
Respond as a text with comma separated list.
target only words: """


WORD = AI.ask_gemini(prompt)
print(random.choices(WORD.split(",")))


prompt_template = f"""
Given a target word, return a list of 4-6 words that
identify the target word easily. Separate the words with a comma.
target word: {WORD}
identifying words: 
"""

FORBIDDEN_WORDS = AI.ask_gemini(prompt_template)
FORBIDDEN_WORDS = [word.strip() for word in FORBIDDEN_WORDS.split(",")]
print(FORBIDDEN_WORDS)

PROMPT = f"""
You are a participant in a game where I need to guess a  
TARGET_WORD you describe in a sentence or two.  
You cannot mention the TARGET_WORD or any of the  
additional forbidden words.  

TARGET_WORD: {WORD}  
additional forbidden words: {FORBIDDEN_WORDS}  
description:
"""

print(AI.ask_gemini(PROMPT))