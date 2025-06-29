import PromptFunction as AI

import PromptFunction as AI

WORD = 'router'
FORBIDDEN_WORDS = ['internet', 'wifi', 'device', 'traffic']


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