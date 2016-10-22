def arithmeticExpression(A, B, C):
    A = float(A)
    B = float(B)
    C = float(C)
    
    print A, B, C
    if A+B == C: 
        print '+'
        return True 
    elif A-B== C: 
        print '-'
        return True 
    elif A*B == C:
        print '*'
        return True
    elif A/B == C:
        print '/', C
        return True 
    else: 
        return False
    
