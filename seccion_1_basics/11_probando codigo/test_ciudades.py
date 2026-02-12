# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 08:49:21 2026

@author: lstivanello
"""
"""
PARTE B


Create a file called test_cities.py that tests the function you just wrote.
Write a function called test_city_country() to verify that calling your function
with values such as 'santiago' and 'chile' results in the correct string. Run the
test, and make sure test_city_country() passes.
"""

from ciudad_funciones import recibidor

def test_prueba_recibidor():
    formato_ciudad = recibidor('caba', 'arg')
    assert formato_ciudad == 'Caba es una ciudad de Arg'