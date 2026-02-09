# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 10:13:28 2026

@author: lstivanello
"""

"""
9-5. Login Attempts: 
    * Add an attribute called login_attempts to your User class
from Exercise 9-3 (page 162). 

* Write a method called increment_login_attempts()
that increments the value of login_attempts by 1.

* Write another method called reset_login_attempts() that resets the value of login_attempts to 0.


Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0
"""
class User:
    
    def __init__(self, primer_nombre, apellido, edad, tipo_usuario = 'regular'):
        self.primer_nombre = primer_nombre
        self.apellido = apellido
        self.tipo_usuario = tipo_usuario
        self.edad = edad
        self.intentos_loggin = 0
        
    def describe_usuario(self):
        print(f"{self.primer_nombre} {self.apellido} es un usuario tipo {self.tipo_usuario} con edad {self.edad}")
    
    def saludar_usuario(self):
        print(f"{self.primer_nombre} te doy la bienvenida")
        
    def incremento_intentos_loggeo(self):
        self.intentos_loggin += 1
    
    def reseteo_intentos_loggeo(self):
        self.intentos_loggin = 0
        print("Se bajoron a 0 los intentos de loggeo")
    

lea = User("lea","ezequiel",33 , "SUDO")

contador = 0
while contador != 5:
    lea.incremento_intentos_loggeo()
    contador += 1
    
print(lea.intentos_loggin)
lea.reseteo_intentos_loggeo()
print(lea.intentos_loggin)