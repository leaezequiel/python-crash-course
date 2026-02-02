# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 12:37:33 2026

@author: lstivanello
"""

"""
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.
"""

ordenes_sandwich = ['atún', 'pavita', 'pastrami', 'j. crudo', 'pastrami', 'arroz yamani', 'pastrami', 'atún']
sand_terminados = []

print("Hola, lamentamos informar que no tenemos mas pastrami :(")

#Chequeo si se encuentra PASTRAMI en la cola de ordenes
while 'pastrami' in ordenes_sandwich:
    ordenes_sandwich.remove('pastrami')
    
while ordenes_sandwich: #mientras haya sand. en la fila...
    sand_actual = ordenes_sandwich.pop(0) #borramos de listado
    print(f"Se esta preparando el de {sand_actual.title()}") #mostramos su preparación
    print("Realizado") 
    sand_terminados.append(sand_actual) #agrega a realizado
    
print(sand_terminados) #chequeo final