from decimal import *
from fixedKey import pi    
getcontext().prec=200
 
def acos(x):
    getcontext().prec += 2
    i, lasts, s, m, e, n = 1, 0, x, 1, 0, 0
    while s != lasts:
        lasts = s
        m *= Decimal(2 * i - 1)/Decimal(2 * i)
        e = 2 * i + 1
        n = ((x ** e) / e)
        s += m * n
        i += 1
    getcontext().prec -= 2
    return pi()/2-s

def dec(x,z):
    for i in range(100): 
        z=acos(Decimal(z)-Decimal(x))
    return z

print(acos(Decimal(0.2)))