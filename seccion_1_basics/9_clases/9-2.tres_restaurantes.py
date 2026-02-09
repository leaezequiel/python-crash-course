# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 09:22:47 2026

@author: lstivanello
"""

"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.
"""

class Restaurante:
    
    #clase constructora
    def __init__(self, restaurante_nombre, tipo_cocina):
        self.restaurante_nombre = restaurante_nombre
        self.tipo_cocina = tipo_cocina
        
    def describe_restaurante(self):
        print(f"{self.restaurante_nombre} sirve {self.tipo_cocina}")
    
    def apertura_restaurante(self):
        print(f"{self.restaurante_nombre} esta abierto" )

        
burger_kid = Restaurante('Burger Kid', 'hamburguesas')
pickit = Restaurante('Pickit food', 'comida barata al paso')
el_salteño = Restaurante('El salteño', 'bodegon')

el_salteño.describe_restaurante()
pickit.describe_restaurante()
burger_kid.describe_restaurante()