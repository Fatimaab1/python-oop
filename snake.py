# inherit reptile from Reptile class

from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True

    def use_tongue_to_smell(self):
        return "I can use my tongue to smell food"

    def _hibernate(self):
        return "protected method"

    def __shed(self):
        return "private method"



snake_object = Snake()
print(snake_object.eat()) # this function is inherited from Animal class
print(snake_object.seek_heat()) # this function is inherited from Reptile class
print(snake_object.use_tongue_to_smell()) # this function is inherited from the direct parent class snake

# create 2 more functions; one with _ the other one with __
# execute them both -return message should explain Encapsulation break down - public - protected - private

print(snake_object._hibernate()) # This is a protected method. prevents its usage by outside entities unless it is a subclass
print(snake_object.__shed) # This is a private method & will print 'AttributeERROR'

snake_object = shake()
# print(snake.object._use_tongue_to_smell())
print(snake_object.use_tongue_to_smell)

# exception handling with try: and except blocks

# what type of errors & exceptions have you seen so far
# syntax error
# indentation Error - value error - attribute error

#def _use_tongue_to_smell(self):
    #try:
        #return object.__shed()
    #except AttributeError:
        #return ""
# Try:
    #print()
    #return

#except name_of_error:
    # print()
    # return

    #finally:
    #print("relevant to logic above")

#