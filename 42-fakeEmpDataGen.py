# FAKE EMP DATA GENERATOR
# ENAME - 3 TO 10 CHARS, 1ST CHAR-UPPER, REST-LOWER
# ENO - e-1234
# ESAL - FLOAT 10000 TO 50000
# ECITY - HYD, CHE, MUM, DEL, BNG, KOL, PUN
# EMOB - 10 DIGITS , 1ST NUM SHOULD BE BETWEEN 6-9
# EDESIG- SW, SSW, TL, PL, DM
from random import *
from string import *

alphabets = ascii_lowercase # ascii_uppercase
digits = digits #string.digits
def getName():
    ename = choice(alphabets).upper()
    n = randint(2,9)  
    for i in range(n):
        ename = ename + choice(alphabets)
    return ename
def getNo():
    eno = 'e-'
    for i in range(4):
        eno = eno + str(randint(0,9))  # choice(digits)
    return eno
def getSal():
    esal = round(uniform(10000,50000),2)  
    return esal
def getCity():
    ecity = ['HYD', 'CHE', 'MUM', 'DEL', 'BNG', 'KOL', 'PUN']
    return choice(ecity)
def getMob():
    emob = str(randint(6,9))  #choice('6789')
    for i in range(9):
        emob = emob + str(randint(0,9))
    return int(emob)
def getDesig():
    edesig = ['SW', 'SSW', 'TL', 'PL', 'DM']
    return choice(edesig)

def getEmpData():
    return getName(),getNo(),getSal(),getCity(),getMob(),getDesig()

for i in range(10):
    print(getEmpData())