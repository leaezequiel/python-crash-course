# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 12:53:33 2026

@author: lstivanello
"""

"""
5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage
of life. Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is
a baby.
• If the person is at least 2 years old but less than 4, print a message that the
person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that
the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that
the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that
the person is an adult.
• If the person is age 65 or older, print a message that the person is an elder.
"""

def estadio_vida(edad):
    if edad < 2:
        print('bebe')
    elif edad >= 2 and edad < 4:
        print('toddler')
    elif edad >= 4 and edad < 13:
        print('chico')
    elif edad >=13 and edad < 20:
        print('adolescente')
    elif edad >=20 and edad < 65:
        print('adulto')
    elif edad >= 65:
        print('adulto mayor')
    else:
        print('lo siento pero no puedo reonocer esa edad')

estadio_vida(33)