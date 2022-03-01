from double_pair import *


# push, pop, empty, size, top
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    # [..], [..], [..] <- [..]
    def push(self, item):
        new_pair = create_dp(item)
        if self.size == 0:
            self.top = new_pair
        else:
            set_next(self.top, new_pair)
            set_prev(new_pair, self.top)
            self.top = new_pair
        self.size += 1


if __name__ == '__main__':

    st = Stack()
    st.push(1)
    st.push(2)