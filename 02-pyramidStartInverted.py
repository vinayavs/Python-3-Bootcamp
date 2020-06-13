# PRINT INVERTED * PYRAMID PATTERN FOR GIVEN NUMBER
# SPACES ARE i, * ARE a-i
a = int(input('ENTER A NUMBER TO PRINT PATTERN :'))
for i in range(a):
    print((' ' * i) + ('* ' * (a-i)))