# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 08:13:18 2026

@author: lstivanello
"""
"""
6-6. Polling: Use the code in favorite_languages.py (page 96).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.
"""


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

personas_a_encuestar = ['lean', 'jen','edward']

for k in favorite_languages.keys():
    if k in personas_a_encuestar:
        print(f"{k.capitalize()} debes tomar la encuesta!")
    else:
        print(f"{k.capitalize()} no debe tomar la encuesta, pero te invitamos de todas formas.")