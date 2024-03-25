"""
File: stopdroproll.py
Author: Jonathan Ennis
Date: 3/10/2024
Description: Solves the Stop Drop and Roll challenge. A 'very easy' (misc) challenge from
             Cyber Apocalypse 2024 (Hack the Box).
"""
from pwn import *

def play_game(host, port):
    context.log_level = "DEBUG"
    conn = remote(host, port)
    
    # Wait for the initial prompt
    print(conn.recvuntil("n)"))
    
    # Send 'y' to start the game
    print(conn.sendline("y"))
    
    while True:
        # Receive the game scenarios
        prompt = conn.recvuntil("?").decode('utf-8')
        print(prompt.strip())
        
        # Parse scenarios
        scenarios = prompt.strip().split(", ")
        
        # Determine the appropriate response for each scenario
        responses = []
        for scenario in scenarios:
            if "GORGE" in scenario:
                responses.append("STOP")
            elif "PHREAK" in scenario:
                responses.append("DROP")
            elif "FIRE" in scenario:
                responses.append("ROLL")
        
        # Send the responses
        conn.sendline("-".join(responses))
        
        # Check if the game is over
        if "Connection closed" in prompt:
            break
    
    # Close the connection
    conn.close()

if __name__ == "__main__":
    host = "94.237.57.161"
    port = 52645
    play_game(host, port)
