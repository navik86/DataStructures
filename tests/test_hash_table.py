from unittest import TestCase
from hash_table import *


class HashTableTestCase(TestCase):

    def test_setitem(self):

        my_hash_table = HashTable()
        my_hash_table[22] = "Ivan"
        my_hash_table[222] = "Oleg"
        my_hash_table[17] = "Elena"

        assert my_hash_table[22] == "Ivan"
        assert my_hash_table[222] == "Oleg"
        assert my_hash_table[17] == "Elena"

    def test_len(self):

        my_hash_table = HashTable()
        my_hash_table[22] = "Ivan"
        my_hash_table[222] = "Oleg"
        my_hash_table[17] = "Elena"

        assert len(my_hash_table) == 3

    def test_resize(self):

        my_hash_table = HashTable()
        my_hash_table[22] = "Ivan"
        my_hash_table[222] = "Oleg"
        my_hash_table[17] = "Elena"

        assert len(my_hash_table.table) == 7

        my_hash_table[113] = "Natasha"

        assert len(my_hash_table.table) == 14

    def test_del(self):

        my_hash_table = HashTable()
        my_hash_table[22] = "Ivan"
        my_hash_table[222] = "Oleg"
        my_hash_table[17] = "Elena"

        del my_hash_table[222]

        assert my_hash_table[222] == None