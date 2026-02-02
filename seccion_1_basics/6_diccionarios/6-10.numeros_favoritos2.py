# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 08:52:58 2026

@author: lstivanello
"""

"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.
"""

numeros_favoritos = {'lea':[11 , 24],
                     'teo':[10 , 4],
                     'male':6 ,
                     'eli':24 ,
                     'messi':10 ,
                     }

for persona in numeros_favoritos:
    print(f"El numero fav. de {persona} es {numeros_favoritos[persona]}")