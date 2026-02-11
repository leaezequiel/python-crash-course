# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 13:24:22 2026

@author: lstivanello
"""

"""
10-11. Favorite Number: 
    Write a program that prompts for the user’s favorite number.
    Use json.dumps() to store this number in a file. 
    Write a separate program that reads in this value and prints the
    message “I know your favorite number! It’s _____.”
"""

from pathlib import Path
import json


numero_favorito = input('Cual es tu numero favorito?')

path = Path ('num_favorito.json')

contents = json.dumps(numero_favorito)
path.write_text(contents)


def levanta_archivo():
    try:
        content = path.read_text()
    except FileNotFoundError:
        pass
    else:
        numbers = json.loads(content)
        print(numbers)
    
levanta_archivo()