def replaceMiddle(arr):
    if len(arr) % 2 == 0: 
        index1 = ((len(arr)/2)-1)
        index2 = ((len(arr)/2))
        
        print 'l at first num is', arr[index1]
        print 'l at second num is', arr[index2]
        
        middle = arr[index1] + arr[index2]
        print 'middle is', middle
        arr[index2] = middle
        print 'just changed index2 so:',arr
        
        for i, j in enumerate(arr): 
            if i == index1: 
                arr.pop(index1)     
        return arr      
    
    elif len(arr) % 2 == 1: 
        mid2 = arr[(len(arr)/2)]
        return arr
