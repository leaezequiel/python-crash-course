# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 08:31:22 2026

@author: lstivanello
"""

"""
9-15. Lottery Analysis: You can use a loop to see how hard it might be to win 
the kind of lottery you just modeled. Make a list or tuple called my_ticket. 
Write a loop that keeps pulling numbers until your ticket wins. 
Print a message reporting how many times the loop had to run to give you a winning ticket.
"""

from random import sample
 
pool = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E']

ganadores = sample(pool, 4)

mi_ticket = ['E', 3, 9, 'A']

intentos = 0

while mi_ticket != ganadores:
    ganadores = sample(pool, 4)
    intentos += 1
    
print("Se necesitaron ...", intentos)
    