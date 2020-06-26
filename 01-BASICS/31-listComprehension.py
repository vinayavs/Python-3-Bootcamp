# CREATE A LIST OF SQUARE VALUES FOR 1 TO N NUMBERS
# [expression for element in iterable]
# [expression for element in iterable if cond] 
n = int(input('ENTER A NUMBER :'))
l = [i*i for i in range(1,n+1)]
print(l)

# LIST WITH POWER
from math import pow
l = [pow(2,i) for i in range(1,n+1)]
print(l)

# ALTERNATIVE
l = [2**i for i in range(1,n+1)]
print(l)

# LIST WITH 1 TO N NUMBERS WHICH ARE DIVISIBLE BY 10
l = [i for i in range(1,n+1) if i%10 == 0]
print(l)

# LIST OF ELEMETS PRESENT IN 1ST LIST BUT NOT IN SECOND LIST
l1 = [10,20,30]
l2 = [30,40,50]
l3 = [i for i in l1 if i not in l2]
print(l3) #[10, 20]

# LIST OF COMMON ELEMENTS IN BOTH LISTS
l4 = [i for i in l1 if i in l2]
print(l4)

# CREATE A LIST ONLY WITH 1ST LETTERS OF GIVEN LIST
l = ['Hi','Welcome','To','Python']
l2 = [word[0] for word in l]
print(l2)

# O/P - [[THE,3],[QUICK,5]......]
s = 'the quick brown fox jumps over the lazy dog'
l = [[word.upper(),len(word)] for word in s.split()]
print(l)
