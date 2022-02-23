def create_pair(a=None, b=None):
    return [a, b]


def pair_first(pair):
    return pair[0]


def pair_second(pair):
    return pair[1]


def set_first():
    pass


def set_second():
    pass


if __name__ == '__main__':

    p = create_pair()

    print(pair_first(p), pair_second(p))