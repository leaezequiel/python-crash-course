# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 12:19:10 2026

@author: lstivanello
"""

"""
8-13. User Profile: Start with a copy of user_profile.py from page 148. Build a
profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you.
"""

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    print(user_info)
    return user_info

user_profile = build_profile('albert', 'einstein',
location='princeton',
field='physics')

user_profile = build_profile('Lea', 'Eze', locacion = 'Buenos Aires', edad = 33)