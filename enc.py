import math
from decimal import *
getcontext().prec=200

def cos(x):
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
    while s != lasts: #run until nth term added to s is so insignficant s==lasts
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
        #print(type(s))
    getcontext().prec -= 2
    return +s  #performs an operation to change s to new precision

def acos(x):
    getcontext().prec += 2
    k, lasts = 0, 0
    s, fact, k_exclam, half_poc = 1, 1, 1, 1
    num= x
    while s!= lasts:
        k+=1
        lasts = s
        half_poc*= (2*k)*(2*k-1)/2
        k_exclam*=k
        num*= x**2
        fact=k_exclam+2*k*k_exclam
        s += num*Decimal(half_poc)/Decimal(fact)
    getcontext().prec -= 2
    s=Decimal(math.pi/2)-s
    return s

def enc(x,y): #produces z
    for i in range(100):
        y=Decimal(x)+Decimal(cos(y))
    return y 

def dec(x,z):
    for i in range(100): 
        z=acos(Decimal(z)-Decimal(x))
    return z/4
