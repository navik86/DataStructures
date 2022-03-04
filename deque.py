from double_linked_list import *


# insertFront, insertRear, deleteFront, deleteRear
# getFront, getRear, isEmpty, size
class MyDeque:
    def __init__(self):
        self.dll = DoubleLinkedList()

    # [new] -> [front], [..], [..], [rear]
    def insertFront(self, item):
        self.dll.push(item)

    # [front], [..], [..], [rear] <- [new]
    def insertRear(self, item):
        self.dll.append(item)

    def deleteFront(self):
        self.dll.remove()

    def deleteRear(self):
        self.dll.pop()

    def getFront(self):
        return self.dll.head

    def getRear(self):
        return self.dll.last

    def isEmpty(self):
        if self.size == -1:
            return True
        else:
            return False

    def size(self):
        a = self.dll.counter + 1
        return a

    def __iter__(self):
        return self.dll.__iter__()
