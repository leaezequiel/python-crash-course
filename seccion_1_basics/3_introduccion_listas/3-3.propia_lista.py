# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 08:13:01 2026

@author: lstivanello
"""

"""
3-3. Your Own List: Think of your favorite mode of transportation, such as a 
motorcycle or a car, and make a list that stores several examples. Use your list 
to print a series of statements about these items, such as “I would like to own a 
Honda motorcycle.”
"""
medios_transporte = ['moto', 'colectivo', 'ecobici', 'caminando', 'auto']
apto_lluvia = [medios_transporte[1], medios_transporte[4]]
mensaje = f"Cuando llueve voy al trabajo en {apto_lluvia}"
print(mensaje)