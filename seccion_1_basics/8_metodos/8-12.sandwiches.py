# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 10:04:08 2026

@author: lstivanello
"""
"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich
that’s being ordered. Call the function three times, using a different number
of arguments each time.
"""

def sandwichs (*items):
    ingredientes = []
    for item in items:
        ingredientes.append(item)
    print(ingredientes)
    return ingredientes
    
sandwichs('Queso')
sandwichs('Jamon','Queso')
sandwichs('Milanesa', 'Tomate', 'Queso')