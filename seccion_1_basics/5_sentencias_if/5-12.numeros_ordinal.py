# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 13:43:08 2026

@author: lstivanello
"""

"""
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as
1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if-elif-else chain inside the loop to print the proper ordinal ending
for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th
8th 9th", and each result should be on a separate line.
"""

numeros = list(range(1,10))
ordinal = []

for numero in numeros:
    numero_str = str(numero)
    if numero == 1:
        ordinal.append(numero_str+"st")
    elif numero == 2:
        ordinal.append(numero_str+"nd")
    elif numero == 3:
        ordinal.append(numero_str+"rd")
    else:
        ordinal.append(numero_str+"th")
        
for num_ordinal in ordinal:
    print(num_ordinal)