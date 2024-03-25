#!/usr/bin/env python3
"""
Description: Wiener's Attack Implementation

This script performs Wiener's attack to factorize RSA modulus when the private exponent is too small.
It uses continued fraction expansion to approximate the private exponent and recover the factors.

Original Python 2 code by BalalaikaCr3w during Hack.lu CTF Quals 2014. Updated to Python 3, replaced
optparse() with argparse(), and xrange() to range(), updated syntax (e.g., print(), integer div, etc).

Date Created: Nov 26, 2014

Modified by: Jonathan Ennis
Date Modified: Mar 23, 2024
Version: 1.0
License: MIT License

Usage: wiener_attack.py -n <modulus> -e <public exponent>
"""
import argparse
from sympy import symbols, solve

def make_next_fraction(fraction):
    """
    Generates the next fraction in the continued fraction expansion.
    This function plays a crucial role in approximating the rational number that represents the private exponent.
    """
    a, b = fraction
    res = b // a
    a1 = b % a
    b1 = a
    return res, (a1, b1)

def make_continued_fraction(fraction):
    """
    Creates the continued fraction expansion of a rational number.
    Continued fraction expansions are essential in Wiener's attack as they allow us to approximate the private exponent.
    """
    a, b = fraction
    v = [0]
    while a != 1:
        r, fraction = make_next_fraction(fraction)
        a, b = fraction
        v.append(r)
    v.append(b)
    return v

def make_indexed_convergent(sequence, index):
    """
    Generates the indexed convergent from a continued fraction sequence.
    These convergents are used to iteratively approximate the private exponent from the continued fraction expansion.
    """
    a, b = 1, sequence[index]
    while index > 0:
        index -= 1
        a, b = b, sequence[index] * b + a
    return b, a

def make_convergents(sequence):
    """
    Generates all the convergents from a continued fraction sequence.
    This function provides a set of convergents, each of which is used to calculate potential values for the private exponent.
    """
    r = []
    for i in range(len(sequence)):
        r.append(make_indexed_convergent(sequence, i))
    return r

def solve_quadratic(a, b, c):
    """
    Solves the quadratic equation ax^2 + bx + c = 0.
    In Wiener's attack, this function is used to find potential values for the factors of the RSA modulus.
    """
    x = symbols('x')
    return solve(a * x ** 2 + b * x + c, x)

def wiener_attack(N, e):
    """
    Performs Wiener's attack to factorize RSA modulus.
    The attack involves iteratively approximating the private exponent using continued fraction expansion
    and solving quadratic equations to find potential factors of the RSA modulus.
    """
    conv = make_convergents(make_continued_fraction((e, N)))
    for frac in conv:
        k, d = frac
        if k == 0:
            continue
        phiN = ((e * d) - 1) // k
        roots = solve_quadratic(1, -(N - phiN + 1), N)
        if len(roots) == 2:
            p, q = roots[0] % N, roots[1] % N
            if p * q == N:
                return p, q

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', dest='n', help='modulus', type=int)
    parser.add_argument('-e', dest='e', help='public exponent', type=int)
    try:
        args = parser.parse_args()
        if args.n and args.e:
            p, q = wiener_attack(args.n, args.e)
            print("-p", p)
            print("-q", q)
            print("-e", args.e)
        else:
            parser.print_help()
            parser.error('n and e must be specified')
    except Exception as e:
        parser.print_help()
        parser.error(str(e))
