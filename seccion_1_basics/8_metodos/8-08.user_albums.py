# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 09:02:58 2026

@author: lstivanello
"""

"""
8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop 
that allows users to enter an album’s artist and title. Once you have that information, 
call make_album() with the user’s input and print the dictionary that’s created.
Be sure to include a quit value in the while loop.
"""

def hacer_album(artista, nombre_album, n_canciones = None):
    album = {'artista':artista, 'album':nombre_album}
    if n_canciones is not None:
        album['canciones'] = n_canciones #asi asigna
    return album
    
bandera = True

while bandera:
    salida = input('Ingrese artista y album para agregar, sino salida si quiere salir')
    if salida == "salida":
        bandera = False
    else:
        hacer_album()
    