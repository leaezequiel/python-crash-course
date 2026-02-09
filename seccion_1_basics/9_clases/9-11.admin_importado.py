# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 14:07:19 2026

@author: lstivanello
"""

"""
PARTE B:
9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). Store
the classes User, Privileges, and Admin in one module. Create a separate file,
make an Admin instance, and call show_privileges() to show that everything is
working correctly.
"""
from sistema import User, Privilegios, Admin

administrador = Admin('Super', 'ADMIN', 3, ['add post','delete post', 'ban other users', 'ES ESTE EL OK?'])
administrador.privilegios.mostrar_privilegios()