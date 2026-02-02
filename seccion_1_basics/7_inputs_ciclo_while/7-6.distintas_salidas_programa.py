# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 10:28:22 2026

@author: lstivanello
"""

"""
7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do
each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.

**El ejercicio de cine ya lo hice con ese formato, voy a ir por el de la pizza:

"""

topping = ""
toppings = []

"""
#• Use a conditional test in the while statement to stop the loop.
while topping != "quit":
    topping = input("ingrese addicional").strip().lower()
    if topping != "quit":
        toppings.append(topping)
        print(f"Se agrego {topping}!")
    
print(f"Se agregaron: {toppings}")
"""

"""
#• Use an active variable to control how long the loop runs.
activo = True #Flag

while activo:
    topping = input("ingrese addicional").strip().lower()
    if topping == "quit":
        activo = False
    else:
        toppings.append(topping)
        print(f"Se agrego {topping}!")
    
print(f"Se agregaron: {toppings}")
"""
#• Use a break statement to exit the loop when the user enters a 'quit' value.
while True:
    topping = input("ingrese addicional").strip().lower()
    if topping == "quit":
        break
    else:
        toppings.append(topping)
        print(f"Se agrego {topping}!")
    
print(f"Se agregaron: {toppings}")
    