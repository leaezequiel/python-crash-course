# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 13:00:38 2026

@author: lstivanello
"""

"""
9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
"""
from usuarios import User

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
    

            
administrador = Admin('Super', 'ADMIN', 3, ['add post','delete post', 'ban other users', 'edit posts'])
administrador.privilegios.mostrar_privilegios()