#Given a divisor and a bound, find the largest integer N such that:
#N is divisible by divisor.
#N is less than or equal to bound.
#N is greater than 0.

def maxMultiple(divisor, bound):
    l = []
    for i in range(bound+1): 
        if i % divisor == 0: 
            l.append(i)
    return max(l)

