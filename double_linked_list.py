from linked_list import *


class DoubleNode:

    # инициализируем у экземпляра атрибуты
    def __init__(self, data):
        self.data = data  # значение узла
        self.next = None  # ссылка на след. узел
        self.prev = None  # ссылка на пред. узел


class DoubleLinkedList(LinkedList):

    # наследуем метод из LinkedList
    # инициализируем пустой двухсвязанный список
    # def __init__(self):
    #     self.head = None

    # метод добавляет элемент в начало списка
    def push(self, new_data):
        # создаем новый элемент списка, указываем знач.
        new_node = DoubleNode(new_data)

        # ссылку даем на существующий объект head
        new_node.next = self.head

        # если список не пустой:
        if self.head:
            self.head.prev = new_node

        # головой становится недавносозданный объект
        self.head = new_node


    # метод добавляет элемент в конец списка
    def append(self, new_data):

        # создаем новый элемент списка, указываем знач.
        # его нужно расположить за последним элементом списка
        new_node = DoubleNode(new_data)

        # если список пустой делаем новый объект головой
        if self.head is None:
            self.head = new_node
            return

        # делаем проход до последнего узла
        last = self.head
        while last.next:
            last = last.next

        # меняем ссылки next prev
        last.next = new_node
        new_node.prev = last


    # удаляем элемент списка, используя данные как ключ для поиска
    def delete(self, key):
        pass


    # наследуем метод из LinkedList
    # вывод всех элементов связанного списка (перебор)
    # def printList(self):
    #     temp = self.head
    #     while temp:
    #         print(temp.data, end=' ')
    #         temp = temp.next




if __name__=='__main__':

    d_list = DoubleLinkedList()

    print('Создадим двухсвязанный список:')
    for i in range(6):
        d_list.push(i)
    d_list.printList()

    print('\nДобавим 5 в начало списка:')
    d_list.push(5)
    d_list.printList()

    print('\nДобавим 6 в конец списка:')
    d_list.append(6)
    d_list.printList()

    print('\nУдалим элемент со значением 0:')
    d_list.delete(0)
    d_list.printList()
