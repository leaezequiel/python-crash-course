# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 09:49:12 2026

@author: lstivanello
"""

"""
4-8. Cubes: A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube.

4-9. Cube Comprehension: Use a list comprehension to generate a list of the first
10 cubes.
"""
#4.8:
    
#Mi solucion del 4.8:
lista = list(range(1,11))
for elemento in lista:
    lista[elemento-1] = elemento**3
print(lista)
print("--------")

#Solucion sugerida x IA:
cubos = [] #define lista vacia

for n in range (1,11):#calcula los cubos y los va asignando a la lista vacia
    cubos.append(n**3)
    
for c in cubos:#imprime para verificar si esta correcto
    print(c) 
    
#4.9:
cubos = [valor**3 for valor in range(1,11)]
#define lista = [valor*accion a realizar FOR valor in rango(x,y)]
print(cubos)