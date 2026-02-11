# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 09:36:51 2026

@author: lstivanello
"""

"""
10-6. Addition: One common problem when prompting for numerical input occurs when
 people provide text instead of numbers.
 When you try to convert the input to an int,
 you’ll get a ValueError. Write a program that prompts for two numbers. 
 Add them together and print the result. Catch the ValueError if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.
"""
numero_1 = input('Ingrese un numero')
numero_2 = input('Ingrese otro numero')


try:
    
    numero_1 = int (numero_1)
    numero_2 = int (numero_2)
except ValueError:
    print("Alguno de los numeros ingresados no es numero")
else:
    resultado = numero_1 + numero_2
    print("El resultado es ",resultado)