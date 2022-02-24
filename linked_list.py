from collections import UserList


def create_pair(a=None, b=None):
    return [a, b]


def pair_first(pair):
    return pair[0]


def pair_second(pair):
    return pair[1]


def set_first(pair, first):
    pair[0] = first
    return pair


def set_second(pair, second):
    pair[1] = second
    return pair


def create_first(obj):
    first = obj
    return first


def create_second(obj):
    second = obj
    return second


# Создаем связанный список из какой-то коллекции
def create_ll(array):
    ll = array
    return ll


# Пользовательская коллекция с доп. атрибутами
def create_array():
    array = UserList()
    array.head = None
    array.tail = None
    array.counter = 0
    return array


def push_front(ll, new_pair):
    if ll.head is None:
        ll.head = ll.tail = new_pair
    elif pair_second(ll.head) is None:
        ll.head = new_pair
        set_second(ll.head, ll.tail)
    else:
        set_second(new_pair, ll.head)
        ll.head = new_pair
    ll.counter += 1
    return ll


def push_back(ll, new_pair):
    if ll.head is None:
        ll.head = ll.tail = new_pair
    else:
        set_second(ll.tail, new_pair)
        ll.tail = new_pair
    ll.counter += 1
    return ll


def pop_back(ll):
    return ll


def pop_front(ll):
    return ll


def swap_pair(ll, x, y):
    return ll


def iter_ll(ll):
    current = ll.head
    while current:
        item_val = current
        current = pair_second(current)
        yield item_val


def print_list(ll):
    for node in iter_ll(ll):
        print(node, end=' ')


# def print_list(ll):
#     current = ll.head
#     last = None
#     while last != ll.head:
#         while pair_second(current) != last:
#             current = pair_second(current)
#         last = current
#         print(last)
#         current = ll.head


def my_sort(ll):
    return ll


if __name__ == '__main__':

    cf = create_first('f1')
    cf2 = create_first('f2')
    cf3 = create_first('f3')
    cf4 = create_first('f4')
    cs = create_second(None)
    cp = create_pair(cf, cs)
    cp2 = create_pair(cf2, cs)
    cp3 = create_pair(cf3, cs)
    cp4 = create_pair(cf4, cs)

    my_ll = create_ll(create_array())
    push_front(my_ll, cp)
    push_front(my_ll, cp2)
    push_front(my_ll, cp3)
    push_back(my_ll, cp4)

    print_list(my_ll)


