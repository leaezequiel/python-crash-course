# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 12:18:22 2026

@author: lstivanello
"""

'''
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3,
and write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned 5
points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned
10 points.
Write one version of this program that runs the if block and another that
runs the else block.

'''

alien_color = 'rojo'
mensaje= f'jugamos con el color {alien_color}'
print(mensaje)

if alien_color == 'verde':
    print('haz ganado 5 puntos')
else:
    print('haz ganado 10 puntos')


alien_color = 'verde'
mensaje= f'jugamos con el color {alien_color}'
print(mensaje)

if alien_color == 'verde':
    print('haz ganado 5 puntos')
else:
    print('haz ganado 10 puntos')