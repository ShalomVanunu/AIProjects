import PromptFunction as AI
import json

DATA ="""
A network sniffer captured a TCP packet originating from Source IP: 192.168.1.100,
destined for Destination IP: 10.0.0.10,
with a Source Port of 54321 and a Destination Port of 80
associated with the Application Name: HTTP
observed at the Physical Layer via Ethernet.
"""


PROMPT = f"""
Extract the IP V4 details of TCP/IP Layers of the user STATEMENT 
Extract the Physical Layer ,Source and Destination IP, Source and Destination PORT,  Application 
If nothing was mentioned, return NONE. Write it in one line .
make correlation with the data given like Destination PORT and application, and check the IP structure
Check as Network expert that the data given for each layer is correct on the knowledge of networking. if it incorrect write NONE

Example of json format:
{{
  "Physical_Layer": "Ethernet",
  "Source_IP": "192.168.1.100",
  "Destination_IP": "10.0.0.5",
  "Source_Port": 54321,
  "Destination_Port": 80,
  "Application": "HTTP",
}}

STATEMENT: {DATA}
JSON:
"""
data = AI.ask_gemini(PROMPT)
#print(data)

cleaned_json = data.replace("```json", "").replace("```", "").strip()
print(cleaned_json)

data_json = json.loads(cleaned_json)
#print(data_json["Destination_IP"])
