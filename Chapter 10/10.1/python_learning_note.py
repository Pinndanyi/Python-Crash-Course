
with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)





with open('learning_python.txt') as file_object:
    for line in file_object.readlines():
        print(line.rstrip())




with open('learning_python.txt') as file_object:
    contents = []
    for line in file_object.readlines():
        contents.append(line)

print(contents)