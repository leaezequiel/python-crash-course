# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 08:52:02 2026

@author: lstivanello
"""

"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t 
arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a 
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two 
names remain in your list. Each time you pop a name from your list, print a 
message to that person letting them know you’re sorry you can’t invite them 
to dinner.
• Print a message to each of the two people still on your list, letting them 
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty 
list. Print your list to make sure you actually have an empty list at the end of 
your program.
"""
invitados = ['marie curie', 'maradona', 'john von neumann', 'gandi', 'asimov', 'manu ginobilli', 'musk']


"""
• Start with your program from Exercise 3-6. Add a new line that prints a 
message saying that you can invite only two people for dinner.
"""
for invitado in invitados:
    invitado = invitado.capitalize()
    mensaje = f"Lo siento, {invitado}, solo tnego 2 lugares. Debo hacer algunos recortes"
    print(mensaje)

"""
• Use pop() to remove guests from your list one at a time until only two 
names remain in your list. Each time you pop a name from your list, print a 
message to that person letting them know you’re sorry you can’t invite them 
to dinner.
"""
while len(invitados) != 2:
    borrado = invitados.pop()
    borrado.capitalize()
    disculpa = f"Lo siento,  {borrado} pero no puedo invitarte"
    print(disculpa)
    
print(invitados)

"""
• Print a message to each of the two people still on your list, letting them 
know they’re still invited.
"""
for invitado in invitados:
    invitado = invitado.capitalize()
    mensaje = f"Tuviste suerte, has sido invitado {invitado}"
    print(mensaje)
    
"""
• Use del to remove the last two names from your list, so you have an empty 
list. Print your list to make sure you actually have an empty list at the end of 
your program.
"""
del invitados [0]
del invitados [0]
print(invitados)