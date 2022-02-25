class Pair:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b


def create_pair(a=None, b=None):
    return Pair(a, b)


def pair_first(pair):
    return pair.a


def pair_second(pair):
    return pair.b


def set_first(pair, first):
    pair.a = first


def set_second(pair, second):
    pair.b = second


if __name__ == '__main__':

    p = Pair()