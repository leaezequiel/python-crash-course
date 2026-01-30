# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 08:22:39 2026

@author: lstivanello
"""

"""
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who 
would you invite? Make a list that includes at least three people you’d like to 
invite to dinner. Then use your list to print a message to each person, inviting 
them to dinner.
"""

invitados = ['maradona', 'john von neumann', 'asimov' , 'MQ-17J']

for invitado in invitados:
    invitado = invitado.capitalize()
    invitacion = f"Buen día {invitado}, has sido invitado a mi evento"
    print(invitacion)