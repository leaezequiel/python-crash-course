# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 12:26:19 2026

@author: lstivanello
"""

"""
8-14. Cars: Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
    
car = make_car('subaru', 'outback', color='blue', tow_package=True)


Print the dictionary that’s returned to make sure all the information was
stored correctly.
"""

def auto_nuevo(fabricante, modelo, **items):
    
    auto = {
        'fabricante' : fabricante ,
        'modelo' : modelo
        }
    
    auto.update(items)
    print(auto)
    return auto

auto_nuevo('Toyota','Etios')
auto_nuevo('Toyota', 'Corolla', anio = 2020)
auto_nuevo('Fiat','Cronos', anio = 2026, color = 'rojo')
