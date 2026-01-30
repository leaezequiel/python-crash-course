# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 12:31:46 2026

@author: lstivanello
"""
"""
5-2. More Conditional Tests: You don’t have to limit the number of tests you create
to 10. If you want to try more comparisons, write more tests and add them
to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
"""

#• Tests for equality and inequality with strings
nombre = 'Lean'
print('te llamas pepe?')
print((nombre == 'pepe'))

print('te llamas lean?')
print((nombre == 'lean'))

#• Tests using the lower() method
print('ah dejame probar con lower')
print(nombre.lower() =='lean' )

print('--numerico--')

#• Numerical tests involving equality and inequality, greater than and less
#than, greater than or equal to, and less than or equal to

jugadores_por_equipo = 11

print('Son 12 jugadores por equipo?')
print(jugadores_por_equipo==12)

print('son mas de 13?')
print(jugadores_por_equipo>13)

print('son menos de 12?')
print(jugadores_por_equipo<12)

print('son 10 o mas?')
print(jugadores_por_equipo>=10)

print('Son 11 o menos?')
print(jugadores_por_equipo<=11)

print('Son 22 jugadores en total')
print(jugadores_por_equipo*2==22)