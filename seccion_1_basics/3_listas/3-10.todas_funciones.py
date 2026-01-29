# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 14:08:24 2026

@author: lstivanello
"""

"""
3-10. Every Function: Think of things you could store in a list. For example, you
could make a list of mountains, rivers, countries, cities, languages, or anything
else you’d like. Write a program that creates a list containing these items and
then uses each function introduced in this chapter at least once.
"""
jugadores_favoritos = ["iverson", "ginobilli","durant","nocioni","scola","antetokounmpo","dončić"]

print("En total tengo la sig. cantidad de favoritos ",len(jugadores_favoritos))

jugadores_favoritos.append("briant")
print(jugadores_favoritos)

print("Son muchos, debo quitar alguno ",jugadores_favoritos)

print("Si los quisiera de la A la Z: ",sorted(jugadores_favoritos))
jugadores_favoritos.sort()
jugadores_favoritos.reverse()
print("Invertida la lista sería: ",jugadores_favoritos)

print("Adios scola.. ya no eres favorito")
jugadores_favoritos.remove("scola")
print(jugadores_favoritos)

print("Me aburri del basquet, no quiero jugar mas y no tengo favoritos:")
del jugadores_favoritos
#print(jugadores_favoritos)