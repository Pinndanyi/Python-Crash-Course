"""
desn't work in Spyder, but works well in online Python.
"""

import json

def greet_user():
    try:
        filename = 'username.json'
        with open(filename) as f_obj:
            username = json.load(f_obj)
        
    except FileNotFoundError:
        filename = 'username.json'
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
        print("We will remember you when you come back, " + username + "!")

    else:
        print("Welcome back, " + username)

greet_user()
