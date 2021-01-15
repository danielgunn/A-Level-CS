class CircularQueue:
    """The CircularQueue is implemented using an array as
    backing store

    Notice it can have three states:
    ## Empty ##
    -1     0 1 2 3 4 5 6
     ^
    Top
    Bottom

    ## Full ##
    0 1 2 3 4 5 6       0 1 2 3 4 5 6
    ^           ^             ^ ^
    Bottom      Top           ^ Bottom
                              Top

    ## Normal ##
    H E L L O         L O     H E L
    0 1 2 3 4 5 6     0 1 2 3 4 5 6
    ^       ^           ^     ^
    Bottom  Top         Top   Bottom
    """
    def __init__(self, size):
        self.a = [0] * size
        self.top = -1
        self.bottom = -1
        self.size = size

    def enqueue(self, value):
        # if full:
        if ((self.top + 1) % self.size) == self.bottom:
            print("The Queue is full.. cannot enqueue")

        else:
            # if empty
            if self.bottom == -1:
                self.bottom = 0

            self.top += 1
            self.top %= self.size
            self.a[self.top] = value

    def dequeue(self):
        """remove the item from the bottom of the queue
        and return its value
        """
        # if empty:
        if self.bottom == -1:
            print("Error Queue is empty!")
            return None
        else:
            val = self.a[self.bottom]
            if self.bottom == self.top:  # only one item left!
                self.bottom = -1
                self.top = -1
            else:
                self.bottom += 1
                self.bottom %= self.size
            return val

def testQueue():
    """ test method for the Stack class """
    print("Testing the stack")
    q = CircularQueue(4)
    q.dequeue()
    print("I expect an empty error above")
    for i in range(3,8,2):
        q.enqueue(i)
    print("I expect 3:", q.dequeue())
    print("I expect 5:", q.dequeue())
    print("I expect 7:", q.dequeue())
    print("I expect empty error above and None:", q.dequeue())
    for i in range(7):
        q.enqueue(i)
    print("I expect three full error above")

if __name__ == "__main__":
    help(CircularQueue)
    testQueue()

