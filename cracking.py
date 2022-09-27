from decimal import *
import enc

#assume y and z are known

#base case
def base(y,z):
    z=Decimal(z)
    for i in range(10):
        i=Decimal(i)
        return (abs(enc.enc(i,y)-z))

#fully autonomous cracker
def cracker(y,z,x=1):
    z=Decimal(z)
    thresh=1
    for i in range(10):
        #x+=i/10**?
        if abs(enc.enc(i,y)-z)>thresh:
            cracker(y,z,x)




#solution to stop cracking: make number of rounds is part of key