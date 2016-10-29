def additionWithoutCarrying(param1, param2):
    
    n1 = str(param1)
    n2 = str(param2)
    num1 = [] 
    num2 = []
    flist = []
    num3 = []
    
    for i in n1: 
        num1.append(i)
    
    for i in n2: 
        num2.append(i)
    
    if len(num1) > len(num2): 
        longer = num1
        shorter = num2
    else: 
        longer = num2
        shorter = num1

    print 'shorter is',shorter,"with length",len(shorter)

    print 'longer is',longer,'with length',len(longer)

    while len(shorter) < len(longer): 
        shorter.insert(0,0)

    for i, j in zip(num1, num2): 
        flist.append(int(i) +int(j))
    
    for i,j in enumerate(flist): 
        if j >= 10: 
            flist[i] = j - 10 
    
    print 'flist is now',flist
    
    for i in flist: 
        num3.append(str(i))

    final_num = ''.join(num3)
    print 'final num is',final_num
    return int(final_num)
