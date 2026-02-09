# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 14:05:40 2026

@author: lstivanello
"""

"""
PARTE A
9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). Store
the classes User, Privileges, and Admin in one module. Create a separate file,
make an Admin instance, and call show_privileges() to show that everything is
working correctly.
"""
class User:
    
    def __init__(self, primer_nombre, apellido, edad, tipo_usuario = 'regular'):
        self.primer_nombre = primer_nombre
        self.apellido = apellido
        self.tipo_usuario = tipo_usuario
        self.edad = edad
        
    def describe_usuario(self):
        print(f"{self.primer_nombre} {self.apellido} es un usuario tipo {self.tipo_usuario} con edad {self.edad}")
    
    def saludar_usuario(self):
        print(f"{self.primer_nombre} te doy la bienvenida")
 
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
    
