class ArrayList:
    """
    This List will not use dynamic memory allocation after constructed.
    It illustrates how one might implement a List using an Array as its backing store

    It is implemented using two lists:
    start - a list to all the values contained in the list
    free - a list of all the spots that are currently unoccupied by data


    There are three possible states:

    1) Empty:
       0 1 2 3 4 5 6          0 1 2 3 4 5  6
    P  1 2 3 4 5 6 -1         5 4 3 1 6 -1 0
    V
       ^                          ^
       Free                       Free

    2) Full:
       0 1 2 3 4 5 6          0 1 2 3 4 5  6
    P  1 2 3 4 5 6 -1         5 4 3 1 6 -1 0
    V
       ^                          ^
       Start                       Start

    3) Normal
      0 1 2  3 4  5 6
    P 2 3 -1 6 -1 4 0
    V L H O  E      L
        ^         ^
        Start     Free
    """
    
    def __init__(self, size):
        """ size -- the maximum size that the list will occupy """
        self.data = [0] * 2
        # assosciative arrays rather than a 2D array to make the code clearer
        self.pointers = [0] * size  # pointers
        self.values = [0] * size    # values
        
        # link up all the nodes of the free list
        for i in range(size):
            self.pointers[i] = i + 1
        self.pointers[size - 1] = -1

        self.start = -1  # first index of items in our list
        self.free = 0  # first index of items that are available (free)

    def append(self, value):
        """ append the value to the list """
        if self.start == -1:
            # take the free lists first item
            self.start = self.free
            self.values[self.start] = value
            self.free = self.pointers[self.free]
            self.pointers[self.start] = -1
        elif self.free == -1:
            print("no free space! cannot insert")
        else:
            # lets find the *end* of the list
            end = self.start
            while self.pointers[end] != -1:
                end = self.pointers[end]

            # put in our new value
            self.pointers[end] = self.free
            self.values[self.free] = value

            # update the free list to point to the next one
            self.free = self.pointers[self.free]

            # the next one to the end is now not pointing anywhere
            self.pointers[self.pointers[end]] = -1

    def delete(self, value):
        """ delete the value from the list, returning the index at which it once existed """
        if self.start == -1:
            print("Empty list.. nothing to delete")
            return -1
        else:
            # if the first item is the one we want to delete
            if self.values[self.start] == value:
                deleted = self.start

                self.start = self.pointers[self.start]

                # the deleted item now points to the free list
                self.pointers[deleted] = self.free
                self.free = deleted

                return deleted
            else:
                # search the list for the value (we're going to delete it)
                current = self.start
                prev = -1
                while self.values[current] != value:
                    prev = current
                    current = self.pointers[current]
                    if current == -1:
                        print("cannot delete value: not found!")
                        return -1

                # the first item might be the one we're deleting (no previous)
                if prev != -1:
                    self.pointers[prev] = self.pointers[current]

                # insert the deleted item to the beginning of the free list
                self.pointers[current] = self.free
                self.free = current

                return current

def testList():
    print("Testing the List")
    l = ArrayList(4)
    l.delete(0)
    print("I expect an empty error above")
    for i in range(3, 8, 2):
        print("Appending",i,"I expect no error")
        l.append(i)
    print("I expect not found error above and -1:", l.delete(10))
    print("I expect 0:", l.delete(3))
    print("I expect 2:", l.delete(7))
    print("I expect 1:", l.delete(5))
    print("I expect empty error above and -1:", l.delete(3))
    for i in range(7):
        l.append(i)
    print("I expect three full error above")

if __name__ == "__main__":
    help(ArrayList)
    testList()