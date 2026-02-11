# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 13:52:58 2026

@author: lstivanello
"""
"""
CASI ENTERAMENTE HECHO CON IA, EL LIBRO ACA FLAQUEA EN LA EXPLICACIÓN...
10-13. User Dictionary: The remember_me.py example only stores one piece of information, the username. Expand this example by asking for two more pieces of information about the user, then store all the information you collect in a dictionary. Write this dictionary to a file using json.dumps(), and read it back in using json.loads(). Print a summary showing exactly what your program remembers about the user.
"""
from pathlib import Path
import json

def get_stored_userinfo(path):
    """Get stored user information if available."""
    if path.exists():
        contents = path.read_text()
        return json.loads(contents)
    return None

def get_new_userinfo():
    """Ask user for name, age and city, then return a dictionary."""
    name = input("What is your name? ")
    age = input("How old are you? ")
    city = input("Where do you live? ")

    return {
        "name": name,
        "age": age,
        "city": city
    }

def store_userinfo(path, userinfo):
    contents = json.dumps(userinfo)
    path.write_text(contents)

def greet_user():
    """Greet user using stored info, or ask and store if missing."""
    path = Path('user_info.json')
    userinfo = get_stored_userinfo(path)

    if userinfo:
        print(f"Welcome back, {userinfo['name']}!")
        print(f"I remember you. You're {userinfo['age']} years old "
              f"and you live in {userinfo['city']}.")
    else:
        userinfo = get_new_userinfo()
        store_userinfo(path, userinfo)
        print("Thanks! I'll remember your information next time.")

greet_user()