
绝对文件路径

file_path = 'E:\Python Note\Python Crash Course\Chapter 10\pi_digits.txt'


*
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)



*
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())
       


*
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())


