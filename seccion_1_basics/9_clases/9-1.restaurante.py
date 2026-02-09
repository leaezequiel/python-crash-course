# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 08:15:38 2026

@author: lstivanello
"""
"""
9-1. Restaurant: Make a class called Restaurant.
 
The __init__() method for Restaurant should store two attributes: 
    a restaurant_name and a cuisine_type. 
 
 Make a method called describe_restaurant() that prints these two pieces of information, 
 
and a method called open_restaurant() that prints a message indicating that the restaurant is open.


Make an instance called restaurant from your class. Print the two attributes
 individually, and then call both methods
"""

class Restaurante:
    """Ejemplo de resto con 2 atriutos y dos metodos """
    
    #clase constructora
    def __init__(self, restaurante_nombre, tipo_cocina):
        self.restaurante_nombre = restaurante_nombre
        self.tipo_cocina = tipo_cocina
        
    def describe_restaurante(self):
        print(f"{self.restaurante_nombre} sirve {self.tipo_cocina}")
    
    def apertura_restaurante(self):
        print(f"{self.restaurante_nombre} esta abierto" )

        
la_kitchen = Restaurante('La Kitchen', 'al paso')
la_kitchen.describe_restaurante()
la_kitchen.apertura_restaurante()
print(la_kitchen.restaurante_nombre)
print(la_kitchen.tipo_cocina)