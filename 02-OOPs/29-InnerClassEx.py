# Inner/Nested Class
# Creating Nested objectes automatically.

class Human:
    def __init__(self,name):
        print('Human Object Created....')
        self.name = name
        self.head = self.Head()
    def info(self):
        print('Hi,',self.name)
        print("I'm Busy with,")
        self.head.talk()
        self.head.brain.think()
    class Head:
        def __init__(self):
            print('Head Object Created...')
            self.brain = self.Brain()
        def talk(self):
            print('Talking....')

        class Brain:
            def __init__(self):
                print('Brain Object Created...')
            def think(self):
                print('Thinking....')

h = Human('vin')  # All Constructors executed automaticaly
h.info()