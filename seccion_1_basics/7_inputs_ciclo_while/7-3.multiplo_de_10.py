# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 09:51:55 2026

@author: lstivanello
"""

"""
7-3. Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not.
"""


multiplo = int(input("Ingrese numero"))

if multiplo%10 == 0:
    print("Multiplo de 10")
else:
    print("No es multiplo de 10")