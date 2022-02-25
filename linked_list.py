from obj_pair import *

# push, pop, append, prepend, (insert, delete, get) - по позиции
class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        # self.counter = 0

    def push(self, item):
        new_pair = create_pair(item)
        if self.head is None:
            self.head = self.tail = new_pair
        elif pair_second(self.head) is None:
            self.head = new_pair
            set_second(self.head, self.tail)
        else:
            set_second(new_pair, self.head)
            self.head = new_pair
        # self.counter += 1
        return self


    # def push_back(ll, new_pair):
    #     if ll.head is None:
    #         ll.head = ll.tail = new_pair
    #     else:
    #         set_second(ll.tail, new_pair)
    #         ll.tail = new_pair
    #     ll.counter += 1
    #     return ll
    #
    #
    # def pop_front(ll):
    #     if ll.head is None:
    #         return
    #     elif ll.counter == 1:
    #         ll.head = ll.tail = None
    #     elif ll.counter == 2:
    #         ll.head = None
    #     else:
    #         ll.head = pair_second(ll.head)
    #     ll.counter -= 1
    #     return ll
    #
    #
    # def pop_back(ll):
    #     if ll.head is None:
    #         return
    #     elif ll.counter == 1:
    #         ll.head = ll.tail = None
    #     elif ll.counter == 2:
    #         ll.tail = None
    #     else:
    #         current = ll.head
    #         while pair_second(pair_second(current)):
    #             current = pair_second(current)
    #         set_second(current, None)
    #     ll.counter -= 1
    #     return ll
    #
    #
    # def iter_ll(ll):
    #     current = ll.head
    #     while current:
    #         item_val = current
    #         current = pair_second(current)
    #         yield item_val


    # def print_list(ll):
    #     for node in iter_ll(ll):
    #         print(node, end=' ')


    # def print_list(ll):
    #     current = ll.head
    #     last = None
    #     while last != ll.head:
    #         while pair_second(current) != last:
    #             current = pair_second(current)
    #         last = current
    #         print(last)
    #         current = ll.head
    #
    #
    # # x, y - значения ноды
    # def swap_pair(ll, x, y):
    #     if ll.counter == 0 or ll.counter == 1:
    #         return
    #     elif x == ll.head and y == ll.tail:
    #         pass
    #     elif x == ll.tail and y == ll.head:
    #         pass
    #     else:
    #         pass
    #     return ll
    #
    #
    # def my_sort(ll):
    #
    #     current = ll.head
    #     index = None
    #
    #     if ll.counter == 0 or ll.counter == 1:
    #         return
    #
    #     try:
    #         if ll.counter > 1:
    #             while current:
    #                 index = pair_second(current)
    #                 while index:
    #                     if pair_first(current) > pair_first(index):
    #                         temp = pair_first(current)
    #                         set_first(current, pair_first(index))
    #                         set_first(index, temp)
    #                     index = pair_second(index)
    #                 current = pair_second(current)
    #     except TypeError:
    #         print('Node does not have int or string')
    #     else:
    #         return ll


if __name__ == '__main__':

    ll = LinkedList()
    ll.push_front(1)


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

