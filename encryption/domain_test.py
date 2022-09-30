#file to test inputs if replacing y=z ever produces invalid inputs for arccos(x)
#for all possible y produced by x+cos(y)

#domain of arccos(x): [-1,1]
#range of arccos(x): [0,pi]

#bijective requirements
#domain of cos(x): [0, pi]
#range of cos(x): [-1,1]

#parameters for x,y,z
#x: [1, pi-1]
#y: (0, pi]   
#z: [pi-2, 2]

import math

def enc(x,y):
    for i in range(100):
        y=x+math.cos(y)
    return y

def dec(x,z):
    for i in range(100): 
        #print(z)
        z=math.acos(z-x)
    return z #this is y



def test(x,y):
    z=(enc(x, y))
    print(z)
    print(dec(x,z))


#testing
#ideal_key=1.13


#range of keys [1,2] and 
#range of cleartext [0,1] all work
for key in range(1,2000):
    key=1+key/1000
    for cleartext in range(1,1000):
        cleartext=cleartext/1000
        print(key, cleartext)
        test(key, cleartext)
    


