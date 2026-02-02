# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 08:43:34 2026

@author: lstivanello
"""

"""
6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places for
each person. To make this exercise a bit more interesting, ask some friends to
name a few of their favorite places. Loop through the dictionary, and print each
person’s name and their favorite places.
"""

lugares_fav = {'lea':'rio parana',
               'malena':['pileta', 'plaza', 'playa'],
               'harry':['la choza de hadrid','clase de pociones']
               }

for k, v in lugares_fav.items():
    print(f"{k.capitalize()} ama ir a {v}")