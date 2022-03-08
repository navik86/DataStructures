from unittest import TestCase
from binary_search_tree import *


class StackTestCase(TestCase):

    def test_insert_tree(self):

        root = None
        root = insert(root, 5)
        assert root.key == 5
        root = insert(root, 3)
        assert root.left.key == 3
        root = insert(root, 2)
        assert root.left.left.key == 2
        root = insert(root, 4)
        assert root.left.right.key == 4
        root = insert(root, 7)
        assert root.right.key == 7
        root = insert(root, 6)
        assert root.right.left.key == 6
        root = insert(root, 8)
        assert root.right.right.key == 8

    def test_search(self):

        root = None
        root = insert(root, 5)
        root = insert(root, 3)
        root = insert(root, 2)
        root = insert(root, 4)
        root = insert(root, 7)
        root = insert(root, 6)
        root = insert(root, 8)

        my_node = search(root, 6)
        assert my_node.key == 6

        my_node2 = search(root, 2)
        assert my_node2.key == 2

        my_node3 = search(root, 8)
        assert my_node3.key == 8

    def test_deleteNode(self):

        root = None
        root = insert(root, 5)
        root = insert(root, 3)
        root = insert(root, 2)
        root = insert(root, 4)
        root = insert(root, 7)
        root = insert(root, 6)
        root = insert(root, 8)

        deleteNode(root, 6)
        assert search(root, 6) == None

        deleteNode(root, 5)
        assert search(root, 5) == None