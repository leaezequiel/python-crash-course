# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 08:43:46 2026

@author: lstivanello
"""

"""
10-5. Guest Book: Write a while loop that prompts users for their name.
 Collect all the names that are entered, and then write these names to a file 
 called guest_book.txt. Make sure each entry appears on a new line in the file.
"""

from pathlib import Path

path = Path('lista_invitados.txt')


nombres = []

while True:
    nombre = input('ingrese nombre o ingrese "SALIR" para salir').strip()
    #EVALUA EL SALIR LUEGO DE PASARLO A MAYUS
    if nombre.upper() == "SALIR":
        print("Gracias por usar archivo")
        break
    
    if nombre:
        nombres.append(nombre)

path.write_text('\n'.join(nombres) +'\n')