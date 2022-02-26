from obj_pair import *


# push, pop, append, prepend, (insert, delete, get) - по позиции
class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.counter = 0

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

    def append(self, item):
        new_pair = create_pair(item)
        if self.head is None:
            self.head = self.last = new_pair
        else:
            set_second(self.last, new_pair)
            self.last = new_pair
        self.counter += 1
        return self

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
            set_second(current, None)
        self.counter -= 1
        return self

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

    self = LinkedList()
    self.push(1)


    # cf = create_first('f1')
    # cf2 = create_first('f2')
    # cf3 = create_first('f3')
    # cf4 = create_first('f4')
    # cs = create_second(None)
    # cp = create_pair(cf, cs)
    # cp2 = create_pair(cf2, cs)
    # cp3 = create_pair(cf3, cs)
    # cp4 = create_pair(cf4, cs)
    #
    # my_ll = create_ll(create_array())
    # push_front(my_ll, cp)
    # push_front(my_ll, cp2)
    # push_front(my_ll, cp3)
    # push_back(my_ll, cp4)
    #
    # # print('Убрать последний')
    # # pop_back(my_ll)
    #
    # print_list(my_ll)
    #
    # my_sort(my_ll)
    #
    # print_list(my_ll)

