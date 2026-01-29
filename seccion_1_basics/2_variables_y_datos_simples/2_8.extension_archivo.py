# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 10:00:29 2026

@author: lstivanello
"""

"""
2-8. File Extensions: Python has a removesuffix() method that works exactly  
like removeprefix(). Assign the value 'python_notes.txt' to a variable called 
filename. Then use the removesuffix() method to display the filename without 
the file extension, like some file browsers do
"""

nombre_archivo = "python_notes.txt"
archivo_sin_extension = nombre_archivo.removesuffix('.txt')

print(archivo_sin_extension)