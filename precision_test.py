from decimal import *
import enc
getcontext().prec=200
def test(x,y):
    z=enc.enc(x,y)
    rev_y=enc.dec(x,z)
    print(f'the decrypted value of y {rev_y}')
    error=Decimal(y)-rev_y
    return error

#accurate for 15 decimal places
#print(test(1.111111111111111,1.111111111111111))

#accurate for 150 decimal places
#print(enc.cos(Decimal(2)))

#accurate for 15 Decimal places
print(enc.acos(Decimal(-0.41614683654714238699756822950076218976600077107554489075514997378196493612407916907453177786016914036736679136521572855928865639989117238568344207401996469532153261824797838625058514854625158662802104)))