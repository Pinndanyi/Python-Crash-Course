while True:
    reason = input('Please tell me why do you like programming or enter "no" '
                   'if you don' + "'t want to continue: ")
    if reason == 'no':
        break
    
    with open('survey.txt', 'a') as file_object:
        file_object.write(reason + "\n")
    
    