encodeTable={' ': '00', '!': '01', '"': '02', '#': '03', '$': '04', '%': '05', '&': '06', 
"'": '07', '(': '08', ')': '09', '*': '10', '+': '11', ',': '12', '-': '13', '.': '14', 
'/': '15', ':': '16', ';': '17', '<': '18', '=': '19', '>': '20', '?': '21', '@': '22', 
'[': '23', '\\':'24', ']': '25', '^': '26', '_': '27', '`': '28', '{': '29', '|': '30', 
'}': '31', '~': '32', 'A': '33', 'B': '34', 'C': '35', 'D': '36', 'E': '37', 'F': '38', 
'G': '39', 'H': '40', 'I': '41', 'J': '42', 'K': '43', 'L': '44', 'M': '45', 'N': '46', 
'O': '47', 'P': '48', 'Q': '49', 'R': '50', 'S': '51', 'T': '52', 'U': '53', 'V': '54', 
'W': '55', 'X': '56', 'Y': '57', 'Z': '58', 'a': '59', 'b': '60', 'c': '61', 'd': '62', 
'e': '63', 'f': '64', 'g': '65', 'h': '66', 'i': '67', 'j': '68', 'k': '69', 'l': '70', 
'm': '71', 'n': '72', 'o': '73', 'p': '74', 'q': '75', 'r': '76', 's': '77', 't': '78', 
'u': '79', 'v': '80', 'w': '81', 'x': '82', 'y': '83', 'z': '84', '0': '85', '1': '86', 
'2': '87', '3': '88', '4': '89', '5': '90', '6': '91', '7': '92', '8': '93', '9': '94'}
 

def encoder():
    outputList=[]
    inputList=[]
    inputStr=input(f'enter cleartext: ')
    #division input into sections of 8
    rounds=len(inputStr)//8
    filler=(8-len(inputStr)%8)*' '
    for i in range(rounds):
        inputList.append(inputStr[i*8:(i+1)*8])
    inputList.append(inputStr[(rounds)*8:]+filler)
    #encode sections
    for chunk in inputList:
        encrypted_str='0.'
        for i in chunk:
            encodeSeg=encodeTable[i]
            encrypted_str+=encodeSeg
        outputList.append(encrypted_str)
    return outputList

#print(encoder())

var='0.7179616600596273'
print(float(var))

