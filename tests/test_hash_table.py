from unittest import TestCase
from hash_table import *


class HashTableTestCase(TestCase):

    def test_insert(self):

        def check_exist(my_object):
            for i in range(len(hash_table)):
                for j in hash_table[i]:
                    if j == my_object:
                        return my_object

        p1 = Person('Ivan')
        p2 = Person('Oleg')
        p3 = Person('Elena')

        insert(hash_table, p1, p1)
        insert(hash_table, p2, p2)
        insert(hash_table, p3, p3)

        assert check_exist(p1) == p1
        assert check_exist(p2) == p2
        assert check_exist(p3) == p3