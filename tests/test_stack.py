from unittest import TestCase
from stack import *
from double_pair import *


class StackTestCase(TestCase):

    def test_push(self):
        st = MyStack()
        st.push(1)
        assert list(st) == [1]
        st.push(2)
        assert list(st) == [2, 1]
        st.push(3)
        assert list(st) == [3, 2, 1]

    def test_pop(self):
        st = MyStack()
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
        st1 = MyStack()
        st1.push(1)
        st2 = MyStack()
        assert list(st1) == [1]
        assert list(st2) == []

    def test_size(self):
        st = MyStack()
        st.push(1)
        st.push(2)
        assert len(list(st)) == 2

    def test_top(self):
        st = MyStack()
        st.push(1)
        st.push(2)
        assert list(st)[0] == 2