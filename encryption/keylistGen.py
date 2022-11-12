#creating a key generated with random.random
import random
def keygenE(x):
    random.seed(x) #key seed can be as many digits but will not generate more than 16 digits for the key list
    key_list=[]
    for i in range(200):
        key_list.append(random.random())
    return key_list
def keygenD(x):   
    random.seed(x)
    key_list=[]
    for i in range(200):
        key_list.append(random.random())
    key_list=key_list[::-1]
    return key_list
