# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 10:02:13 2026

@author: lstivanello
"""

"""
8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() 
with a copy of the list of messages. After calling the function, print both of your lists to show
 that the original list has retained its messages.
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
        
enviar_mensajes(mensajes[:])
print(f"Chequeo de mensaje original: {mensajes}")
