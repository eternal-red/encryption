import time
from encryption import fixedKey
from decimal import *

#start time
start_time=time.time_ns()
gm_time=time.localtime(start_time/1000000000)
output=time.asctime(gm_time)
print(output)

#use for loop for average time estimate
encrypted=(fixedKey.enc(1,1))
#cleartext=(enc.dec(1,encrypted))

#calculate elapsed time
end_time=time.time_ns()
elapse_time=end_time-start_time

#formatting
def format(time): #time in nanoseconds
    sec=time//1000000000
    nano=time%1000000000
    min=sec//60
    sec=sec%60
    print(f'minutes: {min} seconds: {sec} nanoseconds: {nano}')
format(elapse_time)
format(time.process_time_ns())