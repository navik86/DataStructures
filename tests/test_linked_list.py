from unittest import TestCase
from linked_list import *
from pair import *


class LinkedListTestCase(TestCase):

    def test_push(self):

        ll = LinkedList()

        ll.push(1)
        assert list(ll) == [1]
        ll.push(5)
        assert list(ll) == [5, 1]
        ll.push(6)
        assert list(ll) == [6, 5, 1]
        ll.push(8)
        assert list(ll) == [8, 6, 5, 1]

    def test_append(self):

        ll = LinkedList()

        ll.append(1)
        assert list(ll) == [1]
        ll.append(5)
        assert list(ll) == [1, 5]
        ll.append(6)
        assert list(ll) == [1, 5, 6]

    def test_remove(self):

        ll = LinkedList()
        ll.push(1)
        ll.push(2)
        ll.push(3)

        ll.remove()
        assert list(ll) == [2, 1]
        ll.remove()
        assert list(ll) == [1]
        ll.remove()
        assert list(ll) == []

    def test_pop(self):

        ll = LinkedList()
        ll.push(1)
        ll.push(2)
        ll.push(3)

        ll.pop()
        assert list(ll) == [3, 2]
        ll.pop()
        assert list(ll) == [3]
        ll.pop()
        assert list(ll) == []

    def test_insert(self):

        ll = LinkedList()

        ll.insert(0, 1)
        assert list(ll) == [1]
        ll.insert(0, 2)
        assert list(ll) == [2, 1]
        ll.insert(1, 3)
        assert list(ll) == [2, 3, 1]
        ll.insert(2, 4)
        assert list(ll) == [2, 3, 4, 1]

    def test_delete(self):

        ll = LinkedList()
        ll.push(1)
        ll.push(2)
        ll.push(3)
        ll.push(4)
        ll.push(5)

        ll.delete(0)
        assert list(ll) == [4, 3, 2, 1]
        ll.delete(3)
        assert list(ll) == [4, 3, 2]
        ll.delete(1)
        assert list(ll) == [4, 2]
        ll.delete(0)
        assert list(ll) == [2]
        ll.delete(0)
        assert list(ll) == []

    def test_get(self):

        ll = LinkedList()
        ll.push(1)
        ll.push(2)
        ll.push(3)

        b = pair_first(ll.get(0))
        assert b == 3
        c = pair_first(ll.get(1))
        assert c == 2
        d = pair_first(ll.get(2))
        assert d == 1

    def test_iter_ll(self):

        ll = LinkedList()
        ll.push(1)
        ll.push(2)
        ll.push(3)

        a = [pair_first(x) for x in ll.iter_ll()]
        assert a == [3, 2, 1]

