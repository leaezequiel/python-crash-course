# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 07:57:45 2026

@author: lstivanello
"""

"""
6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.
"""
rios = {
        'parana':'argentina',
        'amazonas':'brasil',
        'missisipi':'eeuu'}

#primera consigna
for k, v in rios.items():
    print(f"-Rio {k.capitalize()} se encuentra en {v.capitalize()}.\n")
print("-----")        
#segunda consigna:
print("Rios:")
for k in rios.keys():
    print(f"{k.capitalize()}")
print("-----")
#tercera consigna:
print("Países")
for v in rios.values():
    print(f"{v.capitalize()}")