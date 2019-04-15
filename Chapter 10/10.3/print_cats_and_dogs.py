try:
    with open('cats.txt') as file_1:
        for line in file_1:
            print(line)
    
except FileNotFoundError:
    pass


try:     
    with open('dogs.txt') as file_2:
        print("\n")
        for line in file_2:
            print(line)
        
except FileNotFoundError:
    print("Sorry, the file " + file_2 + " does not exist.")


