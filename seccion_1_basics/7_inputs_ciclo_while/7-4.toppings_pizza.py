# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 09:56:24 2026

@author: lstivanello
"""

"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping, print
a message saying you’ll add that topping to their pizza.
"""
topping = ""
toppings = []

while topping != "quit":
    topping = input("ingrese addicional")
    if topping != "quit":
        toppings.append(topping)
        print(f"Se agrego {topping}!")
    
print(f"Se agregaron: {toppings}")