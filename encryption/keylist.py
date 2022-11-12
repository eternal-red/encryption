#encrypted with keys generated from random seeds
from fixedKey import *
from keylistGen import *

string1=keygenE(1111111111111111)
string2=keygenD(1111111111111111)

def keyEnc(keyList, y):
    for i in range(200):
        y=Decimal(1+keyList[i])+Decimal(cos(y))
    return y 

def keyDec(keyList,z):
    for i in range(200): 
        z=acos(Decimal(z)-Decimal(1+keyList[i]))
        print(z)
    return z

#domain problems :(
key1=keyEnc(string1, 1.1111111111111111)
print(key1)
key2=keyDec(string2,key1 )
print(key2)