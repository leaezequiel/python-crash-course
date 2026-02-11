# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 13:06:26 2026

@author: lstivanello
"""

from pathlib import Path


contents = "Me encanta programar.\n"
contents += "Me encanta la pizza.\n"
contents += "Me gusta andar en bici.\n"

path = Path('programando.txt')
path.write_text(contents) #escribe arriba de lo anterior


