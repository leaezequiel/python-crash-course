# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 07:58:15 2026

@author: lstivanello
"""

"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text 
of a message that should be printed on the shirt. The function should print a sentence 
summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. 
Call the function a second time using keyword arguments.
"""

def hacer_remera(tamanio, mensaje):
    print(f"El pedido va a ser una remera talle {tamanio}, con la inscripción '{mensaje}'")
    
#Call the function once using positional arguments to make a shirt. 
hacer_remera("L", "Aguante los redondos")

#Call the function a second time using keyword arguments.
hacer_remera(tamanio ="M", mensaje="Thanos was right")

"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
"""
print("Segunda tanda de remeras: ")
def hacer_remera_2(tamanio = 'L', mensaje = 'I love Python'): #tienen que estar los dos con default 
    print(f"El pedido va a ser una remera talle {tamanio}, con la inscripción '{mensaje}'")
    
hacer_remera_2()
hacer_remera_2(tamanio = 'M')
hacer_remera_2('XXL','ACDC LIVE TOUR 2026')