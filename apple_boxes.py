def appleBoxes(k):
    i = 1
    red = 0 
    yellow = 0 

    while i <=k: 
        if i %2 == 1: 
            yellow += i*i
            print "yellow is now:",yellow
            i += 1
        elif i%2 == 0: 
            red += i*i
            print "red is now:",red
            i += 1 

    return red - yellow
