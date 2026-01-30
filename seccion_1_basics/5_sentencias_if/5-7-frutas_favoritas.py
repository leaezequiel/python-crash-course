# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 13:03:25 2026

@author: lstivanello
"""

'''
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit
is in your list. If the fruit is in your list, the if block should print a statement,
such as You really like bananas!
'''
#se que dice de definir 5 if pero es mil veces mas practico este codigo reutilizable
frutas_favoritas = ['kiwi', 'arandanos', 'banana']

def inspector_frutas(fruta):
    if fruta in frutas_favoritas:
        print("Me encanta comer ", fruta)
    else:
        print("Lo siento pero no me gusta comer",fruta)

inspector_frutas('kiwi')
inspector_frutas('banana')
inspector_frutas('manzana')
inspector_frutas('pera')
inspector_frutas('durazno')