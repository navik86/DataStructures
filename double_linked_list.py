class Node:

    # инициализируем у экземпляра атрибуты
    def __init__(self, data):
        self.data = data  # значение узла
        self.next = None  # ссылка на след. узел
        self.prev = None  # ссылка на пред. узел


class DoubleLinkedList:

    # инициализируем пустой двухсвязанный список
    def __init__(self):
        self.head = None

    # метод добавляет элемент в начало списка
    def push(self, new_data):
        # создаем новый элемент списка, указываем знач.
        new_node = Node(new_data)

        # ссылку даем на существующий объект head
        new_node.next = self.head

        # если head не None:
        if self.head:
            self.head.prev = new_node

        # головой становится недавносозданный объект
        self.head = new_node





    # вывод всех элементов связанного списка (перебор)
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next




if __name__=='__main__':

    my_list = DoubleLinkedList()

    print('Создадим двухсвязанный список:')
    for i in range(6):
        my_list.push(i)

    my_list.printList()