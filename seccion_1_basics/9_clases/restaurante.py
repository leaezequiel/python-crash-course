# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 09:40:34 2026

@author: lstivanello
"""

"""
PARTE A:
9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
 Add an attribute called number_served with a default value of 0.

 Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again.
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