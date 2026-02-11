# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 10:13:00 2026

@author: lstivanello
"""

"""
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt.
 Store at least three names of cats in the first file and three names of dogs in the second file. 
 Write a program that tries to read these files and print the contents of the file to the screen.
 Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block executes properly.
"""

from pathlib import Path

listas = ['otra_prueba.txt','perros.txt', 'gatos.txt','prueba.txt']

def muestra_contenido(path):
    try:
        content = path.read_text()
    except FileNotFoundError:
        print(f"No se encontro {path}")
    else:
        print(content)

for lista in listas:
    path = Path(lista)
    muestra_contenido(path)


