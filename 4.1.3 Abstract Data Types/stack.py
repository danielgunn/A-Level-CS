from list import List

class Stack:
    l = List()

    def push(self, value):
        self.l.add(value)

    def pop(self):
        if self.l.length == 0:
            return None
        else:
            i = self.l.head
            value = self.l.remove(self.l.length-1)
            return value

if __name__ == "__main__":
    help(Stack)