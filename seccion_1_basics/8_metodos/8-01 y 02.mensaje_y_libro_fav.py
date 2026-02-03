# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 07:55:14 2026

@author: lstivanello
"""

"""
8-1. Message: Write a function called display_message() that prints one sentence
telling everyone what you are learning about in this chapter. Call the
function, and make sure the message displays correctly.

8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call.
"""

def muestra_mensaje ():
    print("Aca estoy aprendiendo Python!!")
          
muestra_mensaje()

def libro_favorito(libro):
    print(f"Uno de mis libros favoritos es {libro}.")
    
libro_favorito("Crimen y Castigo")