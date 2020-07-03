# GENERATE A RANDOM PASSWORD OF LEN(6) WHERE 1,3,5 ARE CHARS RESL ALL DIGITS
from random import *

pwd = ''
for i in range(6):
    if i%2 == 0:
        pwd = pwd + str(randint(0,9))
    else:
        alphabets = list(map(chr, range(ord('a'), ord('z')+1)))
        pwd = pwd + choice(alphabets)
print(pwd) 

# ALTERNATIVE
# TO GET ALPHABETS AS STRING
# import string
# string.ascii_lowercase  #'abcdefghijklmnopqrstuvwxyz'  
# string.digits # '0123456789'
from string import *

alphabets = ascii_lowercase + ascii_uppercase
digits = digits #string.digits
print(choice(alphabets),choice(digits),choice(alphabets),choice(digits),choice(alphabets),choice(digits),sep='')

alnum = ascii_lowercase + ascii_uppercase + digits
print(choice(alnum),choice(alnum),choice(alnum),choice(alnum),choice(alnum),choice(alnum),sep='')
