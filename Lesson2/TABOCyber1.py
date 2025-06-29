import PromptFunction as AI

PROMPT = """
You are a participant in a game where I need to guess a  
TARGET_WORD you describe in a sentence or two.  
You cannot mention the TARGET_WORD or any of the  
additional forbidden words.  

TARGET_WORD: 'router'  
additional forbidden words: internet, wifi, device, traffic  
description:
"""

print(AI.ask_gemini(PROMPT))