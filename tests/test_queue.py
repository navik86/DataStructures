from unittest import TestCase
from queue import *


class QueueTestCase(TestCase):

    def test_enqueue(self):
        my_q = MyQueue()

        my_q.enqueue(1)
        assert list(my_q) == [1]
        my_q.enqueue(2)
        assert list(my_q) == [2, 1]
        my_q.enqueue(3)
        assert list(my_q) == [3, 2, 1]

    def test_dequeue(self):
        my_q = MyQueue()
        my_q.enqueue(1)
        my_q.enqueue(2)
        my_q.enqueue(3)

        my_q.dequeue()
        assert list(my_q) == [3, 2]
        my_q.dequeue()
        assert list(my_q) == [3]
        my_q.dequeue()
        assert list(my_q) == []

    def test_front(self):
        my_q = MyQueue()
        my_q.enqueue(1)
        my_q.enqueue(2)
        my_q.enqueue(3)

        assert pair_first(my_q.front()) == 3

