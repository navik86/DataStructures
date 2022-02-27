from pair import *


# push, pop, append, prepend, (insert, delete, get) - по позиции
class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.counter = 0

    # Добавление элемента в начало
    def push(self, item):
        new_pair = create_pair(item)
        if self.head is None:
            self.head = self.last = new_pair
        elif pair_second(self.head) is None:
            self.head = new_pair
            set_second(self.head, self.last)
        else:
            set_second(new_pair, self.head)
            self.head = new_pair
        self.counter += 1
        return self

    # Добавление элемента в конец
    def append(self, item):
        new_pair = create_pair(item)
        if self.head is None:
            self.head = self.last = new_pair
        else:
            set_second(self.last, new_pair)
            self.last = new_pair
        self.counter += 1
        return self

    # Удалить первый элемент
    def remove(self):
        if self.head is None:
            return
        elif self.counter == 1:
            self.head = self.last = None
        elif self.counter == 2:
            self.head = None
        else:
            self.head = pair_second(self.head)
        self.counter -= 1
        return self

    # Удалить последний элемент
    def pop(self):
        if self.head is None:
            return
        elif self.counter == 1:
            self.head = self.last = None
        elif self.counter == 2:
            self.last = None
        else:
            current = self.head
            while pair_second(pair_second(current)):
                current = pair_second(current)
            self.last = set_second(current, None)
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
        elif position == 2 and self.counter == 2:
            set_second(self.head, None)
            self.last = self.head
        elif position == self.counter:
            self.pop()
        else:
            current = self.head
            prev = self.head
            while position:
                position -= 1
                prev = current
                current = pair_second(current)
            set_second(prev, pair_second(current))
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
            current = pair_second(current)
            position -= 1
        return item

    def iter_ll(self):
        current = self.head
        while current:
            item_val = current
            current = pair_second(current)
            yield item_val

    def print_list(self):
        current = self.head
        last = None
        while last != self.head:
            while pair_second(current) != last:
                current = pair_second(current)
            last = current
            print(last)
            current = self.head


if __name__ == '__main__':

    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.print_list()

    ll.append(9)
    ll.print_list()

    ll.remove()
    ll.print_list()

    ll.pop()
    ll.print_list()

    ll.insert(4, 6)
    ll.print_list()

    print(ll.get(5))

    ll.delete(3)
    ll.print_list()
