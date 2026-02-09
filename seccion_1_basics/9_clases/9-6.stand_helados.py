# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 10:30:21 2026

@author: lstivanello
"""

"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
Write a class called IceCreamStand that inherits from the Restaurant class you wrote in
Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
will work; just pick the one you like better. 

Add an attribute called flavors that stores a list of ice cream flavors. 
Write a method that displays these flavors.
Create an instance of IceCreamStand, and call this method.
"""
from restaurante import Restaurante 
#del archivo... importa la clase...

class Helado_stand(Restaurante):
    
    def __init__(self, restaurante_nombre, tipo_cocina, gustos):
        super().__init__(restaurante_nombre, tipo_cocina)#no va el self
        self.gustos = gustos
        
    def muestra_gustos(self):
        for gusto in self.gustos:
            print(gusto)
            
los_amores = Helado_stand('Muy Helados', 'gelateria', ['crema', 'super dulce de leche', 'sambayon'])
los_amores.muestra_gustos()