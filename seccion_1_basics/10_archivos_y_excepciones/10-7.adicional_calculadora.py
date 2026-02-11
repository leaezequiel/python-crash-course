# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 10:01:50 2026

@author: lstivanello
"""
"""
10-7. Addition Calculator: Wrap your code from Exercise 10-5 in a while loop so the user can continue entering numbers, even if they make a mistake and enter text instead of a number.
"""

numeros = 0



while True:
    numero = input('ingrese numeros para sumarlos o ingrese "q" para salir')

    if numero == "q":
        print("Gracias por usar el acumulador")
        print("Acumulaste ", numeros)
        break
    try:
        numero = int(numero)
    except ValueError:
        print("Lo atrame, tranca que sigue")
        pass
    else:
        numeros += numero
        
        print(numeros)
