from list import List

class Queue:
    l = List()

    def enqueue(self, value):
        self.l.add(value)

    def dequeue(self):
        if self.l.is_empty():
            print("Error: dequeue attempt on empty queue")
            return None
        else:
            v = self.l.head.data
            self.l.remove(0)
            return v

if __name__ == "__main__":
    help(Queue)