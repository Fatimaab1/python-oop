# create a Animal class
# syntax class name:

class Animal:
    # __init__ to declare class attribues (to initialise a class)

    def __init__(self): # self refers to current class
        self.alive = True
        self.spine = True

    def sleep(self):
        return "8 hours of sleep is advised"

    def eat(self):
        return "eat if you like to stay alive.. and eat healthy."

# create an object of the class before using it
cat = Animal()
#print(cat.eat()) # abstarcted how was eat created or what info is available
