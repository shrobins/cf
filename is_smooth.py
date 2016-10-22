def isSmooth(arr):
    if arr[0] == arr[-1]: 
        print "first and last are same"
        if len(arr) % 2 == 0: 
            print "even number array"
            mid1 = arr[(len(arr)/2)]
            mid2 = arr[((len(arr)/2)-1)]
            print "sum of middles is",mid1 + mid2
            if mid1 + mid2 == arr[0]: 
                return True 
            else: 
                return False
        elif len(arr) % 2 == 1: 
            print "odd number array"
            middle = arr[(len(arr)/2)]
            print "middles is",middle
            if middle == arr[0]: 
                return True 
            else: 
                return False 
                
    else: 
        return False
