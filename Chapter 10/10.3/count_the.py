filename = 'alice2.txt'
with open(filename) as f_obj:
    file = f_obj.read()
    print(file.lower().count('the'))