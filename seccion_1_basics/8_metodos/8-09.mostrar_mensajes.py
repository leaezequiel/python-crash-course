# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 09:19:46 2026

@author: lstivanello
"""

"""
8-9. Messages: Make a list containing a series of short text messages.
 Pass the list to a function called show_messages(), which prints each text message.
"""

mensajes = ['dale dale dale Bo', 'Jugadores... la @#(923 de su madre', 'Cuando vas a la cancha... vas con el patrullero']

def mostrar_mensajes(lista):
    for i in lista:
        print(i)
        
mostrar_mensajes(mensajes)