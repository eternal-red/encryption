import math
from decimal import *
from enc import pi
getcontext().prec=200

def acos(x):
    getcontext().prec += 2
    i, lasts, s, fact= 0, 1, 0, 1
    double_fact=1
    expo=x
    constant=1
    while s != lasts: #run until nth term added to s is so insignficant s==lasts
        lasts = s
        i += 1
        double_n=(2*i+1)
        fact *= i
        double_fact*=(2*i)*(2*i-1)
        expo *= x ** 2
        constant*= 4 
        s+=(double_fact*expo)/(constant*(fact**2)*double_n)
    getcontext().prec -= 2
    s=pi()/2-x-s
    return +s  #performs an operation to change s to new precision

