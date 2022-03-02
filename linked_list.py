from pair import *


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.counter = -1

    def push(self, item):
        new_pair = create_pair(item)
        if self.counter == -1:
            self.head = self.last = new_pair
        else:
            set_second(new_pair, self.head)
            self.head = new_pair
            if self.counter == 0:
                set_second(self.head, self.last)
        self.counter += 1
        return self

    def prepend(self, item):
        self.push(item)
        return self

    def append(self, item):
        new_pair = create_pair(item)
        if self.head is None:
            self.head = self.last = new_pair
        else:
            if self.counter == 0:
                set_second(self.head, new_pair)
            else:
                set_second(self.last, new_pair)
            self.last = new_pair
        self.counter += 1
        return self

    def remove(self):
        if self.head is None:
            return
        else:
            if self.counter == 0:
                self.head = self.last = None
            elif self.counter == 1:
                self.head = self.last
            else:
                self.head = pair_second(self.head)
        self.counter -= 1

    def pop(self):
        if self.head is None:
            return
        else:
            if self.counter == 0:
                self.head = self.last = None
            else:
                current = self.head
                while pair_second(pair_second(current)):
                    current = pair_second(current)
                self.last = set_second(current, None)
            self.counter -= 1

    def insert(self, position, item):
        if position < 0:
            return print("Invalid position!")
        if position > self.counter:
            return print("Position out of range")

        new_pair = create_pair(item)

        # Binding head, last
        if position == 0:
            if self.counter == 0:
                self.head = new_pair
                set_second(self.head, self.last)
            else:
                set_second(new_pair, self.head)
                self.head = new_pair
        else:
            current = self.head
            while position:
                position -= 1
                if position == 0 and pair_second(current) is not None:
                    set_second(new_pair, pair_second(current))
                    set_second(current, new_pair)
                    break
                if position == 0 and pair_second(current) is None:
                    set_second(new_pair, self.last)
                    set_second(current, new_pair)
                current = pair_second(current)
            self.counter += 1
        return self

    def delete(self, position):
        if position < 0:
            return print("Invalid position!")
        if position > self.counter:
            return print("Position out of range")

        # Binding head, last
        if position == 0:
            if self.counter == 0:
                self.head = self.last = None
            elif self.counter == 1:
                self.head = self.last
            else:
                self.remove()
        else:
            current = self.head
            prev = self.head
            while position:
                if position == 1 and self.counter == 1:
                    set_second(self.head, None)
                    self.last = self.head
                position -= 1
                prev = current
                current = pair_second(current)
            set_second(prev, pair_second(current))
            self.last = prev
            self.counter -= 1

    def get(self, position):
        if position < 0:
            return print("Invalid position!")
        if position > self.counter:
            return print("Position out of range")
        current = self.head
        while position != -1:
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
        if self.head is None:
            return print('There is no data')
        current = self.head
        while current:
            print(f'{pair_first(current)} -> ', end=' ')
            current = pair_second(current)


if __name__ == '__main__':

    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)

    ll.print_list()
    print()

    print('Добавление в конец')
    ll.append(9)

    ll.print_list()
    print()
    print(f'head {ll.head}')
    print(f'last {ll.last}')

    print('Удалить первый')
    ll.remove()
    ll.print_list()
    print()
    print(f'head {ll.head}')
    print(f'last {ll.last}')

    print('Удалить последний')
    ll.pop()
    ll.print_list()
    print()
    print(f'head {ll.head}')
    print(f'last {ll.last}')

    ll.insert(3, 6)
    ll.print_list()
    print()

    print('Удалить 4 й')
    ll.delete(4)
    ll.print_list()
    print()
    print(f'head {ll.head}')
    print(f'last {ll.last}')

    print(ll.get(3))