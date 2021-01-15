class node:
    data = None # Value at this node
    next = None # A pointer to the next node in the list (Note Python doesnt have pointers)

    def __init__(self, value):
        self.data = value

class list:
    head = None  # a pointer to the first node
    length = 0 # keeping track of how many nodes we have

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
        if index == 0:
            value = self.head.data
            self.head = self.head.next
        else:
            prev = self.head
            for i in range(0, index-1):
                prev = prev.next
            value = prev.next.data
            prev.next = prev.next.next
        return value

    def print(self):
        i = self.head
        print("The list is: [", end='')
        while i!=None:
            print(i.data,"",end="")
            i = i.next
        print("]")

    def linear_search(self, value):
        i = self.head
        index = 0
        while (i.data != value):
            i = i.next
            index += 1
        return index

class Queue:
    l = list()

    def enqueue(self, value):
        self.l.add(value)

    def dequeue(self):
        v = self.l.head.data
        self.l.remove(0)
        return v

class Stack:
    l = list()

    def push(self, value):
        self.l.add(value)

    def pop(self):
        i = self.l.head
        value = self.l.remove(self.l.length-1)
        return value

def testList():
    l = list()
    l.add(3)
    l.add(5)
    l.add(7)
    l.remove(1)
    l.print() # Should print [3 7 ]

def testQueue():
    q = Queue()
    q.enqueue(3)
    q.enqueue(5)
    q.enqueue(7)
    print(q.dequeue()) # Should print 3

def testStack():
    s = Stack()
    s.push(3)
    s.push(5)
    s.push(7)
    print(s.pop()) # Should print 7

def testLinearSearch():
    l = list()
    l.add(3)
    l.add(5)
    l.add(7)
    print(l.linear_search(5)) # Should print 1

testList()
testQueue()
testStack()
testLinearSearch()