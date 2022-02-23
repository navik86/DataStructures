from linked_list import *


class DoubleNode:

    # инициализируем у экземпляра атрибуты
    def __init__(self, data):
        self.data = data  # значение узла
        self.next = None  # ссылка на след. узел
        self.prev = None  # ссылка на пред. узел


class DoubleLinkedList(LinkedList):

    # Инициализируем пустой список
    def __init__(self):
        self.head = None
        self.tail = None

    # метод добавляет элемент в начало списка
    def push(self, data):
        new_node = Node(data);

        # если список пустой
        if self.head is None:
            # голова и хвост указывают на new_node
            self.head = self.tail = new_node
            # ссылка на предыдущий None
            self.head.prev = None
            # ссылка на следующий None
            self.tail.next = None
        # если список уже имеет элемент или элементы
        else:
            # меняем prev ссылку с None на новый объект
            self.head.prev = new_node
            # меняем next ссылку нового объекта
            new_node.next = self.head
            # меняем prev ссылку нового объекта
            new_node.prev = None
            # новый объект становится на место головы
            self.head = new_node


    # метод добавляет элемент в конец списка
    def append(self, new_data):

        # создаем новый элемент списка, указываем знач.
        # его нужно расположить за последним элементом списка
        new_node = DoubleNode(new_data)

        # если список пустой делаем новый объект головой см. выше
        if self.head is None:
            self.head = self.tail = new_node
            self.head.prev = None
            self.tail.next = None
        # если список уже имеет элемент или элементы
        else:
            # меняем next ссылку хвоста на новый объект
            self.tail.next = new_node
            # меняем prev ссылку нового объекта на хвост
            new_node.prev = self.tail
            # Делаем новый объект хвостом
            self.tail = new_node
            # Меняем next ссылку хвоста на None
            self.tail.next = None


    # удаляем элемент внутри списка, используя данные как ключ
    def delete(self, value):

        temp = self.head
        temp2 = self.tail

        # если голова содержит удаляемое значение
        if temp.data == value:
            self.head = temp.next
            temp = None
            return
        # если хвост содержит удаляемое значение
        elif temp2.data == value:
            self.tail = temp2.prev
            self.tail.next = None
            return
        # если значение содержится внутри списка
        elif while temp:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next

        # Если список пуст
        if temp is None:
            return print('Список пуст')

        # отключаем удаляемый объект
        prev.next = temp.next


a = {1: 2}
a[]


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
