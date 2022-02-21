from linked_list import *


class DoubleNode:

    # инициализируем у экземпляра атрибуты
    def __init__(self, data):
        self.data = data  # значение узла
        self.next = None  # ссылка на след. узел
        self.prev = None  # ссылка на пред. узел


class DoubleLinkedList(LinkedList):


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




if __name__=='__main__':

    d_list = DoubleLinkedList()

    print('Создадим двухсвязанный список:')
    for i in range(5, 12):
        d_list.push(i)
    d_list.printList()

    print('\nДобавим 5 в начало списка:')
    d_list.push(5)
    d_list.printList()

    print('\nДобавим 6 в конец списка:')
    d_list.append(6)
    d_list.printList()

    print('\nУдалим элемент со значением 5:')
    d_list.delete(5)
    d_list.printList()

    print('\nУдаляем последний объект:')
    d_list.deleteLastNode()
    d_list.printList()

    print('\nКол-во элементов в связанном списке:')
    d_list.len()

    print('Отсортируем по возрастанию наш список:')
    d_list.my_sort()
    d_list.printList()

    print('\nЕсть ли элемент со значением 22 в списке :')
    d_list.search_item(22)
