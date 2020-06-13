# PRINT * PYRAMID PATTERN FOR GIVEN NUMBER
# SPACES ARE a-i-1, * ARE i + 1
a = int(input('ENTER A NUMBER TO PRINT PATTERN :'))
for i in range(a):
    print(' ' * (a-i-1) + '* ' * (i+1))