from heapq import *
from typing import List


class MyObject:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return f"{self.val}"

    def __eq__(self, other):
        return self.val == other.val


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
