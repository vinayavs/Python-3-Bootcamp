# CHECK WHETHER THE GIVEN NUMBER IS PRIME OR NOT
#           10
#   1 2 3 4 5 6 7 8 9 10
#     ----2 TO n-1---   => range(2, n)  range(2,(n-1)+1) instead of this 
# To improve performance n//2 + 1, we can iterate up to middle.
n = int(input('Enter a number :'))
if n > 1 :
    isPrime = True
    for i in range(2,n//2 + 1):
        if n % i == 0:
            isPrime = False
            break
    if isPrime == True:
        print(n,'is a prime number')
    else:
        print(n,'is a composite number')
else:
    print(n, 'is a not a prime number')