# Inner/Nested class in defined inside the body of another class.
class Outer:
    def __init__(self):
        print('Outer Object')
    class Inner:
        def __init__(self):
            print('Inner Object')
        class Nested:
            def __init__(self):
                print('Nested object')
            def m1(self):
                print('Nested Instance method')
            @staticmethod
            def m2():
                print('Nested Class Static Method')

# To call - Method 1 
o = Outer()
i = o.Inner()
n = i.Nested()
n.m1()
n.m2()
i.Nested.m2()

# Method 2 
Outer().Inner().Nested().m1()   # Instance Method
Outer().Inner().Nested.m2()  # Calling Static method by using class ref
Outer().Inner().Nested().m2()  # Calling static method by using object ref