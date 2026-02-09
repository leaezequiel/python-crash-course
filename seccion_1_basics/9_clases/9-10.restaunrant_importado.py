# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 14:00:17 2026

@author: lstivanello
"""

"""
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
Make a separate file that imports Restaurant. Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is working
properly.
"""

from restaurante import Restaurante as resto

capuchi = resto('Capuchi', 'cocina de hogar')
capuchi.describe_restaurante()
capuchi.apertura_restaurante()