from decimal import *
import enc
getcontext().prec=200
def test(x,y):
    z=enc.enc(x,y)
    rev_y=enc.dec(x,z)
    error=Decimal(y)-rev_y
    return error

print(test(1.1111111111,1.1111111111))
