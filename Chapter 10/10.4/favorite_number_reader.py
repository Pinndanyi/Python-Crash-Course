import json

with open('favorite_number.json') as f_obj:
    number = json.load(f_obj)
    print("I know your favorite number, it's: " + number)