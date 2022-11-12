from encryption.fixedKey import *
from encoding.decoder import *
from encoding.encoder import *

encoded=(encoder())
print(encoded)
output=''
for segment in encoded:
    encoded=float(segment)
    encrypted=enc(x=1.111111111111111,y=encoded)
    decrypted=str(dec(x=1.111111111111111,z=encrypted))
    decoded=decoder(decrypted)
    output+=decoded


print(f'encoded: {encoded}')
print(f'encrypted sample: {encrypted}')
print(f'decrypted sample: {decrypted}')
print(f'decoded: {output}') 