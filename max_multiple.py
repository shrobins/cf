def maxMultiple(divisor, bound):
    l = []
    for i in range(bound+1): 
        if i % divisor == 0: 
            l.append(i)
    return max(l)

