# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 09:57:30 2026

@author: lstivanello
"""

"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
 Add an attribute called number_served with a default value of 0.

 Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again.
 Primera parte:
"""
class Restaurante:
    """Ejemplo de resto con 2 atriutos y dos metodos """
    
    #clase constructora
    def __init__(self, restaurante_nombre, tipo_cocina):
        self.restaurante_nombre = restaurante_nombre
        self.tipo_cocina = tipo_cocina
        self.clientes_servidos= 0
        
    def describe_restaurante(self):
        print(f"{self.restaurante_nombre} sirve {self.tipo_cocina}")
    
    def apertura_restaurante(self):
        print(f"{self.restaurante_nombre} esta abierto" )
        
    #desde aca segunda parte:  
    def set_clientes_servidos(self, clientes):
        self.clientes_servidos = clientes
        print("Se sirvieron ", self.clientes_servidos)
        
    def incrementa_clientes(self, clientes):
        self.clientes_servidos += clientes
        print("Se sirvieron ", self.clientes_servidos)
        
kitchen = Restaurante("kitchenet","gourmet")
print(kitchen.clientes_servidos)
kitchen.clientes_servidos = 3
print(kitchen.clientes_servidos)
kitchen.set_clientes_servidos(100)
kitchen.incrementa_clientes(999)

"""
Add a method called set_number_served() that lets you set the number of
customers that have been served. Call this method with a new number and print
the value again.

Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a day of
business.

"""