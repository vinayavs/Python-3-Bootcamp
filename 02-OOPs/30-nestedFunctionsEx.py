# A function which is defined inside another function is called as nested function
# Nested functions are able to access the variables of enclosing scope

class Test:
    def m1(self):
        def calc(a,b):
            print('SUM :',a+b)
            print('SUB :',a-b)
        calc(10,20)
        calc(40,10)
t = Test()
t.m1()

# EXAMPLE 2
def outer(n):
    def inner_incr(n):  # HIDDEN FROM OUTER CODE
        return n+1
    num = inner_incr(n)
    print(n,num)
outer(10)
