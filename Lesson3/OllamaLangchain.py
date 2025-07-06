# Import OllamaLLM from the updated langchain_ollama package
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


template = """
Answer the question below.
Here is the conversation history: {context}
Question: {question}
Answer:
"""

# Initialize the Ollama LLM with the specified model (e.g., "llama2")
# Ensure that Ollama is running and the 'llama2' model is available on your system.
llm = OllamaLLM(model="mistral")
prompt = ChatPromptTemplate.from_template(template=template)

chain = prompt | llm

# Invoke the LLM with a prompt to tell a joke
result = chain.invoke({"context":"","question":"tell me about electric car in one sentence"})

print(result)

