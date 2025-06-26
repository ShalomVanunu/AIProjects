import PromptFunction as AI


def promt(context="",question=""):
    PROMPTChat = f"""
    Answer the Question below.
    
    Here is the conversation history : {context}
    
    Question : {question}
    
    Answer:
    """
    return PROMPTChat

def handle_conversation():
    context= ""
    print("Welcome to gemini ChatBot! , (type 'exit' to Quit) ")
    while True:
        user_input = input("You:")
        if user_input.lower() == 'exit':
            break
        result = AI.ask_gemini(promt(context,user_input))
        print(f"Bot : {result}")
        context += f"\nUser:{user_input}\nBot:{result}"

handle_conversation()
# Explain what is Electric CAR in a few words