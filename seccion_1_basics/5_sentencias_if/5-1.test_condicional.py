# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 11:49:19 2026

@author: lstivanello
"""

"""
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.
"""
import random 
club = 'boca'
print('es tu club favorito boca? club == boca? yo digo que SI')
print(club == 'boca')

#con mayus
print('es tu club favorito Boca? club == Boca? yo digo que NO')
print(club == 'Boca')

#con otro club
print('es tu club favorito riber? club == riber? yo digo que NO')
print(club == 'riber')

"""
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.
"""
numero_favorito = 11

print('tu numero favorito es par?')
print((numero_favorito%2)== 0)

print('tu numero favorito es impar?')
print((numero_favorito%2)== 1)

for i in range (1,5): #aca hay 4 false
    print('tu numero favorito es ', i)
    print(i==numero_favorito)

#un intento aleatorio (del 10 al 19)
intento = random.randint(10,20)
print('es el numero mayor a ', intento)
print(intento<numero_favorito)

# un intento por multiplo
print('es multiplo de 11?')
print(numero_favorito%11==0)

for i in range (88,0,-11):
    print('es el ', i)
    print(numero_favorito==i)