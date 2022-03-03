from unittest import TestCase
from queue import *


class QueueTestCase(TestCase):

    def test_enqueue(self):
        my_q = create_queue()

        enqueue(my_q, 1)
        assert list(my_q) == [1]
        enqueue(my_q, 2)
        assert list(my_q) == [2, 1]
        enqueue(my_q, 3)
        assert list(my_q) == [3, 2, 1]

    def test_dequeue(self):
        my_q = create_queue()
        enqueue(my_q, 1)
        enqueue(my_q, 2)
        enqueue(my_q, 3)

        dequeue(my_q)
        assert list(my_q) == [3, 2]
        dequeue(my_q)
        assert list(my_q) == [3]
        dequeue(my_q)
        assert list(my_q) == []

    def test_front(self):
        my_q = create_queue()
        enqueue(my_q, 1)
        enqueue(my_q, 2)
        enqueue(my_q, 3)

        assert pair_first(front(my_q)) == 3

    def test_rear(self):
        my_q = create_queue()
        enqueue(my_q, 1)
        enqueue(my_q, 2)
        enqueue(my_q, 3)

        assert pair_first(rear(my_q)) == 1
