import unittest
from list import List
from queue import Queue
from stack import Stack
from static_list import ArrayList
from static_queue import CircularQueue
from static_stack import ArrayStack

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
        self.assertEqual(None, q.dequeue())

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

    def test_static_list(self):
        l = ArrayList(4)
        self.assertEqual(-1, l.delete(0))
        print("I expect an error message above")
        for i in range(3, 8, 2):
            l.append(i)
        self.assertEqual(-1, l.delete(10))
        print("I expect an error message above")
        self.assertEqual(0, l.delete(3))
        self.assertEqual(2, l.delete(7))
        self.assertEqual(1, l.delete(5))
        self.assertEqual(-1, l.delete(3))
        print("I expect an error message above")
        for i in range(7):
            l.append(i)
        print("I expect three error messages above")

    def test_circular_queue(self):
        """ test method for the circular queue """
        print("Testing the stack")
        q = CircularQueue(4)
        self.assertEqual(-1, q.dequeue())
        print("I expect an empty error above")
        for i in range(3, 8, 2):
            q.enqueue(i)
        self.assertEqual(3, q.dequeue())
        self.assertEqual(5, q.dequeue())
        self.assertEqual(7, q.dequeue())
        self.assertEqual(-1, q.dequeue())
        print("I expect an error message above")
        for i in range(7):
            q.enqueue(i)
        print("I expect three error messages above")

    def test_static_stack(self):
        """ test method for the Stack class """
        print("Testing the stack")
        s = ArrayStack(4)
        self.assertEqual(None, s.pop())
        print("I expect an empty error above")
        for i in range(3, 8, 2):
            s.push(i)
        self.assertEqual(7, s.pop())
        self.assertEqual(5, s.pop())
        self.assertEqual(3, s.pop())
        self.assertEqual(None, s.pop())
        print("I expect empty error above")
        for i in range(7):
            s.push(i)
        print("I expect three full error above")

if __name__ == '__main__':
    unittest.main()
