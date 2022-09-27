import math
from decimal import *
getcontext().prec=200
pi=Decimal(3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951)

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
    s=pi/2-x-s
    return +s  #performs an operation to change s to new precision

def enc(x,y): #produces z
    for i in range(100):
        y=Decimal(x)+Decimal(cos(y))
    return y 

def dec(x,z):
    for i in range(100): 
        z=acos(Decimal(z)-Decimal(x))
    return z