# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 13:56:08 2026

@author: lstivanello
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