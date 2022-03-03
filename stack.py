from linked_list import *


# push, pop, empty, size, top
class MyStack:
    def __init__(self):
        self.ll = LinkedList()

    # [..] -> [..], [..], [..]
    def push(self, item):
        self.ll.push(item)

    # [..] <- [..], [..], [..]
    def pop(self):
        self.ll.remove()

    def empty(self):
        if self.size == -1:
            return True
        else:
            return False

    def size(self):
        a = self.ll.counter + 1
        return a

    def top(self):
        return self.ll.head

    def __iter__(self):
        return self.ll.__iter__()



