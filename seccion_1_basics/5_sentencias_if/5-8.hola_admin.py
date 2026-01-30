# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 13:20:05 2026

@author: lstivanello
"""

"""
5-8. Hello Admin: Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user.
• If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for
logging in again.
"""
usernames = ['mate','juli3p','admin','lmessi','icecube']

for user in usernames:
    if user == 'admin':
        print('Hola Admin, quieres un reporte de la situación actual?')
    else:
        mensaje = f'hola {user}, te doy la bienvenida'
        print(mensaje)