from unittest import TestCase
from stack import *
from double_pair import *


class StackTestCase(TestCase):

    def test_push(self):
        st = Stack()
        st.push(1)
        assert list(st) == [1]
        st.push(2)
        assert list(st) == [2, 1]
        st.push(3)
        assert list(st) == [3, 2, 1]

    def test_pop(self):
        st = Stack()
        st.push(1)
        st.push(2)
        st.push(3)

        st.pop()
        assert list(st) == [2, 1]
        st.pop()
        assert list(st) == [1]
        st.pop()
        assert list(st) == []

    def test_empty(self):
        st1 = Stack()
        st1.push(1)
        st2 = Stack()
        assert list(st1) == [1]
        assert list(st2) == []

    def test_iter_st(self):
        st = Stack()
        st.push(1)
        st.push(2)
        st.push(3)

        a = [pair_first(x) for x in st.iter_st()]
        assert a == [3, 2, 1]