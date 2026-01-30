# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 12:50:16 2026

@author: lstivanello
"""

"""
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse
chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed
for the appropriate color alien.
"""

alien_color = 'gris'
mensaje= f'jugamos con el color {alien_color}'
print(mensaje)

if alien_color == 'verde':
    print('haz ganado 5 puntos')
elif alien_color == 'amarillo':
    print('haz ganado 10 puntos')
elif alien_color == 'rojo':
    print('haz ganado 15 puntos')
else:
    print('ese color es inusual, no se !')