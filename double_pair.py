from obj_pair import *


class DoublePair:
    def __init__(self, data=None, ref=None):
        self.data = data
        self.ref = ref

    def __str__(self):
        return f"{self.data}"


def create_dp(data):
    a = create_pair(data)
    b = create_pair()
    pair_second(b)
    return DoublePair(a, b)


# [... , ...] -> ref[... , ...]
def get_ref_pair(double_pair):
    return double_pair.ref


# [data , ...] -> [... , ...]
def get_data(double_pair):
    return pair_first(double_pair.data)


# [... , ...] -> [prev , ...]
def get_prev(double_pair):
    return pair_first(double_pair.ref)


# [... , ...] -> [... , next]
def get_next(double_pair):
    return pair_second(double_pair.ref)


# [data, ...] -> [... , ...]
def set_data(double_pair, data):
    return set_first(double_pair.data, data)


# [... , ref] - [... , ...]
def set_ref_pair(double_pair, ref):
    return set_second(double_pair.data, ref)


# [... , ...] -> [prev , ...]
def set_prev(double_pair, prev):
    set_first(double_pair.ref, prev)


# [... , ...] -> [... , next]
def set_next(double_pair, next):
    set_second(double_pair.ref, next)


if __name__ == '__main__':

    dp1 = create_dp(1)
    dp2 = create_dp(2)
    dp3 = create_dp(3)

    set_prev(dp2, dp1)
    set_next(dp2, dp3)




