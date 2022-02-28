from double_pair import *


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.counter = 0

    # Добавление элемента в начало
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
            set_prev(new_pair, self.head)
        self.counter += 1
        return self

    # Добавление элемента в начало
    def prepend(self, item):
        self.push(item)
        return self

    # Добавление элемента в конец
    def append(self, item):
        new_pair = create_dp(item)
        if self.counter == 0:
            self.head = self.last = new_pair
        elif self.counter == 1:
            set_next(self.head, new_pair)
            self.last = new_pair
            set_prev(self.last, self.head)
        else:
            set_next(self.last, new_pair)
            set_prev(new_pair, self.last)
            self.last = new_pair
        self.counter += 1
        return self

    def print_dll(self):
        if self.counter == 0:
            return
        current = self.head
        while current:
            print(f'{get_data(current)}', end=' ')
            current = get_next(current)


if __name__ == '__main__':

    dll = DoubleLinkedList()
    dll.push(1)
    dll.push(2)
    dll.push(3)
    dll.append(4)

    # print(get_prev(dll.last))
    # print(get_next(dll.last))

    dll.print_dll()