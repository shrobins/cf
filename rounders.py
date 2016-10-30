#came down to math trick
def rounders(value):
    base = 1 
    value = value 

    while value > 0: 
        if value < 10: 
            break
        elif value % 10 < 5: 
            value = value / 10 
        else: 
            value = value/10 + 1 
        base *= 10 

    return value * base 
