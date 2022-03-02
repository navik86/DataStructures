from double_pair import *
from linked_list import *


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.counter = -1

    def push(self, item):
        new_pair = create_dp(item)
        if self.counter == -1:
            self.head = self.last = new_pair
        else:
            set_next(new_pair, self.head)
            set_prev(self.head, new_pair)
            self.head = new_pair
            if self.counter == 0:
                set_next(self.head, self.last)
                set_prev(self.last, self.head)
        self.counter += 1

    def prepend(self, item):
        self.push(item)
        return self

    def append(self, item):
        new_pair = create_dp(item)
        if self.head is None:
            self.head = self.last = new_pair
        else:
            set_prev(new_pair, self.last)
            set_next(self.last, new_pair)
            self.last = new_pair
        self.counter += 1

    def remove(self):
        if self.head is None:
            return
        else:
            if self.counter == 0:
                self.head = self.last = None
            else:
                self.head = get_next(self.head)
                set_prev(self.head, None)
                if self.counter == 1:
                    self.head = self.last
        self.counter -= 1

    def pop(self):
        if self.head is None:
            return
        else:
            if self.counter == 0:
                self.head = self.last = None
            else:
                current = self.head
                while get_next(get_next(current)):
                    current = get_next(current)
                self.last = current
                set_next(current, None)
            self.counter -= 1

    def insert(self, position, item):
        if position < 0:
            return print("Invalid position!")
        if position > self.counter:
            return print("Position out of range")

        new_pair = create_dp(item)

        # Binding head, last
        if position == 0:
            self.push(item)
        else:
            current = self.head
            while position:
                position -= 1
                if position == 0 and get_next(current) is not None:
                    set_next(new_pair, get_next(current))
                    set_prev(get_next(current), new_pair)
                    set_next(current, new_pair)
                    set_prev(new_pair, current)
                    break
                if position == 0 and get_next(current) is None:
                    set_next(new_pair, self.last)
                    set_prev(self.last, new_pair)
                    set_next(current, new_pair)
                    set_prev(new_pair, current)
                current = get_next(current)
            self.counter += 1
        return self

    def delete(self, position):
        if position < 0:
            return print("Invalid position!")
        if position > self.counter:
            return print("Position out of range")

        # Binding head, last
        if position == 0:
            self.remove()
        else:
            current = self.head
            prev = self.head
            while position:
                if position == 1 and self.counter == 1:
                    set_next(self.head, None)
                    self.last = self.head
                position -= 1
                prev = current
                current = get_next(current)
            set_next(prev, get_next(current))
            set_prev(get_next(current), prev)
            self.counter -= 1

    def get(self, position):
        if position < 0:
            return print("Invalid position!")
        if position > self.counter:
            return print("Position out of range")
        current = self.head
        while position !=-1:
            item = current
            current = get_next(current)
            position -= 1
        return item

    def iter_ll(self):
        current = self.head
        while current:
            item_val = current
            current = get_next(current)
            yield item_val

    def print_list(self):
        if self.counter == -1:
            return print('There are no data')
        current = self.head
        while current:
            print(f'{get_data(current)} -> ', end=' ')
            current = get_next(current)


if __name__ == '__main__':

    dll = DoubleLinkedList()
    dll.push(1)
    dll.push(2)
    dll.push(3)
    dll.push(4)
    dll.push(5)
    dll.print_list()
    print()

    dll.append(0)
    dll.print_list()
    print()

    dll.remove()
    dll.print_list()
    print()

    # print(get_next(dll.last))
    # print(get_prev(dll.last))

    dll.pop()
    dll.print_list()
    print()

    dll.insert(1, 9)
    dll.print_list()
    print()

    # print(get_prev(dll.head))
    # print(get_next(dll.head))
    # print(get_prev(dll.last))
    # print(get_next(dll.last))

    dll.delete(3)
    dll.print_list()
    print()

    # print(get_prev(dll.head))
    # print(get_next(dll.head))
    # print(get_prev(dll.last))
    # print(get_next(dll.last))
    # print(dll.last)

    print(dll.get(3))
