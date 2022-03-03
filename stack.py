from double_pair import *


# push, pop, empty, size, top
class Stack:
    def __init__(self):
        self.top = None
        self.size = -1

    # [..] -> [..], [..], [..]
    def push(self, item):
        new_pair = create_dp(item)
        if self.size == -1:
            self.top = new_pair
        else:
            set_next(self.top, new_pair)
            set_prev(new_pair, self.top)
            self.top = new_pair
        self.size += 1

    # [..] <- [..], [..], [..]
    def pop(self):
        if self.size == -1:
            return
        else:
            if self.size == 0:
                self.top = None
            else:
                self.top = get_prev(self.top)
                set_next(self.top, None)
        self.size -= 1

    def print_stack(self):
        if self.size == -1:
            return
        current = self.top
        while current:
            print(f'{get_data(current)} -> ', end=' ')
            current = get_prev(current)

    def empty(self):
        if self.size == -1:
            return True
        else:
            return False

    def iter_st(self):
        current = self.top
        while current:
            item_val = current
            current = get_prev(current)
            yield item_val

    def __iter__(self):
        return iter(map(lambda x: (get_data(x)), self.iter_st()))
