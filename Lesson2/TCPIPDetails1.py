import PromptFunction as AI

DATA ="""
A network sniffer captured a TCP packet originating from Source IP: 192.168.1.100,
 destined for Destination IP: 10.0.0.5,
  with a Source Port of 54321 and a Destination Port of 80
  associated with the Application Name: FTTP,
  observed at the Physical Layer via Ethernet.
"""


PROMPT = f"""
Extract the IP V4 details of TCP/IP Layers of the user
STATEMENT in one line. Extract the Physical Layer ,Source and Destination IP, Source and Destination PORT,  Application Layer
for each TCP/IP Layer.
If nothing was mentioned, return NONE. 
STATEMENT: {DATA}
TCP/IP:
"""

print(AI.ask_gemini(PROMPT))

