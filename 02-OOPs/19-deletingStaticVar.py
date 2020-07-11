# we can’t modify/delete static variable by using obj ref or self. But we can access 
# static variables by using obj ref, self and class
class Test:
    a = 10
    b = 20
    c = 50
t = Test()
print(t.a)  # 10
# del t.a  #AttributeError , deleting stacitc variable by using obj is not possible
del Test.a  # Deleting Static variable by usning classname
print(Test.__dict__)

t.b = 30 # Modifying/adding static varialbe by obj ref not possible, it will create/update a new instance var
print(Test.__dict__) # b = 20 

Test.b = 40 # modifying static variable by using classname
del Test.c  # deleting static variable by using classname
print(Test.__dict__)