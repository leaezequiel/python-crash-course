# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 08:32:40 2026

@author: lstivanello
"""

"""

8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 
The function should take in an artist name and an album title, and it should return a dictionary 
containing these two pieces of information. 
Use the function to make three dictionaries representing different albums.
Print each return value to show that the dictionaries are storing the album information correctly.
Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
If the calling line includes a value for the number of songs, add that value to the album’s dictionary.
Make at least one new function call that includes the number of songs on an album.

"""

def hacer_album(artista, nombre_album, n_canciones = None):
    album = {'artista':artista, 'album':nombre_album}
    if n_canciones is not None:
        album['canciones'] = n_canciones #asi asigna
    return album

print(hacer_album("Nirvana", "Nevermind"))
print(hacer_album("LP", "Meteora",20))
print(hacer_album("Jonas Brothers", "Live tour"))

