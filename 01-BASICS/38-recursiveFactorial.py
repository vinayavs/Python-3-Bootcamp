# WRITE A FUNCTION TO FIND FACTORIAL
# WITHOUT RECURSION
def fact(n):
    res = 1
    while n >=1 :
        res = res*n
        n = n-1
    return res

fact(3)
# WITH RECURSION
def factorial(n):
    if n == 0:
        res = 1
    else:
        res = n * factorial(n-1)
#         print('The factorial of {} is :{}'.format(n,res))
    return res
# for i in range(11):
#     print('The factorial of {} is :{}'.format(i,factorial(i)))
factorial(5)