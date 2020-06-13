# PRINT DIAMOND * PATTERN FOR GIVEN NUMBER
# SPACES ARE FOR 1ST HALF a-i-1, * ARE i + 1, 2nd Half  i + 1, a-i-1
a = int(input('ENTER A NUMBER TO PRINT PATTERN :'))
for i in range(a):
    print(' ' * (a-i-1) + '* ' * (i+1))
for i in range(a):
    print((' ' * (i+1)) + ('* ' * (a-i-1)))