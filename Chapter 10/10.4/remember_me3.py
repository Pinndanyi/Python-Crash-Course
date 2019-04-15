"""
desn't work in Spyder, but works well in online Python.
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


def greet_user():
    username = get_stored_user_name()
    if username:
        print("Welcome back, " + username)
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We will remember you when you come back, " + username + "!")

greet_user()
        