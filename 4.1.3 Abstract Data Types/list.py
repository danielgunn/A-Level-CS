class node:
    """A Node will contain only two things:
        - A Pointer to the next node
        - A value

        It is the fundamental building block of Lists
    """

    def __init__(self, value):
        """ The value is any data we wish to store at this Node """
        self.data = value # The value
        self.next = None  # A pointer to the next node in the list (Note Python doesnt have pointers)

class List:
    """
    A List consists of a node, connected to a node, connected to a node, ... and so on

    """
    def __init__(self):
        self.head = None  # a pointer to the first node
        self.length = 0 # keeping track of how many nodes we have

    def add(self, val):
        new_node = node(val)

        if self.length == 0:
            self.head = new_node
        else:
            i = self.head
            while (i.next != None):
                i = i.next

            i.next = new_node

        self.length += 1

    def remove(self, index):
        value = None
        if index > self.length - 1:
            return None #  this index is invalid
        elif index == 0:
            value = self.head.data
            self.head = self.head.next
        else:
            prev = self.head
            for i in range(0, index-1):
                prev = prev.next
            value = prev.next.data
            prev.next = prev.next.next
        self.length -= 1
        return value

    def __str__(self):
        if self.head == None:
            return "[]"

        i = self.head
        s = "["
        while i!=None:
            s+= str(i.data) + ", "
            i = i.next
        return s[:-2] + "]"

    def linear_search(self, value):
        i = self.head
        index = 0
        while (i.data != value):
            i = i.next
            index += 1
        return index

if __name__ == "__main__":
    help(List)
