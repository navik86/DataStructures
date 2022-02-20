class Node:

    # инициализируем у экземпляра атрибуты
    def __init__(self, data):
        self.data = data  # значение узла
        self.next = None  # ссылка на след. узел


class LinkedList:
 
    # инициализируем первый элемент связанного списка
    # т.е. список создается с head, кот. не несет значение
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
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
 
        # Находим ключ который нужно удалить, отслеживая
        # предыдущий объект
        while temp is not None:
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

            if self.head is None:
                return None
            if self.head.next is None:
                self.head = None
                return None
            second_last = self.head
            while second_last.next.next:
                second_last = second_last.next
            second_last.next = None


    # метод добавляет элемент в середину списка
    def insertMiddle(self, data):

        if self.head is None:  # if the list is empty
            self.head = Node(data)
        else:

            # create a new node for the value
            # to be inserted
            new_node = Node(data)

            ptr = self.head
            length = 0

            # calculate the length of the linked
            # list
            while ptr is not None:
                ptr = ptr.next
                length += 1

            # 'count' the number of node after which
            # the new node has to be inserted
            if length % 2 == 0:
                count = length / 2
            else:
                (length + 1) / 2

            ptr = self.head

            # move ptr to the node after which
            # the new node has to inserted
            while count > 1:
                count -= 1
                ptr = ptr.next

            # insert the 'newNode' and adjust
            # links accordingly
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
        last.next =  new_node
 

    # кол-во элементов в списке
    def len(self):
        counter = 0
        my_node = self.head
        while my_node:
            counter += 1
            my_node = my_node.next
        print(counter)


    # сортировка элементов по значению по возрастанию
    def my_sort(self):
        current = self.head
        index = None

        if self.head is None:
            return
        else:
            while current is not None:
                index = current.next
                while index is not None:
                    if current.data > index.data:
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next


    # вывод всех элементов связанного списка
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


