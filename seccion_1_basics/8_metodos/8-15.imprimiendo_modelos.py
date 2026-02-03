# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 13:23:59 2026

@author: lstivanello
"""

"""
8-15. Printing Models: Put the functions for the example printing_models.py in
 a separate file called printing_functions.py.

 Write an import statement at the top of printing_models.py, and modify the
 file to use the imported functions.
"""

import printing_functions 


unprinted = ['car', 'robot', 'rocket','miniatura de ginobilli']
completed = []

printing_functions.print_models(unprinted, completed)
printing_functions.show_completed_models(completed)
