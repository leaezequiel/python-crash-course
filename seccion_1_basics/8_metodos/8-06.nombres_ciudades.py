# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 08:21:01 2026

@author: lstivanello
"""

"""
8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the values
that are returned.
"""

def ciudad_pais(ciudad, pais):
    mensaje = (f"{ciudad}, {pais}")
    return mensaje

print(ciudad_pais('BA', 'Argentina'))
print(ciudad_pais('Berlin', 'Alemania'))
print(ciudad_pais('Bariloche', 'Argentina'))