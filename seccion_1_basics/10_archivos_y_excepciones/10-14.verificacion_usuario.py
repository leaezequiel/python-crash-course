# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 14:01:22 2026

@author: lstivanello
"""

"""
10-14. Verify User: The final listing for remember_me.py assumes either that the user has already entered their username or that the program is running for the first time. We should modify it in case the current user is not the person who last used the program.
Before printing a welcome back message in greet_user(), ask the user if this is the correct username. If it’s not, call get_new_username() to get the correct username.

"""
from pathlib import Path
import json

path = Path('user_info.json')

def get_stored_userinfo():
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

def get_new_userinfo():
    name = input("What is your name? ")
    age = input("How old are you? ")
    city = input("Where do you live? ")
    userinfo = {"name": name.strip(), "age": age.strip(), "city": city.strip()}
    path.write_text(json.dumps(userinfo), encoding='utf-8')
    return userinfo

def greet_user():
    userinfo = get_stored_userinfo()
    if userinfo:
        ans = input(f"Is this you, {userinfo['name']}? (y/n) ").strip().lower()
        if ans != 'y':
            userinfo = get_new_userinfo()
    else:
        userinfo = get_new_userinfo()

    print(f"Welcome back, {userinfo['name']}!")
    print(f"I remember you. You're {userinfo['age']} years old and you live in {userinfo['city']}.")

if __name__ == "__main__":
    greet_user()