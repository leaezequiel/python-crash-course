# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 08:33:38 2026

@author: lstivanello
"""

"""
3-6. More Guests: You just found a bigger dinner table, so now more space is 
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the 
end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
"""

invitados = ['maradona', 'john von neumann', 'asimov' , 'manu ginobilli']

#• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the 
#end of your program, informing people that you found a bigger table.
for invitado in invitados:
    invitado = invitado.capitalize()
    mensaje = f"Hey! {invitado}, tenemos mas lugar! preparate para mas invitados, tenemos una nueva mesa"
    print(mensaje)
    
"""
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
"""
invitados.insert(0, "marie curie")
invitados.insert(3, "gandi")
invitados.append("musk")

#• Print a new set of invitation messages, one for each person in your list.
for invitado in invitados:
    invitado = invitado.capitalize()
    mensaje = f"Tengo el agrado de invitarte, {invitado}"
    print(mensaje)

#print(invitados)