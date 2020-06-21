# CREATE A LIST OF SQUARE VALUES FOR 1 TO N NUMBERS
n = int(input('ENTER A NUMBER :'))
l = [i*i for i in range(1,n+1)]
print(l)