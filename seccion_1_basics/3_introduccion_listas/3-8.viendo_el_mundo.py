# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 09:07:01 2026

@author: lstivanello
"""

"""
3-8. Seeing the World: Think of at least five places in the world you’d like  
to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; 
just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the 
actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without chang
ing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse() to change the order of your list. Print the list to show that its 
order has changed.
• Use reverse() to change the order of your list again. Print the list to show 
it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the 
list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order. 
Print the list to show that its order has changed
"""
"""
Seeing the World: Think of at least five places in the world you’d like  
to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; 
just print it as a raw Python list.
"""
lugares = ["rio de janeiro", "bariloche","usuhuaia","berlin","zurich","amsterdam"]
for lugar in lugares:
    print(lugar.capitalize())
    
"""
• Use sorted() to print your list in alphabetical order without modifying the 
actual list.
• Show that your list is still in its original order by printing it.
"""
lugares_ordenados = sorted(lugares)
print("ordenado: ",lugares_ordenados)
print("original: ", lugares)
"""
• Use sorted() to print your list in reverse-alphabetical order without chang
ing the order of the original list.
• Show that your list is still in its original order by printing it again.
"""
ordenado_reverso= sorted(lugares_ordenados, reverse=True)
print("ordenado al revez con sorted true: ",ordenado_reverso)
print("original: ", lugares)

"""
• Use reverse() to change the order of your list. Print the list to show that its 
order has changed.
• Use reverse() to change the order of your list again. Print the list to show 
it’s back to its original order.
"""
lugares.reverse()
print("algo paso con el original: ",lugares)
print("dejame acomodarlo: ")
lugares.reverse()
print(lugares)

"""
• Use sort() to change your list so it’s stored in alphabetical order. Print the 
list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order. 
Print the list to show that its order has changed
"""
lugares.sort()
print("Dejame chequear si va de la A a la Z: ",lugares)
print("Ahora de la Z a la A: ")
lugares.sort(reverse=True)
print(lugares)