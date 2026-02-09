# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 14:22:48 2026

@author: lstivanello
"""

"""
9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""

from random import randint

class Dado:
    def __init__(self, lados = 6):
        self.lados = lados 
        
    def tirar_dados(self):
        numero = randint(1, self.lados)
        print(numero)


#Make a 6-sided die and roll it 10 times.
d6 = Dado()
d6.tirar_dados()
contador = 0
while contador != 10:
    d6.tirar_dados()
    contador += 1

#Make a 10-sided die and a 20-sided die. Roll each die 10 times.
d10 = Dado(10)
d10.tirar_dados()

contador = 0
while contador != 10:
    d10.tirar_dados()
    contador += 1
    
#20 lados:
d20 = Dado(20)
d20.tirar_dados()

contador = 0
while contador != 10:
    d10.tirar_dados()
    contador += 1