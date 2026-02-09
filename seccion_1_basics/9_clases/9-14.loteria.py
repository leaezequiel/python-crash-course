# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 14:37:23 2026

@author: lstivanello
"""

"""
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 numbers or letters from the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.
"""
from random import sample
 
pool = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E']

ganadores = sample(pool, 4)

mi_ticket = ['E', 3, 9, 'A']

print(f"Los numeros ganadores son ... {ganadores}")

for ticket in mi_ticket:
    if ticket in ganadores:
        print(f"Felicidades... {ticket} es uno de los ganadores")
    else:
        print(f"{ticket} no salio")
    
    
