# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 08:49:21 2026

@author: lstivanello
"""
"""
11-1. 
PARTE A
City, Country:
Write a function that accepts two parameters: a city name
and a country name. The function should return a single string of the form
City, Country, such as Santiago, Chile. Store the function in a module called
city_functions.py, and save this file in a new folder so pytest won’t try to run the
tests we’ve already written.


"""

def recibidor(ciudad, pais):
    ciudad = input('Ingrese nombre ciudad')
    pais = input('Ingrese país')

    mensaje = f"{ciudad.capitalize()} es una Ciudad de {pais.capitalize()}"
    print(mensaje)
    
recibidor()