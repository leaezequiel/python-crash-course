# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 07:47:11 2026

@author: lstivanello
"""

"""
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When
you’re sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output.
Ya lo habia hecho con ese formato. No obstante se agregan mas palabras al glosario para confirmar su funcionamiento.
"""

glosario = {'variable':'espacio de memoria asignado',
            'clase':'un paradigma de programación',
            'int':'numero entero',
            'metodo':'forma de definir una serie de pasos logicos',
            'string':'texto',
            'identado':'espacio que delimita bloques de codigo',
            'ciclo for':'ciclo que se ejecuta una n cantidad de veces',
            'ciclo while':'ciclo que se ejecuta hasta que se cumpla x condición',
            'Python crash course':'librazo para aprender',
            'git':'forma de gestion de versiones',
            }

for k,v in glosario.items():
    print(f"-{k.capitalize()}: {v}.\n")