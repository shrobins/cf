def increaseNumberRoundness(n):
    x = str(n)
    y = x.count('0')
    if '0' in x[0:-y]: 
        return True
    else:
        return False
    
