class CircularQueue:
    """The CircularQueue is implemented using an array as
    backing store

    Notice it can have three states:
    ## Empty ##
    -1     0 1 2 3 4 5 6
     ^
     Front
     Back

    ## Full ##
    0 1 2 3 4 5 6       0 1 2 3 4 5 6
    ^           ^             ^ ^
    Front       Back          ^ Front
                              Back

    ## Normal ##
    H E L L O         L O     H E L
    0 1 2 3 4 5 6     0 1 2 3 4 5 6
    ^       ^           ^     ^
    Front   Back        Back   Front
    """
    def __init__(self, size):
        self.a = [0] * size
        self.back = -1
        self.front = -1
        self.size = size

    def enqueue(self, value):
        """ Add the value to the back of the queue """
        # if full:
        if ((self.back + 1) % self.size) == self.front:
            print("The Queue is full.. cannot enqueue")

        else:
            # if empty
            if self.front == -1:
                self.front = 0

            self.back += 1
            self.back %= self.size
            self.a[self.back] = value

    def dequeue(self):
        """remove the item from the front of the queue and return its value """
        # if empty:
        if self.front == -1:
            print("Error Queue is empty!")
            return None
        else:
            val = self.a[self.front]
            if self.front == self.back:  # only one item left!
                self.front = -1
                self.back = -1
            else:
                self.front += 1
                self.front %= self.size
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

