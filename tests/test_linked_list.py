from unittest import TestCase
from linked_list import *


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
        ll.push(4)

        ll.remove()
        assert list(ll) == [2, 1]

        ll.remove()
        assert list(ll) == [1]

        ll.remove()
        assert list(ll) == []



