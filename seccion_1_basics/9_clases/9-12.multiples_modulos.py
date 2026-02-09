# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 14:13:04 2026

@author: lstivanello
"""

"""
9-12. Multiple Modules: Store the User class in one module,
 and store thePrivileges and Admin classes in a separate module.

 In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.
"""

from adminPrivilegios import Privilegios, Admin
from user import User

administrador = Admin('Super', 'ADMIN', 3, ['add post','delete post', 'ban other users', 'ES ESTE EL OK? OOKKK ?'])
administrador.privilegios.mostrar_privilegios()