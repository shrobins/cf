def tennisSet(score1, score2):
    
    if score1 > score2: 
        winner = score1
        loser = score2
    elif score2> score1: 
        winner = score2 
        loser = score1
    else: 
        return False

    print winner, loser

    if winner == 6 and loser <=4: 
        return True 
    elif winner ==7 and loser ==5 or loser==6:
        return True 
    else: 
        return False
