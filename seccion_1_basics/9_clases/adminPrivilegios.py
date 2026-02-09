# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 14:14:44 2026

@author: lstivanello
"""
from user import User

class Privilegios():
    
    def __init__(self, privilegios):
        self.privilegios = privilegios
        
    def mostrar_privilegios(self):
        for privilegio in self.privilegios:
            print(privilegio)
            
class Admin(User):
    
    def __init__(self, primer_nombre, apellido, edad, privilegios = None ):#no se asigna privilegio
        super().__init__(primer_nombre, apellido, edad)
        self.privilegios = Privilegios(privilegios)
    
