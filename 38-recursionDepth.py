# TO CHECK MAX RECURSION DEPTH - 995
# till 994 its Okay
cnt = 0
def factorial(n):
    global cnt
    cnt = cnt + 1
    print('Execution of factorial for :',n)
    if n == 0:
        res = 1
    else:
        res = n * factorial(n-1)
    return res

# print(factorial(994))   
print(factorial(995))  # RecursionError: Max recursion depth exceeds
print('The no of times factorial executed is :',cnt)