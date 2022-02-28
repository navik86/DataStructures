from double_pair import *


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.counter = 0

    def push(self, item):
        new_pair = create_dp(item)
        if self.counter == 0:
            self.head = self.last = new_pair
        elif get_next(self.head) is None:
            self.head = new_pair
            set_next(self.head, self.last)
            set_prev(self.last, self.head)
        else:
            set_next(new_pair, self.head)
            self.head = new_pair
        self.counter += 1
        return self

    def print_dll(self):
        if self.counter == 0:
            return
        current = self.head
        while get_next(current):
            current = get_next(current)
            print(f'{get_data(current)} -> ', end=' ')


if __name__ == '__main__':

    dll = DoubleLinkedList()
    dll.push(1)
    dll.push(2)
    dll.push(3)

    dll.print_dll()