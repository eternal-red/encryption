from decimal import *
import random
getcontext().prec=70
def pi():
    getcontext().prec += 2  # extra digits for intermediate steps
    three = Decimal(3)      # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t
    getcontext().prec -= 2
    return +s       

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
    i, s=0,0
    double_fact,fact,constant,lasts=1,1,1,1
    expo=x
    while s != lasts: #run until nth term added to s is so insignficant s==lasts
        lasts = s
        i += 1
        double_n=(2*i+1)
        fact *= i
        double_fact*=(2*i)*(2*i-1)
        expo *= x ** 2
        constant*= 4 
        s+=(double_fact*expo)/(constant*(fact**2)*double_n) #stored as decimal type
    getcontext().prec -= 2
    s=pi()/2-x-s
    return +s  #performs an operation to change s to new precision

def enc(x,y): #produces z
    for i in range(200):
        y=Decimal(x)+Decimal(cos(y))
    return y 

def dec(x,z):
    for i in range(200): 
        z=acos(Decimal(z)-Decimal(x))
    return z
getcontext().prec=16 


