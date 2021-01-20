import unittest
from list import List
from queue import Queue
from stack import Stack

class TestADTs(unittest.TestCase):
    def test_list(self):
        """ Making sure our implementation of list matches python's """
        mylist = List()
        pylist = []
        self.assertEqual(str(mylist), str(pylist))

        for i in range(10, 20, 2):
            mylist.add(i)
            pylist.append(i)
            self.assertEqual(str(mylist), str(pylist))

    def test_queue(self):
        q = Queue()
        q.enqueue(3)
        q.enqueue(5)
        q.enqueue(7)
        self.assertEqual(3, q.dequeue())
        self.assertEqual(5, q.dequeue())
        self.assertEqual(7, q.dequeue())

    def test_stack(self):
        s = Stack()
        s.push(3)
        s.push(5)
        s.push(7)
        self.assertEqual(7, s.pop())
        self.assertEqual(5, s.pop())
        self.assertEqual(3, s.pop())

    def test_linearsearch(self):
        l = List()
        l.add(3)
        l.add(5)
        l.add(7)
        self.assertEqual(1,l.linear_search(5))
        self.assertEqual(0,l.linear_search(3))
        self.assertEqual(2,l.linear_search(7))

if __name__ == '__main__':
    unittest.main()
