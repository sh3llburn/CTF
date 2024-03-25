"""
File: character.py
Author: Jonathan Ennis
Date: 3/10/2024
Description: Solves the Character challenge. A 'very easy' (misc) challenge from
             Cyber Apocalypse 2024 (Hack the Box).
"""
from pwn import *

def get_flag_character(host, port):
    conn = remote(host, port)
    
    # Initialize an empty flag
    flag = "HTB{"
    
    # Start with index 4
    index = 4
    
    # Loop to get each character of the flag
    while True:
        context.log_level = "DEBUG"
        # Send the index request
        conn.sendline(str(index))
        
        # Receive the character
        char_response = conn.recv().decode('utf-8').strip()
        char = char_response.split("\n")[0][-1]
        
        # Add the character to the flag
        flag += char
        print(flag)
        # Check if we reached the end of the flag
        if char == "}":
            break
        
        # Increment index for the next character
        index += 1
    
    # Close the connection
    conn.close()
    
    return flag

if __name__ == "__main__":
    host = "83.136.252.250"
    port = 31724
    flag = get_flag_character(host, port)
    print("Flag:", flag)
