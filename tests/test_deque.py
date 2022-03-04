from unittest import TestCase
from deque import *


class DequeTestCase(TestCase):

    def test_insertFront(self):
        d = MyDeque()
        d.insertFront(1)
        assert list(d) == [1]
        d.insertFront(2)
        assert list(d) == [2, 1]
        d.insertFront(3)
        assert list(d) == [3, 2, 1]

    def test_insertRear(self):
        d = MyDeque()
        d.insertRear(1)
        assert list(d) == [1]
        d.insertRear(2)
        assert list(d) == [1, 2]
        d.insertRear(3)
        assert list(d) == [1, 2, 3]

    def test_deleteFront(self):
        d = MyDeque()
        d.insertFront(1)
        d.insertFront(2)
        d.insertFront(3)

        d.deleteFront()
        assert list(d) == [2, 1]
        d.deleteFront()
        assert list(d) == [1]
        d.deleteFront()
        assert list(d) == []


    def test_deleteRear(self):
        d = MyDeque()
        d.insertFront(1)
        d.insertFront(2)
        d.insertFront(3)

        d.deleteRear()
        assert list(d) == [3, 2]
        d.deleteRear()
        assert list(d) == [3]
        d.deleteRear()
        assert list(d) == []


    def test_getFront(self):
        d = MyDeque()
        d.insertFront(1)
        d.insertFront(2)
        d.insertFront(3)
        assert get_data(d.getFront()) == 3

    def test_getRear(self):
        d = MyDeque()
        d.insertFront(1)
        d.insertFront(2)
        d.insertFront(3)
        assert get_data(d.getRear()) == 1

    def test_size(self):
        d = MyDeque()
        d.insertFront(1)
        d.insertFront(2)
        d.insertFront(3)
        assert len(list(d)) == 3