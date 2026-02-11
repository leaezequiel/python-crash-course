# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 10:34:17 2026

@author: lstivanello
"""
"""
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-7 to fail silently if either file is missing
"""
from pathlib import Path

listas = ['otra_prueba.txt','perros.txt', 'gatos.txt','prueba.txt']

def muestra_contenido(path):
    try:
        content = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(content)

for lista in listas:
    path = Path(lista)
    muestra_contenido(path)

