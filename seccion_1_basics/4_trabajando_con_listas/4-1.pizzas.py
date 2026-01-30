# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 08:22:45 2026

@author: lstivanello
"""

"""
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza,
instead of printing just the name of the pizza. For each pizza, you should
have one line of output containing a simple statement like I like pepperoni
pizza.
• Add a line at the end of your program, outside the for loop, that states
how much you like pizza. The output should consist of three or more lines
about the kinds of pizza
"""

pizzas = ['roquefort', 'napolitana','anchoas']

for pizza in pizzas:
    mensaje= f'Me encanta la pizza de {pizza}'
    print(mensaje)
    
print('Basicamente soy un fanatico pizzero')