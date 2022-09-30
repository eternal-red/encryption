from decimal import *
import enc
import arccos2
getcontext().prec=200
def test(x,y):
    z=enc.enc(x,y)
    rev_y=arccos2.dec(x,z)
    print(f'decrypted value of y is: {rev_y}')
    error=Decimal(y)-rev_y
    return error


#accuracy up to 17 decimal places with new pi and declaring everything decimal
print(test(1.111111111111111,1.111111111111111))

#accurate for 15 decimal places for enc file
#print(test(1.111111111111111,1.111111111111111))

#accurate for 150 decimal places
#print(enc.cos(Decimal(2)))