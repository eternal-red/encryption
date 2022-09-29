from decimal import *
import enc

#assume y and z are known

#base case
def base(y,z):
    pos_list=[]
    z=Decimal(z)
    for i in range(10,20):
        i=Decimal(i)/10 
        possible_x=abs(enc.enc(i,y)-z)
        pos_list.append(possible_x)
    return pos_list
getcontext().prec=5

output_list=base(1.11111,1.3267291)
for i in output_list:
    print(i, "\n")


#fully autonomous cracker
def cracker(y,z,x=1):
    z=Decimal(z)
    thresh=1
    for i in range(10):
        #x+=i/10**?
        if abs(enc.enc(i,y)-z)>thresh:
            cracker(y,z,x)




#solution to stop cracking: make number of rounds is part of key