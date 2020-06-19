# PRINT RIGHT HALF DIAMOND * PATTERN FOR GIVEN NUMBER
a = int(input('ENTER A NUMBER TO PRINT PATTERN :'))
for i in range(a):
    print('* '*(i+1))
for i in range(a-1):
    print('* '*(a-i-1))