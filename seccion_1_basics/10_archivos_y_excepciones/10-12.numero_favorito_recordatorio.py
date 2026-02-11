# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 13:43:44 2026

@author: lstivanello
"""

"""
10-12. Favorite Number Remembered:
Combine the two programs you wrote in Exercise 10-11 into one file. 
If the number is already stored, report the favorite number to the user.

 If not, prompt for the user’s favorite number and store it in a file. 
 
 Run the program twice to see that it works.
"""


from pathlib import Path
import json


path = Path ('num_favorito.json')


def levanta_archivo():
    try:
        content = path.read_text()
    except FileNotFoundError:
        pass
    else:
        numbers = json.loads(content)
        print(numbers)
    
def guarda_archivo():
    numero_favorito = input('Cual es tu numero favorito?')
    contents = json.dumps(numero_favorito)
    path.write_text(contents)
    print(f"se que tu favorito es {numero_favorito}")

if path.exists():
    levanta_archivo()
else: 
    guarda_archivo()
    
    
