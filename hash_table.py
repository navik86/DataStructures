
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, person_obj):
        return isinstance(person_obj, Person) and self.name == person_obj.name

    def __repr__(self):
        return f"{self.name}"


hash_table = [[] for _ in range(10)]


# hash function
def hashing(keyvalue):
    return hash(keyvalue) % len(hash_table)


def insert(hash_table, keyvalue, value):
    hash_key = hashing(keyvalue)
    hash_table[hash_key].append(value)


def display_hash(hash_table):
    for i in range(len(hash_table)):
        print(i, end=" ")

        for j in hash_table[i]:
            print("-->", end=" ")
            print(j, end=" ")
        print()


if __name__ == '__main__':

    p1 = Person('Ivan')
    p2 = Person('Oleg')
    p3 = Person('Elena')

    insert(hash_table, p1, p1)
    insert(hash_table, p2, p2)
    insert(hash_table, p3, p3)

    display_hash(hash_table)