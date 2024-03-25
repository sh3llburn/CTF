#!/usr/bin/env python3
"""
Description: 
Factorize RSA Modulus into Prime Factors

This script factorizes an RSA modulus into its prime factors using the sympy library.

RSA encryption relies on the product of two large prime numbers for its security. This script
determines the prime factors of the RSA modulus, which is used for certain cryptographic operations.

Author: Jonathan Ennis
Date Created: Mar 22, 2024
Version: 1.0
License: MIT License

Usage: python factorize_modulus.py
"""
from sympy import factorint

# Integer value of the modulus goes here
modulus_int = 207006830488235668671955689390815624796833363161842587562758966652474780634716637447867252305688653008916026906416134119860202636965181

# Factorize the modulus to obtain the prime factors (p and q)
factors = factorint(modulus_int)

# Extract prime factors p and q
p, q = factors.keys()

print("Prime factor p:", p)
print("Prime factor q:", q)
