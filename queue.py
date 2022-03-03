from linked_list import *


# Enqueue (push), dequeue(pop), front(), rear()
class MyQueue(LinkedList):

    append = insert = delete = get = property(doc='(!) Not available')

    def enqueue(self, item):
        self.push(item)
        return self

    def dequeue(self):
        self.pop()
        return self

    def front(self):
        return self.head

    def rear(self):
        return self.last


if __name__ == '__main__':

    my_q = MyQueue()
    my_q.enqueue(1)
    my_q.enqueue(2)
    my_q.enqueue(3)
    print(my_q.front())


