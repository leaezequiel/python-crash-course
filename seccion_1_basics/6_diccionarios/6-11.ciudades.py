# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 08:54:47 2026

@author: lstivanello
"""

"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information
you have stored about it.
"""

ciudades = {'buenos aires': {'pais':'arg','poblacion':5000000,'fact':'mejor ciudad del mundo'},
            'madrid': {'pais':'esp','poblacion':7000000, 'fact':'lleno de gente'},
            'nuevo asgard' : {'pais':'dinamarca', 'poblacion':1000,'fact':'no existe'}
    }

for k, v in ciudades.items():
    print(f"{k.capitalize()} se que queda en {v['pais'].capitalize()}, es habitada por {v['poblacion']} habitantes y algo curioso: {v['fact']}")