# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 10:41:07 2026

@author: lstivanello
"""

"""
4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the
change.
• The restaurant changes its menu, replacing two of the items with different
foods. Add a line that rewrites the tuple, and then use a for loop to print
each of the items on the revised menu.
"""

menu = ('milanesa con pure','pizza de muzzarella','wrap de pollo','risoto','ensalada cesar')
print("Menú original:")
for comida in menu:
    print(comida)
    
#menu[0] = 'empandas fritas'

#nuevo menu:
menu = ('empanadas fritas','tortilla de papa','wrap de pollo','risoto','ensalada cesar')
print("Menú modificado:")
for comida in menu:
    print(comida)