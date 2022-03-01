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

        new_pair = create_dp(item)

        # C учетом смены ссылок head, last
        if position == 1 and self.counter == 1:
            self.head = new_pair
            set_next(self.head, self.last)
            set_prev(self.last, self.head)
        elif position == 1 and self.counter > 1:
            set_next(new_pair, self.head)
            set_prev(self.head, new_pair)
            self.head = new_pair
        elif position == 2 and self.counter == 2:
            set_next(new_pair, self.last)
            set_prev(self.last, new_pair)
            set_next(self.head, new_pair)
            set_prev(new_pair, self.head)
        else:
            current = self.head
            while position:
                position -= 1
                if position == 1 and get_next(current) is not None:
                    set_next(new_pair, get_next(current))
                    set_prev(get_next(current), new_pair)
                    set_next(current, new_pair)
                    set_prev(new_pair, current)
                    break
                if position == 1 and get_next(current) is None:
                    set_next(new_pair, self.last)
                    set_prev(self.last, new_pair)
                    set_next(current, new_pair)
                    set_prev(new_pair, current)
                current = get_next(current)
            self.counter += 1
        return self

    # Удаление позиции
    def delete(self, position):
        if position < 1:
            return print("Invalid position!")
        if position > self.counter:
            return print("Position out of range")

        # C учетом смены ссылок head, last
        if position == 1 and self.counter == 1:
            self.head = self.last = None
        elif position == 1 and self.counter == 2:
            self.head = self.last
            set_next(self.head, None)
            set_prev(self.last, None)
        elif position == 2 and self.counter == 2:
            set_next(self.head, None)
            self.last = self.head
            set_prev(self.last, None)
        elif position == self.counter:
            self.pop()
        elif position == 1:
            self.remove()
        else:
            current = self.head
            prev = self.head
            while position - 1:
                position -= 1
                prev = current
                current = get_next(current)
            set_next(prev, get_next(current))
            set_prev(get_next(current), prev)
            set_second(current, None)
            self.counter -= 1
        return self

    # Получение элемента
    def get(self, position):
        if position < 1:
            return print("Invalid position!")
        if position > self.counter:
            return print("Position out of range")
        current = self.head
        while position:
            item = current
            current = get_next(current)
            position -= 1
        return item

    def iter_ll(self):
        current = self.head
        while current:
            item_val = current
            current = set_next(current)
            yield item_val

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
    dll.push(4)
    dll.push(5)
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

    print()

    dll.insert(4, 5)
    dll.print_dll()

    print()

    dll.delete(5)
    dll.print_dll()

    print()

    print(dll.get(4))

