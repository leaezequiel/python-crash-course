# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 12:23:14 2026

@author: lstivanello
"""

"""
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop through
the list of sandwich orders and print a message for each order, such as I made
your tuna sandwich. As each sandwich is made, move it to the list of finished
sandwiches. After all the sandwiches have been made, print a message listing
each sandwich that was made.
"""

ordenes_sandwich = ['atún', 'pavita', 'pastrami', 'j. crudo']

realizados = []

while ordenes_sandwich: #mientras haya algo en la lista ....

    sand_actual = ordenes_sandwich.pop() #remueve
    print(f"Se esta preparando el de {sand_actual.title()}")
    print("Realizado")
    realizados.append(sand_actual)
    
print(f"Total de la orden: {realizados}")