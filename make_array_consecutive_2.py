def makeArrayConsecutive2(sequence):
    low = min(sequence)
    high = max(sequence)
    l2 = range(low,high+1)
    l3 = []
    for i, j in enumerate(l2): 
        if j not in sequence: 
            l3.append(j)
    
    return len(l3)
