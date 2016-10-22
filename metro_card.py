def metroCard(lastNumberOfDays):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    l = [] 
    
    if lastNumberOfDays == 28: 
        l.append(31)
        return l
    elif lastNumberOfDays == 30: 
        l.append(31)
        return l
    else:
        l = [28,30,31]
        return l
