from unittest import TestCase
from double_linked_list import *
from double_pair import *


class LinkedListTestCase(TestCase):

    def test_push(self):

        dll = DoubleLinkedList()

        dll.push(1)
        assert list(dll) == [1]
        dll.push(5)
        assert list(dll) == [5, 1]
        dll.push(6)
        assert list(dll) == [6, 5, 1]
        dll.push(8)
        assert list(dll) == [8, 6, 5, 1]

    def test_append(self):

        dll = DoubleLinkedList()

        dll.append(1)
        assert list(dll) == [1]
        dll.append(5)
        assert list(dll) == [1, 5]
        dll.append(6)
        assert list(dll) == [1, 5, 6]

    def test_remove(self):

        dll = DoubleLinkedList()
        dll.push(1)
        dll.push(2)
        dll.push(3)

        dll.remove()
        assert list(dll) == [2, 1]
        dll.remove()
        assert list(dll) == [1]
        dll.remove()
        assert list(dll) == []

    def test_pop(self):

        dll = DoubleLinkedList()
        dll.push(1)
        dll.push(2)
        dll.push(3)

        dll.pop()
        assert list(dll) == [3, 2]
        dll.pop()
        assert list(dll) == [3]
        dll.pop()
        assert list(dll) == []

    def test_insert(self):

        dll = DoubleLinkedList()

        dll.insert(0, 1)
        assert list(dll) == [1]
        dll.insert(0, 2)
        assert list(dll) == [2, 1]
        dll.insert(1, 3)
        assert list(dll) == [2, 3, 1]
        dll.insert(2, 4)
        assert list(dll) == [2, 3, 4, 1]

    def test_delete(self):

        dll = DoubleLinkedList()
        dll.push(1)
        dll.push(2)
        dll.push(3)
        dll.push(4)
        dll.push(5)

        dll.delete(0)
        assert list(dll) == [4, 3, 2, 1]
        dll.delete(3)
        assert list(dll) == [4, 3, 2]
        dll.delete(1)
        assert list(dll) == [4, 2]
        dll.delete(0)
        assert list(dll) == [2]
        dll.delete(0)
        assert list(dll) == []

    def test_get(self):

        dll = DoubleLinkedList()
        dll.push(1)
        dll.push(2)
        dll.push(3)

        b = pair_first(dll.get(0))
        assert b == 3
        c = pair_first(dll.get(1))
        assert c == 2
        d = pair_first(dll.get(2))
        assert d == 1

    def test_iter_dll(self):

        dll = DoubleLinkedList()
        dll.push(1)
        dll.push(2)
        dll.push(3)

        a = [pair_first(x) for x in dll.iter_dll()]
        assert a == [3, 2, 1]

