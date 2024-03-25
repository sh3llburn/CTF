#!/usr/bin/env python3
"""
Description: Convert Hexadecimal Modulus to Integer. This script converts a hexadecimal representation 
of an RSA modulus into its corresponding integer value.

The modulus is typically represented in hexadecimal format in RSA key files, converting it
into an integer is required for various cryptographic operations.

Author: Jonathan Ennis
Date Created: Mar 20, 2024
Version: 1.0
License: MIT License
Usage: python get_modulus.py
"""

# Hexadecimal representation of the modulus
modulus_hex = """
48:e8:f0:19:5d:8c:7b:0a:f1:4b:7f:ae:1b:d9:f8:
e4:08:77:44:8e:66:44:e9:f5:83:cd:76:57:d2:36:
5c:7f:83:51:99:08:e1:1f:6e:41:35:bb:f7:6a:76:
b9:80:cc:d1:e6:99:43:dd:39:f5:3d
"""

# Remove whitespace and colon characters
modulus_hex = "".join(modulus_hex.split()).replace(":", "")

# Convert hexadecimal string to integer
modulus_int = int(modulus_hex, 16)

print("Integer value of the modulus:")
print(modulus_int)
