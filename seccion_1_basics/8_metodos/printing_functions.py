# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 12:45:20 2026

@author: lstivanello
"""
"""
8-15. Printing Models: Put the functions for the example printing_models.py in
 a separate file called printing_functions.py. Write an import statement at the
 top of printing_models.py, and modify the file to use the imported functions.
"""

# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)