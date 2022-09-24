import decimal
from decimal import *
getcontext().prec=200
def test(x,y):
    getcontext().prec=50
    z=Decimal(x)/Decimal(y) #be sure to do this not (Decimal(x/y)
    return z