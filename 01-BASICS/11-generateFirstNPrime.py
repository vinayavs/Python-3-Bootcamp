n = int(input('ENTER A NUMBER :'))
count = 0
n1 = 2
while True:
    isPrime = True
    for i in range(2, n1//2 +1):
        if n1 % i == 0:
            isPrime = False
            break
    if isPrime == True:
        print(n1)
        count += 1
    if count == n:
        break
    n1 += 1