from list_based_adt import List

class Queue:
    l = List()

    def enqueue(self, value):
        self.l.add(value)

    def dequeue(self):
        v = self.l.head.data
        self.l.remove(0)
        return v


def testQueue():
    q = Queue()
    q.enqueue(3)
    q.enqueue(5)
    q.enqueue(7)
    print(q.dequeue()) # Should print 3

if __name__ == "__main__":
    help(Queue)
    testQueue()