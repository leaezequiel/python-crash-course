# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 09:27:12 2026

@author: lstivanello
"""

"""
9-3. Users: Make a class called User:
    + Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile.
    
    *Make a method called describe_user() that prints a summary of the user’s information.
    *Make another method called greet_user() that prints a personalized greeting to the user.
    
Create several instances representing different users, and call both methods for each user.
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
        

lea = User("lea","ezequiel",33 , "SUDO")
charmander = User("charmander","ketchup", 6)
pikachu = User('pikachu', "ketchup", 2, "SUDO")
lea.saludar_usuario()
lea.describe_usuario()
charmander.saludar_usuario()
charmander.describe_usuario()
pikachu.describe_usuario()
pikachu.saludar_usuario()