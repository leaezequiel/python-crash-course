# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 09:49:21 2026

@author: lstivanello
"""

"""
7-2. Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message saying
they’ll have to wait for a table. Otherwise, report that their table is ready.
"""

comensales = int(input("Ingrese cantidad de comensales"))

if comensales > 8:
    print("Lo siento, hay una demora. Debe esperar")
else:
    print("Aquí esta su mesa dispinible")
    