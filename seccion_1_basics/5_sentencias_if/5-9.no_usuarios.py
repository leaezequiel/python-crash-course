# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 13:27:37 2026

@author: lstivanello
"""

"""
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message
is printed.
"""

usernames = ['mate','juli3p','admin','lmessi','icecube']


if usernames:
    for user in usernames:
        if user == 'admin':
            print('Hola Admin, quieres un reporte de la situación actual?')
        else:
            mensaje = f'hola {user}, te doy la bienvenida'
            print(mensaje)
else:
    print("No hay usuarios en la lista")
    
print('---vacio lista---')
del usernames
usernames = []

if usernames:
    for user in usernames:
        if user == 'admin':
            print('Hola Admin, quieres un reporte de la situación actual?')
        else:
            mensaje = f'hola {user}, te doy la bienvenida'
            print(mensaje)
else:
    print("No hay usuarios en la lista")