while True:
    name = input('Please enter your name or enter "no" if you ' + "don't" +' want'
                 ' to continue: ')
    if name == 'no':
        break
    
    print("Welcome, " + name.title())
    
    with open('guest_book.txt', 'a') as file_object:
        file_object.write(name.title() + " has visited. \n")
    