from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain.agents import AgentExecutor, create_react_agent, tool
import Tools


# Load the Ollama model (ensure the desired model is installed and running)
llm = OllamaLLM(model="llama3.1:8b") # Replace 'llama2' with your desired model


prompt_template = PromptTemplate.from_template("""
You are an expert AI cybersecurity agent whose role is to analyze email messages and determine if they are a phishing attack.
Use your judgment, and in doing so, you have access to the following tools:

{tools}

To use a tool, use the following format:

1.  **Thought:** Analyze the email content. Look for spelling errors, unusual requests (like personal details, passwords), threats, unrealistic promises, and an urgent or threatening tone.
2.  **Action:** the action to take, should be one of {tool_names}
3.  **Thought:** For each extracted link, use the 'check_url_reputation' tool to check its reputation.
4.  **Thought:** Summarize all findings (from the text and the tools) and draw conclusions. Does the email appear to be a phishing attack? Justify your conclusion in detail.
5.  **Final Answer:** Present your final conclusion (Is this phishing: Yes/No/Uncertain) and a clear recommendation to the user.

For each email, analyze the content and the links within it.

Email content to analyze:
{input}

{agent_scratchpad}
""")

# Define the tools available to the agent
tools = [Tools.extract_urls_from_text, Tools.check_url_reputation]

# Create the Agent using ReAct
agent = create_react_agent(llm, tools, prompt_template)

# Create the Agent Executor
phishing_detection_agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=10 # Limit the number of iterations to prevent infinite loops
)

#
# SMS_1 = """
# 6 כביש
# אזהרה: יש לשלם 12.90
# ₪ הפרש תשלום באופן
# מיידי כדי למנוע כפל
# סכום/הליכים
# משפטיים/אגרות
# נוספות: http://kvish6.click/kvish6
# """
# result1 = phishing_detection_agent_executor.invoke({"input":SMS_1})
# print(f" Result Summary Check :{result1['output']}")

SMS_2 ="""

    שלום
זיהינו פעילויות חריגות בכרטיס האשראי שלך. על מנת להגן עליך בוצעה חסימה זמנית של הכרטיס.
להחזרת הכרטיס לפעילות
https://t.co/t6MD4D73Ma
    
    """
result2 = phishing_detection_agent_executor.invoke({"input":SMS_2})
print(f" Result Summary Check :{result2['output']}")
