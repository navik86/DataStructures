from obj_pair import *


def create_dp(data):
    links = create_pair()
    return Pair(data, links)


# [data, [... , ...]]
def get_data(double_pair):
    return pair_first(double_pair)


# [..., [prev, ...]]
def get_prev(double_pair):
    return pair_first(pair_second(double_pair))


# [..., [..., next]]
def get_next(double_pair):
    return pair_second(pair_second(double_pair))


# [data, [... , ...]]
def set_data(double_pair, data):
    return set_first(double_pair, data)


# [..., [prev, ...]]
def set_prev(double_pair, prev):
    return set_first(pair_second(double_pair), prev)


# [..., [..., next]]
def set_next(double_pair, next):
    return set_second(pair_second(double_pair), next)