import PromptFunction as AI

PROMPT = """Write me 5 only names of movies with Tom Hankes"""

print(AI.ask_gemini(PROMPT))

PROMPT = """Write just the names of the Movies"""

print(AI.ask_gemini(PROMPT))