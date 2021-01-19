from list_based_adt import List

class Stack:
    l = List()

    def push(self, value):
        self.l.add(value)

    def pop(self):
        i = self.l.head
        value = self.l.remove(self.l.length-1)
        return value


def testStack():
    s = Stack()
    s.push(3)
    s.push(5)
    s.push(7)
    print(s.pop()) # Should print 7

if __name__ == "__main__":
    help(Stack)
    testStack()