"""
doesn't work in Spyder, but works well in online Python.
"""

import json

def get_stored_user_name():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
    

def get_new_username():
    filename = 'username.json'
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    print("We will remember you when you come back, " + username + "!")


def greet_user():
    username = get_stored_user_name()
    if username:
        answer = input("Is " + username + " your name? yes/no")
        if answer == 'yes':
            print("Welcome back, " + username)
        else:
            get_new_username()
    else:
        get_new_username()

greet_user()