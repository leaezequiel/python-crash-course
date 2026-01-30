# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 09:41:34 2026

@author: lstivanello
"""

"""
4-5. Summing a Million: Make a list of the numbers from one to one million, and
then use min() and max() to make sure your list actually starts at one and ends
at one million. Also, use the sum() function to see how quickly Python can add
a million numbers.
"""

lista_al_millon = list (range(1, 1000001))

print(min(lista_al_millon))
print(max(lista_al_millon))
print(sum(lista_al_millon))