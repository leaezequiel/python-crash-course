# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 08:27:28 2026

@author: lstivanello
"""

"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the 
dinner, so you need to send out a new set of invitations. You’ll have to think of 
someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of 
your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the 
name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in 
your list.
"""

invitados = ['maradona', 'john von neumann', 'asimov' , 'MQ-17J']

for invitado in invitados:
    invitado = invitado.capitalize()
    invitacion = f"Buen día {invitado}, has sido invitado a mi evento"
    print(invitacion)

#• Start with your program from Exercise 3-4. Add a print() call at the end of 
#your program, stating the name of the guest who can’t make it.    
disculpas = f"Lo siento, pero {invitados[-1]} no puede venir porque no es real, tampoco ha nacido."
print(disculpas)

#• Modify your list, replacing the name of the guest who can’t make it with the 
#name of the new person you are inviting.
invitados[-1]="manu ginobilli"

#• Print a second set of invitation messages, one for each person who is still in 
#your list.
for invitado in invitados:
    invitado = invitado.capitalize()
    invitacion = f"Buen día {invitado}, has sido invitado a mi evento"
    print(invitacion)