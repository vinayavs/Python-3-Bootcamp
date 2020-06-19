# GENERATE PRIME NUMBERS WHICH ARE LESS THAN OR EQUAL TO GIVEN NUMBER
n = int(input('Enter a number :'))
n1 = 2
while n1 <= n:
    isPrime = True
    for i in range(2, n1//2 +1):
        if n1 % i == 0:
            isPrime = False
            break
    if isPrime == True:
            print(n1)
    n1 += 1 