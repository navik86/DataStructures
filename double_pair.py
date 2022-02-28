from obj_pair import *


class DoublePair:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a}"


def create_dp(a):
    return DoublePair(a, Pair())


def get_data(pair):
    return pair.a


def get_ref_pair(pair):
    return pair.b


def get_prev(pair):
    return pair.b.a


def get_next(pair):
    return pair.b.b


def set_data(pair, data):
    pair.a = data


def set_ref_pair(pair, ref):
    pair.b = ref


def set_prev(pair, prev):
    pair.b.a = prev


def set_next(pair, next):
    pair.b.b = next


