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
    ll.append(pair)
    # Привязка ссылки
    return ll


def push_front(ll, pair):
    ll.insert(0, pair)
    # Привязка ссылки
    return ll


if __name__ == '__main__':

    # Какие-то данные
    some_data = {'obj1': 'Ivan', 'obj2': 23423, 'obj3': {}, 'obj4': None}




