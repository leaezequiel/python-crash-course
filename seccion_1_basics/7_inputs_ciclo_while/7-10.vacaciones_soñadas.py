# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 13:08:15 2026

@author: lstivanello
"""

"""
7-10. Dream Vacation: Write a program that polls users about their dream vacation.
Write a prompt similar to If you could visit one place in the world, where
would you go? Include a block of code that prints the results of the poll.
"""
activo = True
destinos = []

while activo == True:
    destino = input('Ingrese destino deseado o basta para dejar de jugar....')
    if destino == "basta":
        activo = False
    else:
        if destino not in destinos:
            destinos.append(destino)
        else:
            print(f"{destino} es un lugar muy solicitado")

print(f"La gente quiere ir a: {destinos}")