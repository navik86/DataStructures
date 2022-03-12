class Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __repr__(self):
        return f"{self.val}"


class HashTable:

    def __init__(self, length=7):

        self.table = [None] * length
        self.counter = 0
        self.load_factor = 0.5

    def _hash_function(self, key):
        return key % len(self.table)

    def __len__(self):
        return self.counter

    def __getitem__(self, key):
        hashed_key = self._hash_function(key)
        if self.table[hashed_key] is None:
            return print("Invalid position!")
        else:
            for item in self.table[hashed_key]:
                if item.key == key:
                    return item.val
            return print("Invalid position!")

    def __setitem__(self, key, val):

        hashed_key = self._hash_function(key)

        # если под этим индексом еще нет бакета
        if self.table[hashed_key] is None:
            self.table[hashed_key] = []

        # eсли в бакете есть объект с таким key обновляем значение
        for item in self.table[hashed_key]:
            if item.key == key:
                item.val = val
                return

        # добавим новый элемент в бакет
        self.table[hashed_key].append(Item(key, val))
        self.counter += 1

        # если кол-во элементов превысило больше половины сущ. длины
        # запускаем процедуру увеличения хранилища

        if self.counter / len(self.table) > self.load_factor:
            self.resize(2*len(self.table))

    def __delitem__(self, key):
        hashed_key = self._hash_function(key)
        if self.table[hashed_key] is None:
            return print("Invalid position!")
        else:
            for item in self.table[hashed_key]:
                if item.key == key:
                    self.table[hashed_key] = None
                    return
            return print("Invalid position!")

    # увеличение hashtable
    def resize(self, length):
        temp = []

        # собираем все объекты во временный список
        for bucket in self.table:
            if bucket is not None:
                for items in bucket:
                    temp.append(items)

        # обнуляем атрибут table нашей hashtable
        self.table = length * [None]
        self.counter = 0

        # перезаписываем объекты с новыми хэшами
        for items in temp:
            self[items.key] = items.val

    def display_hash(self):
        for i in range(len(self.table)):
            print(i, end=" ")
            if self.table[i]:
                for j in self.table[i]:
                    print("-->", end=" ")
                    print(j, end=" ")
            print()