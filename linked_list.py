class Node:

    # инициализируем у экземпляра атрибуты
    def __init__(self, data):
        self.data = data  # значение узла
        self.next = None  # ссылка на след. узел


class LinkedList:
 
    # инициализируем пустой связанный список
    def __init__(self):
        self.head = None
 
 
    # метод добавляет элемент в начало списка
    def push(self, new_data):
 
        # создаем новый элемент списка, указываем знач.
        new_node = Node(new_data)
 
        # ссылку даем на существующий объект head
        new_node.next = self.head
 
        # головой становится недавносозданный объект
        self.head = new_node


    # удаляем элемент списка, используя данные как ключ
    def deleteNode(self, key):
         
        # присваиваем temp ссылку на объект head
        temp = self.head
 
        # если head содержит удаляемое значение
        if temp:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
 
        # Находим ключ который нужно удалить, отслеживая
        # предыдущий объект
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
 
        # если значения нет в нашем списке
        if temp == None:
            return
 
        # отключаем удаляемый объект
        prev.next = temp.next
 
        temp = None


    # удаляем последний объект
    def deleteLastNode(self):

        # если список пустой
        if self.head is None:
            return None
        # если список содержит только один элемент
        if self.head.next is None:
            self.head = None
            return None
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None


    # метод добавляет элемент в середину списка
    def insertMiddle(self, data):

        if self.head is None:  # если список пуст
            self.head = Node(data)
        else:
            # создаем новый элемент списка, указываем знач.
            new_node = Node(data)

            ptr = self.head
            length = 0

            # подсчитываем длину списка
            while ptr:
                ptr = ptr.next
                length += 1

            # считаем номер узла после которого нужно вставить
            if length % 2 == 0:
                count = length / 2
            else:
                (length + 1) / 2

            ptr = self.head

            # перемещаем позицию на нужный номер
            while count > 1:
                count -= 1
                ptr = ptr.next

            # вставляем новый элемент, переписываем ссылки
            new_node.next = ptr.next
            ptr.next = new_node
 
 
    # метод добавляет элемент в конец списка
    def append(self, new_data):
 
        # создаем новый элемент списка, указываем знач.
        new_node = Node(new_data)
 
        # если список пуст, делаем новый элемент головным
        if self.head is None:
            self.head = new_node
            return
 
        # проходим до последнего узла
        # последний_узел.next == None
        last = self.head
        while last.next:
            last = last.next
 
        # последний модуль ссылается на недавносозданный
        last.next = new_node
 

    # кол-во элементов в списке
    def len(self):
        counter = 0
        my_node = self.head
        while my_node:
            counter += 1
            my_node = my_node.next
        print(counter)


    # сортировка элементов по значению по возрастанию
    # сортировка выполена пузырьком
    def my_sort(self):
        current = self.head
        index = None

        if self.head is None:   # если список пуст
            return
        else:
            while current:
                # index привязываем к объекту, след. за головой
                index = current.next
                while index:
                    # если 1-го больше 2-го, меняем местами
                    if current.data > index.data:
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    # если все ок, переходи к следующей паре
                    index = index.next
                current = current.next


    # вывод всех элементов связанного списка (перебор)
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next   
 



if __name__=='__main__':

    my_list = LinkedList()

    print('Создадим связанный список:')
    for i in range(6):
        my_list.push(i)

    my_list.printList()

    print('\nДобавим 5 в начало списка:')
    my_list.push(5)
    my_list.printList()

    print('\nДобавим 6 в конец списка:')
    my_list.append(6)
    my_list.printList()

    print('\nДобавим 7 в середину списка:')
    my_list.insertMiddle(7)
    my_list.printList()

    print('\nУдалим элемент со значением 0:')
    my_list.deleteNode(0)
    my_list.printList()

    print('\nУдаляем последний объект:')
    my_list.deleteLastNode()
    my_list.printList()

    print('\nКол-во элементов в связанном списке:')
    my_list.len()

    print('Отсортируем по возрастанию наш список:')
    my_list.my_sort()
    my_list.printList()


