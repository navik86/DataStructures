from unittest import TestCase
from heap import *


class HeapTestCase(TestCase):

    def test_create_heap(self):
        ln1 = MyObject(1)
        ln2 = MyObject(4)
        ln3 = MyObject(7)
        ln4 = MyObject(9)
        ln5 = MyObject(15)

        list_obj = [ln5, ln2, ln3, ln1, ln4]
        list_int = [53, 32, 23, 43, 2]
        list_str = ['Vlad', 'Ivan', 'Oleg', 'Natasha', 'Elena']

        my_heap = MyHeap(list_obj, min_heap)
        my_heap2 = MyHeap(list_int)
        my_heap3 = MyHeap(list_str)

        assert my_heap.data[0] == ln1
        assert my_heap2.data[0] == 2
        assert my_heap3.data[0] == 'Elena'

    def test_push(self):

        ln1 = MyObject(1)
        ln2 = MyObject(4)
        ln3 = MyObject(7)
        ln4 = MyObject(9)
        ln5 = MyObject(15)
        ln6 = MyObject(3)

        list_obj = [ln5, ln2, ln3, ln1, ln4]
        list_int = [53, 32, 23, 43, 2]
        list_str = ['Vlad', 'Ivan', 'Oleg', 'Natasha', 'Elena']

        my_heap = MyHeap(list_obj, min_heap)
        my_heap2 = MyHeap(list_int)
        my_heap3 = MyHeap(list_str)

        push(my_heap, ln6)
        push(my_heap2, 1)
        push(my_heap3, 'Vladimir')

        assert my_heap.data[0] == ln1
        assert my_heap2.data[0] == 1
        assert my_heap3.data[0] == 'Elena'

    def test_pop(self):

        ln1 = MyObject(1)
        ln2 = MyObject(4)
        ln3 = MyObject(7)
        ln4 = MyObject(9)
        ln5 = MyObject(15)

        list_obj = [ln5, ln2, ln3, ln1, ln4]
        list_int = [53, 32, 23, 43, 2]
        list_str = ['Vlad', 'Ivan', 'Oleg', 'Natasha', 'Elena']

        my_heap = MyHeap(list_obj, min_heap)
        my_heap2 = MyHeap(list_int)
        my_heap3 = MyHeap(list_str)

        # my_heap [1, 4, 7, 15, 9]
        # my_heap2 [2, 32, 23, 43, 53]
        # my_heap3 ['Elena', 'Ivan', 'Oleg', 'Natasha', 'Vlad']

        pop(my_heap)
        pop(my_heap2)
        pop(my_heap3)

        # my_heap [4, 9, 7, 15]
        # my_heap2 [23, 32, 53, 43]
        # my_heap3 ['Ivan', 'Natasha', 'Oleg', 'Vlad']

        assert my_heap.data[0] == ln2
        assert my_heap2.data[0] == 23
        assert my_heap3.data[0] == 'Ivan'