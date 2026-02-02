# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 10:07:26 2026

@author: lstivanello
"""

"""
7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
"""



def gestor(edad):
    if edad <=2:
        print("Entras gratis")
    elif edad >= 3 and edad <= 12:
        print("Debes pagar $10")
    elif edad >= 13:
        print("Debes pagar 15")
        

while True:
    edad = input("Ingrese edad o escriba 'salir' para terminar")
    if edad == "salir":
        break
    else:
        entrada = int(edad)
        gestor(entrada)
        
        