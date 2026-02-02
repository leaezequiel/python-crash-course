# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 08:19:30 2026

@author: lstivanello
"""

"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make
two new dictionaries representing different people, and store all three dictionaries
in a list called people. Loop through your list of people. As you loop through
the list, print everything you know about each person.
"""
aang = {'primer_nombre':'Aang','apellido':'pies ligeros','edad':12,
        'ciudad_residencia':'nomade'}
toph = {'primer_nombre':'Toph','apellido':'Beifong','edad':10,
        'ciudad_residencia':'Ba Sing See'}
katara = {'primer_nombre':'katara','apellido': 'agua','edad':11,
        'ciudad_residencia':'tribu agua del sur'}
zoka = {'primer_nombre':'Zoka','apellido':'maestro del boomerang','edad':14,
        'ciudad_residencia':'tribu agua del sur'}

equipo_avatar = [aang, toph, katara, zoka]

for integrante in equipo_avatar:
    for k, v in integrante.items():
        print(k, v)
    print("----")