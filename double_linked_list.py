class Node:

    # инициализируем у экземпляра атрибуты
    def __init__(self, data):
        self.data = data  # значение узла
        self.next = None  # ссылка на след. узел
        self.prev = None  # ссылка на пред. узел


class DoubleLinkedList:

    # инициализируем первый элемент связанного списка
    # т.е. список создается с head
    def __init__(self):
        self.head = None









if __name__=='__main__':

    my_list = DoubleLinkedList()