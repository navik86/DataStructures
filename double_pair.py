from obj_pair import *


class DoublePair:
    def __init__(self, data=None, ref=None):
        self.data = data
        self.ref = ref


def create_dp(data):
    a = create_pair(data)
    b = create_pair()
    pair_second(b)
    return DoublePair(a, b)


def get_data(double_pair):
    return pair_first(double_pair.data)


def get_ref_pair(double_pair):
    return double_pair.ref


def get_prev(pair):
    return prev


def get_next(pair):
    return next


def set_data(pair, data):
    pair.a = data


def set_ref_pair(pair, ref):
    pair.b = ref


def set_prev(pair, prev):
    pair.b.a = prev


def set_next(pair, next):
    pair.b.b = next


if __name__ == '__main__':

    dp1 = create_dp(1)

    print(get_data(dp1))


