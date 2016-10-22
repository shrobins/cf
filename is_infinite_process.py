#not passing all tests 

def isInfiniteProcess(a, b):
    
    if a == b: 
        return False 
    
    a += 1
    b -= 1
    
    while a != b: 
        if b < a: 
            return True
        else:
            return False
