from unittest import TestCase
from binary_search_tree import *


class StackTestCase(TestCase):

    def test_insert_tree(self):

        root = Node(10)
        assert root.val == 10
        insert(root, 5)
        assert root.left.val == 5
        insert(root, 6)
        assert root.left.right.val == 6
        insert(root, 12)
        assert root.right.val == 12
        insert(root, 11)
        assert root.right.left.val == 11
        insert(root, 14)
        assert root.right.right.val == 14

    def test_find_node_and_parent(self):

        root = Node(10)
        insert(root, 5)
        insert(root, 6)
        insert(root, 12)
        insert(root, 11)
        insert(root, 14)

        finded_root, parent = find_node_and_parent(root, 12)
        assert finded_root.val == 12
        assert parent.val == 10

    def test_get_min(self):

        root = Node(10)
        insert(root, 5)
        insert(root, 6)
        insert(root, 12)
        insert(root, 11)
        insert(root, 14)

        assert get_min(root) == 5

    def test_get_max(self):

        root = Node(10)
        insert(root, 5)
        insert(root, 6)
        insert(root, 12)
        insert(root, 11)
        insert(root, 14)

        assert get_max(root) == 14

    def test_delete(self):

        root = Node(10)
        insert(root, 5)
        insert(root, 6)
        insert(root, 12)
        insert(root, 11)
        insert(root, 14)

        delete(root, 12)

        assert find_node_and_parent(root, 12) == 'Not found'

        assert root.val > root.left.val
        assert root.val < root.right.val
        assert root.left.val < root.left.right.val
        assert root.right.val < root.right.right.val