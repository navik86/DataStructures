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
    setattr(array, 'head', 'None')
    setattr(array, 'tail', 'None')
    return array


def push_back(ll, pair):
    if ll.head is None:
        ll.head = ll.tail = pair
    elif pair_second(ll.head) is None:
        pair_second(ll.head) = ll.tail
        ll.tail = pair
    else:
        pair_second(ll.tail) = pair
        ll.tail = pair
    return ll


def push_front(ll, pair):
    if ll.head is None:
        ll.head = ll.tail = pair
    elif len(ll) == 1:
        pair_second(ll.head) = ll.tail
        ll.head = pair
    else:
        pair_second(pair)= ll.head
        ll.head = pair
    return ll


def pop_back(ll):
    if ll.head is None:
        return
    elif len(ll) == 1:
        ll.head = ll.tail = None
    else:
        current = ll.head
        while pair_second(current) != ll.tail:
            current = current.next
        pair_second(current) = None
        ll.tail = current
    return ll


def pop_front(ll):
    return ll


def swap_pair(ll, x, y):
    return ll


def iter_ll(ll):
    current = ll.head
    while current:
        item_val = pair_first(current)
        current = pair_second(current)
        yield item_val


def print_list(ll):
    for node in iter_ll(ll):
        print(node, end=' ')


def my_sort(ll):
    return ll


if __name__ == '__main__':

    # Просто данные для заполнения, который
    # Объекты first
    list_f = [create_first(f'f{i}') for i in range(1, 5)]
    # list_s = [create_second(f's{i}') for i in range(1, 5)]

    # Создаем pairs
    list_p = [create_pair() for i in range(1, 5)]

    # Добавляем объекты в пары
    for i in range(4):
        set_first(list_p[i], list_f[i])
        # set_second(list_p[i], list_s[i])

    my_ll = create_ll(create_array())
    push_front(my_ll, list_p[0])





