f_num = input("Please enter your favorite number: ")

filename = 'favorite_number.json'

with open(filename, 'w') as f_obj:
    json.dump(f_num, f_obj)
    