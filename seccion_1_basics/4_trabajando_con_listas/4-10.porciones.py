# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 10:18:03 2026

@author: lstivanello
"""

"""
4-10. Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a
slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to
print the last three items in the list
"""

varios_tres = list(range(3,60,3))
print(varios_tres)

primeros_tres=varios_tres[:3]
print(primeros_tres)

ultimos_tres=varios_tres[-3:]
print(ultimos_tres)

print(len(varios_tres))
mitad = varios_tres[9:12]
print(mitad)