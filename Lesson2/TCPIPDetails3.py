import PromptFunction as AI

DATA ="""
A network sniffer captured a TCP packet originating from Source IP: 192.168.1.100,
destined for Destination IP: 10.0.0.300,
with a Source Port of 80321 and a Destination Port of 80
associated with the Application Name: FTTP
observed at the Physical Layer via Ethernet.
"""


PROMPT = f"""
Extract the IP V4 details of TCP/IP Layers of the user STATEMENT 
Extract the Physical Layer ,Source and Destination IP, Source and Destination PORT,  Application 
If nothing was mentioned, return NONE. Write it in one line .
make correlation with the data given like Destination PORT and application, and check the IP structure
Check as Network expert that the data given for each layer is correct on the knowledge of networking. if it incorrect write me the problem/error

Example result:
Physical : WiFi #
Source IP : 128.34.56.7 #
Destination IP :12.3.56.7 #
Source PORT : 4567 #
Destination PORT : 443 #
Application : HTTPS #


STATEMENT: {DATA}
TCP/IP:
"""

print(AI.ask_gemini(PROMPT))