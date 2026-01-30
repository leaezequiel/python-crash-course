# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 10:36:00 2026

@author: lstivanello
"""
"""
4-12. More Loops: All versions of foods.py in this section have avoided using
for loops when printing, to save space. Choose a version of foods.py, and
write two for loops to print each list of foods.
"""

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

for i in my_foods:
    print("me gusta mucho comer", i)
    
for n in friend_foods:
    print("mi amigo ama comer", n)