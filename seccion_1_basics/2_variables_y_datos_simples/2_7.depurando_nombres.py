# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 09:46:38 2026

@author: lstivanello
"""

"""
2-7. Stripping Names: Use a variable to represent a person’s name, and 
include some whitespace characters at the beginning and end of the name. 
Make sure you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed. 
Then print the name using each of the three stripping functions, lstrip(), 
rstrip(), and strip().
""" 

nombre = " Leandro Ezequiel "
print("Con la t: Leandro\t Ezequiel")
print("Con la n: Leandro\n Ezequiel")
print("-", nombre, "-")
print(nombre.lstrip())
print(nombre.rsplit())
print(nombre.strip())