# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 11:30:40 2026

@author: lstivanello
"""

"""
9-7. Admin: An administrator is a special kind of user.

Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167).

* Add an attribute, privileges, that stores a list of
strings like "can add post", "can delete post", "can ban user", and so on.


*Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
"""

from usuarios import User

class Admin(User):
    
    def __init__(self, primer_nombre, apellido, edad, privilegios ):
        super().__init__(primer_nombre, apellido, edad)
        self.privilegios = privilegios
    
    def mostrar_privilegios(self):
        for privilegio in self.privilegios:
            print(privilegio)
            
administrador = Admin('Super', 'ADMIN', 3, ['add post','delete post', 'ban other users', 'edit posts'])
administrador.mostrar_privilegios()