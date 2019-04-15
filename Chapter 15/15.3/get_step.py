from random import choice

def get_step():
    direction = choice([1, -1])
    distance = choice([1, 1, 2, 3, 4])
    steps = direction * distance
    
    return steps

            
