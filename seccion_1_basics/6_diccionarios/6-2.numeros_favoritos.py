# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 10:13:54 2026

@author: leaez
"""

"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary.  
Think of a favoritenumber for each person, and store each as a value in your
 dictionary. Printeach person’s name and their favorite number. For even more fun,
 poll a few friends and get some actual data for your program
"""

numeros_favoritos = {'lea':11 ,
                     'teo':10 ,
                     'male':6 ,
                     'eli':24 ,
                     'messi':10 ,
                     }

for persona in numeros_favoritos:
    print(f"El numero fav. de {persona} es {numeros_favoritos[persona]}")