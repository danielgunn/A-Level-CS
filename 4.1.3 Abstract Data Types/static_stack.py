class ArrayStack:
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
        self.data = [0] * size
        self.size = size
        self.top = -1

    def push(self, value):
        """Add the value to the top of the stack"""
        if self.top == (self.size - 1):
            print("Error the stack is full!")

        else:
            self.top += 1
            self.data[self.top] = value

    def pop(self):
        """return the value that is currently on the top of the stack"""
        if self.top == -1:
            print("Error the stack is empty!")
            return None
        else:
            self.top -= 1
            return self.data[self.top + 1]

if __name__ == "__main__":
    help(ArrayStack)