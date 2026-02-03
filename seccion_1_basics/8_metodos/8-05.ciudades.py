# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 08:17:44 2026

@author: lstivanello
"""

"""
8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.
"""

def describe_ciudad(nombre_ciudad, pais='No estoy seguro...'):
    print(f"{nombre_ciudad} es en {pais}")
    
describe_ciudad('Buenos Aires','Argentina')
describe_ciudad(nombre_ciudad = 'Berlin', pais = 'Alemania')
describe_ciudad('Ciudad del Cabo')
    