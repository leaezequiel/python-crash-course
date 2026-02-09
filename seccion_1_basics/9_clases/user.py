# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 14:13:41 2026

@author: lstivanello
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
 