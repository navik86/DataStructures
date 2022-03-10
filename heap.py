from typing import List


class MyObject:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return f"{self.val}"

    def __eq__(self, other):
        return self.val == other.val


min_heap = lambda self, other: self.val <= other.val


class MyHeap:
    def __init__(self, lists: List[MyObject], func=None):
        if func:
            setattr(MyObject, "__lt__", func)

        if lists:
            self.data = lists
            list_to_heap(self.data)
            self.size = len(self.data) - 1
        else:
            self.data = []
            self.size = - 1

        self.min = self.data[0]


def parent(i):
    return (i - 1) // 2


def leftChild(i):
    return (2 * i) + 1


def rightChild(i):
    return (2 * i) + 2


def swap(list_heap, i, j):
    temp = list_heap[i]
    list_heap[i] = list_heap[j]
    list_heap[j] = temp


def list_to_heap(list_heap):
    n = len(list_heap)
    for i in reversed(range(n // 2)):
        shiftDown(list_heap, i)


def push(heap, item):
    heap.size += 1
    heap.data.append(item)
    shiftUp(heap.data, heap.size)


def pop(heap):
    result = heap.data[0]
    heap.data[0] = heap.data[heap.size]
    heap.data.pop()
    heap.size -= 1
    shiftDown(heap.data, 0)
    return result


def shiftUp(list_heap, i):
    while i > 0 and list_heap[parent(i)] > list_heap[i]:
        swap(list_heap, parent(i), i)
        i = parent(i)


def shiftDown(list_heap, i):
    # Находим минимум из родителя и двух потомков
    min_index = min_item(list_heap, i)

    if i != min_index:
        swap(list_heap, i, min_index)
        shiftDown(list_heap, min_index)


def min_item(list_heap, i):
    size = len(list_heap) - 1
    min_index = i

    if leftChild(i) <= size and list_heap[leftChild(i)] < list_heap[min_index]:
        min_index = leftChild(i)

    if rightChild(i) <= size and list_heap[rightChild(i)] < list_heap[min_index]:
        min_index = rightChild(i)

    return min_index
