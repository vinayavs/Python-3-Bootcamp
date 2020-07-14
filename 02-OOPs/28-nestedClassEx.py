# Inner/Nested class in defined inside the body of another class.
class Human:   # Outer Class
    class Head: # Inner Class
        def talk(self):
            print('Talking...')
        class Brain:
            def think(self):
                print('Thinking....')

# To call - method 1
hu = Human()   # Obj created
h = hu.Head()
b = h.Brain()
h.talk()
b.think()
