# PRINT TRIANGED *'S FOR GIVEN NUMBER BY USING NESTED LOOPS
a = int(input('ENTER A NUMBER TO DISPLAY TRIANGLED * :'))
for i in range(1, a + 1):
    for j in range(1, i + 1):
        print('*', end='')
    print()