"""
This set of Abstract Data Types use static memory allocation.
They all use an array as their backing data store, and they
will never use dynamic memory allocation after the point
of construction.

They are meant as demonstration.  I don't recommend using
this type of data structure in your project, unless you have
specific memory requirements
"""


class Stack:
    """This stack is implemented using an array that is
    allocated during construction.  It can never grow beyond
    this size limitation

    Notice it can have three states:
    ## Empty ##
    -1     0 1 2 3 4 5 6
     ^


    Top

    ## Full ##
    0 1 2 3 4 5 6
                ^
                Top

    ## Normal ##
    H E L L O
    0 1 2 3 4 5 6
            ^
            Top
    """
    def __init__(self, size):
        """ size -- the maximum size the stack will contain """
        self.a = [0] * size
        self.size = size
        self.top = -1

    def push(self, value):
        """Add the value to the top of the stack"""
        if self.top == (self.size - 1):
            print("Error the stack is full!")

        else:
            self.top += 1
            self.a[self.top] = value

    def pop(self):
        """return the value that is currently on the top of the stack"""
        if self.top == -1:
            print("Error the stack is empty!")
            return None
        else:
            self.top -= 1
            return self.a[self.top+1]

def testStack():
    """ test method for the Stack class """
    print("Testing the stack")
    s = Stack(4)
    s.pop()
    print("I expect an empty error above")
    for i in range(3,8,2):
        s.push(i)
    print("I expect 7:", s.pop())
    print("I expect 5:", s.pop())
    print("I expect 3:", s.pop())
    print("I expect empty error above and None:", s.pop())
    for i in range(7):
        s.push(i)
    print("I expect three full error above")

help(Stack)
testStack()