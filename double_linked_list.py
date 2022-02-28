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

    # Удалить первый элемент
    def remove(self):
        if self.counter == 0:
            return
        elif self.counter == 1:
            self.head = self.last = None
        elif self.counter == 2:
            self.head = None
        else:
            self.head = get_next(self.head)
            set_prev(self.head, None)
        self.counter -= 1
        return self

    # Удалить последний элемент
    def pop(self):
        if self.counter == 0:
            return
        elif self.counter == 1:
            self.head = self.last = None
        else:
            self.last = get_prev(self.last)
            set_next(self.last, None)
        self.counter -= 1
        return self

    # Вставляет элемент в указанную позицию, отсчет
    def insert(self, position, item):
        # Проверка позиции
        if position < 1:
            return print("Invalid position!")
        if position > self.counter:
            return print("Position out of range")

        new_pair = create_pair(item)

        # C учетом смены ссылок head, last
        if position == 1 and self.counter == 1:
            self.head = new_pair
            set_second(self.head, self.last)
        elif position == 1 and self.counter > 1:
            set_second(new_pair, self.head)
            self.head = new_pair
        elif position == 2 and self.counter == 2:
            set_second(new_pair, self.last)
            set_second(self.head, new_pair)
        else:
            current = self.head
            while position:
                position -= 1
                if position == 1 and pair_second(current) is not None:
                    set_second(new_pair, pair_second(current))
                    set_second(current, new_pair)
                    break
                if position == 1 and pair_second(current) is None:
                    set_second(new_pair, self.last)
                    set_second(current, new_pair)
                    pass
                current = pair_second(current)
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
    dll.print_dll()
    print()

    dll.append(4)
    dll.print_dll()
    print()

    dll.remove()
    dll.print_dll()
    print()

    dll.pop()
    dll.print_dll()
