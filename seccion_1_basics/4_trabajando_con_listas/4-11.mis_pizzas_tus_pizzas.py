# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 10:28:03 2026

@author: lstivanello
"""
"""
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56).
Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the
following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas
are:, and then use a for loop to print the first list. Print the message My
friend’s favorite pizzas are:, and then use a for loop to print the second list.
Make sure each new pizza is stored in the appropriate list.
"""
pizzas = ['roquefort', 'napolitana','anchoas']
pizzas_amigos = pizzas[:]

pizzas.append('jamon y morron')

pizzas_amigos.append('margarita')

#defini una funcion para ahorrar tiempo, no es la idea pero ya me aburri de definir fors...
def imprime_lista(lista):
    for i in lista:
        print(i)
    
print('Mis pizzas favoritas son: ')
imprime_lista(pizzas)

print('Las de mi amigui son:')
imprime_lista(pizzas_amigos)