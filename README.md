# Python OOP

![](Screenshot 2022-08-04 at 11.43.11.png)

#### Step 1:
````python
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
print(cat.eat()) # abstarcted how was eat created or what info is available
````

#### Step 2:

Creating reptile file & inheriting from Animal class

````python
# inherit everything from Animal class into reptile
from animal import Animal

# create a reptile class
class Reptile(Animal): # write the name of the class in () - (parent class) to inherit
    # parent class - base class - super class

    def __init__(self):
        # need to let it know to inherit everything from parent class (Animal)
        super().__init__() # super is used to inherit everything from base class
        self.cold_blooded = True
        self.heart_chamber = [3, 4]

    def seek_heat(self):
        return "looking for the sun shine"

    def hunt(self):
        return "working hard to catch a next meal"

    # create an object of reptile class
reptile_object = Reptile()

#print(reptile_object.eat())
#print(reptile_object.hunt())
````
