# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 08:41:07 2026

@author: lstivanello
"""

"""
10-4. Guest: Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.
"""

from pathlib import Path

path = Path('invitado.txt')

nombre = input('ingrese nombre')


path.write_text(nombre)