#have an ascii table in here
#be sure to also encode numbers, spacecs, and symbols
#dictionary best method? 
# end of sequence symbol seems not necessary
#sequences of two numbers per character?

encodeTable={'a':'00', 'b':'01', 'c':'02', 'd':'03', 'e':'04', 
             'f':'05', 'g':'06', 'h':'07', 'i':'08', 'j':'09',
             'k':'10', 'l':'11', 'm':'12', 'n':'13', 'o':'14',
             'p':'15', 'q':'16', 'r':'17', 's':'18', 't':'19',
             'u':'20', 'v':'21', 'w':'22', 'x':'23', 'y':'24', 'z':'25',
            }
 
encrypted_str='0.'
inputStr=input(f'enter cleartext: ')

for i in inputStr:
    encodeSeg=encodeTable[i]
    encrypted_str+=encodeSeg


