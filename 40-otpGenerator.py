from random import *
print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')

# ALTERNATIVE
otp = ''
for i in range(6):
    otp = otp + str(randint(0,9))
print(otp)