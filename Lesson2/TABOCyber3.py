import PromptFunction as AI

WORD = 'router'

prompt_template = f"""
Given a target word, return a list of 4-6 words that
identify the target word easily. Separate the words with a comma.
target word: {WORD}
identifying words: 
"""

FORBIDDEN_WORDS = AI.ask_gemini(prompt_template)
FORBIDDEN_WORDS = [word.strip() for word in FORBIDDEN_WORDS.split(",")]


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