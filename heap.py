from heapq import *
from typing import List


class MyObject:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return f"{self.val}"


class MyHeap:
    def __init__(self, lists: List[MyObject], func=None):

        if func:
            setattr(MyObject, "__lt__", func)

        if lists:
            self._data = lists
            heapify(self._data)
        else:
            self._data = []

    def push(self, item):
        heappush(self._data, item)

    def pop(self):
        return heappop(self._data)


min_heap = lambda self, other: self.val < other.val
max_heap = lambda self, other: self.val > other.val


if __name__ == '__main__':

    ln1 = MyObject(1)
    ln2 = MyObject(4)
    ln3 = MyObject(7)
    ln4 = MyObject(9)
    ln5 = MyObject(15)

    list_obj = [ln5, ln2, ln3, ln1, ln4]
    list_int = [53, 32, 23, 43, 2]
    list_str = ['Vlad', 'Ivan', 'Oleg', 'Natasha', 'Elena']
    my_heap = MyHeap(list_obj, min_heap)
    print(my_heap._data)
    my_heap2 = MyHeap(list_int)
    print(my_heap2._data)
    my_heap3 = MyHeap(list_str)
    print(my_heap3._data)
