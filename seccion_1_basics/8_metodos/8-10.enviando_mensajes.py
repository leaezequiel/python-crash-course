# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 09:54:10 2026

@author: lstivanello
"""

"""
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
Write a function called send_messages() that prints each text message and moves 
each message to a new list called sent_messages as it’s printed. After calling the function,
 print both of your lists to make sure the messages were moved correctly.
"""

mensajes = ['dale dale dale Bo', 'Jugadores... la @#(923 de su madre', 'Cuando vas a la cancha... vas con el patrullero']
enviados = []

"""def mostrar_mensajes(lista):
    for i in lista:
        print(i)
 """
        
def enviar_mensajes(lista):
    while lista:
        actual = lista.pop()
        enviados.append(actual)
        print(f"Se envio: {enviados}")
        
enviar_mensajes(mensajes)
print(f"Chequeo de vacio: {mensajes}")