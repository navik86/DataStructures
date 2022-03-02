from double_pair import *


# push, pop, empty, size, top
class Stack:
    def __init__(self):
        self.top = None
        self.size = -1

    # [..], [..], [..] <- [..]
    def push(self, item):
        new_pair = create_dp(item)
        if self.size == -1:
            self.top = new_pair
        else:
            set_next(self.top, new_pair)
            set_prev(new_pair, self.top)
            self.top = new_pair
        self.size += 1

    # [..], [..], [..] -> [..]
    def pop(self):
        if self.size == -1:
            return
        elif self.size == 0:
            self.top = None
        else:
            self.top = get_prev(self.top)
            set_next(self.top, None)
        self.size -= 1

    def print_dll(self):
        if self.size == 0:
            return
        current = self.top
        a = []
        while current:
            # print(get_data(current), end=' ')
            a.append(get_data(current))
            current = get_prev(current)
        [print(i, end=' ') for i in reversed(a)]


if __name__ == '__main__':

    st = Stack()
    st.push(1)
    st.push(2)
    st.push(3)

    st.print_dll()
    print()

    st.pop()
    st.print_dll()