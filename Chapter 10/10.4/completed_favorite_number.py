import json

def get_favorite_number():
    try:
        filename = 'favorite_number.json'
        with open(filename) as f_obj:
            favorite_number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favorite_number

def get_new_number():
    favorite_number = input("Please enter your favorite number: ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f_obj:
        json.dump(favorite_number, f_obj)

def know_number():
    favorite_number = get_favorite_number()
    if favorite_number:
        print("I know your favorite number is " + favorite_number)
    else:
        get_new_number()

know_number()