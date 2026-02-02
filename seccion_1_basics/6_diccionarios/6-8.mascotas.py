# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 08:23:37 2026

@author: lstivanello
"""

"""
6-8. Pets: Make several dictionaries, where each dictionary represents a different
pet. In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet.
"""


coco = {'nombre':'coco', 'duenio':'meli' ,'animal':'perro'}
clodine = {'nombre':'clodine', 'duenio':'lilian' ,'animal':'perro'}
doris = {'nombre':'doris', 'duenio':'lean' ,'animal':'gato'}
pinky = {'nombre':'pinky', 'duenio':'dani' ,'animal':'hamster'}

pets = [coco, clodine, doris, pinky]

for mascota in pets:
    print(mascota)
    print(f"{mascota['nombre'].capitalize()}: pertenece a {mascota['duenio'].capitalize()} y es un {mascota['animal']}")