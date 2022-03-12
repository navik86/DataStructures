class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def __repr__(self):
        return f"{self.val}"


def get_min(root):
    current = root
    while current.left:
        current = current.left
    return current.val


def get_max(root):
    current = root
    while current.right:
        current = current.right
    return current.val


def insert(root, val):
    # если дерево пустое вернем новый элемент
    if root.val is None:
        root.val = val
    else:
        # print('flag')
        # проверка на наличие такого элемента
        if val == root.val:
            return 'element exists'
        # поиск места для вставки
        if val < root.val:
            # если есть левый потомок
            if root.left:
                insert(root.left, val)
            # вставка если левого потомка нет
            else:
                root.left = Node(val)
        else:
            if root.right:
                insert(root.right, val)
            else:
                root.right = Node(val)


# Поиск в ширину
def breadth_first_search(root):

    current_node = root
    bfs_list = []
    queue = []
    queue.insert(0, current_node)

    while len(queue) > 0:
        current_node = queue.pop()
        bfs_list.append(current_node.val)

        if current_node.left:
            queue.insert(0, current_node.left)

        if current_node.right:
            queue.insert(0, current_node.right)

    return bfs_list


# Обход: левое поддерево, корень, правое поддерево
def traverse_inorder(root, lst):

    if root.left:
        traverse_inorder(root.left, lst)

    lst.append(root.val)

    if root.right:
        traverse_inorder(root.right, lst)

    return lst


# Обход: корень, левое поддерево, правое поддерево
def traverse_preorder(root, lst):

    lst.append(root.val)

    if root.left:
        traverse_preorder(root.left, lst)

    if root.right:
        traverse_preorder(root.right, lst)

    return lst


# Обход: корень, левое поддерево, правое поддерево
def traverse_postorder(root, lst):

    if root.left:
        traverse_postorder(root.left, lst)

    if root.right:
        traverse_postorder(root.right, lst)

    lst.append(root.val)

    return lst


# Находим узел и родителя (используем в удалении)
def find_node_and_parent(root, val, parent=None):

    if val == root.val:
        return root, parent

    if val < root.val:
        if root.left:
            return find_node_and_parent(root.left, val, root)
        else:
            return 'Not found'
    else:
        if root.right:
            return find_node_and_parent(root.right, val, root)
        else:
            return 'Not found'


# При удалении меняем часть дерева
def delete(root, val):

    # Проверяем наличие узла
    if find_node_and_parent(root, val) == 'Not found':
        return 'Node is not in tree'

    # получаем удаляемый узел и его родителя
    deleting_node, parent_node = find_node_and_parent(root, val)

    # проверяем сколько потомков содержит удаляемый узел
    nodes_effected = traverse_preorder(deleting_node, [])

    # если удаляемый узел не имеет потомков
    if len(nodes_effected) == 1:
        if parent_node.left.val == deleting_node.val:
            parent_node.left = None
        else:
            parent_node.right = None
        return 'Succesfully deleted'

    # если удаляемый содержит потомки, поэтому перестраиваем дерево из узла удаления
    else:
        # если удаляемый узел не имеет родителей
        if parent_node is None:
            nodes_effected.remove(deleting_node.val)
            # реализуем новое дерево без удаленного элемента
            root.left = None
            root.right = None
            root.val = None
            # создаем новое дерево
            for node in nodes_effected:
                insert(root, node)
            return 'Succesfully deleted'

        # если удаляемый элемент имеет родителя, делаем обход от родителя
        nodes_effected = traverse_preorder(parent_node, [])

        if parent_node.left == deleting_node:
            parent_node.left = None
        else:
            parent_node.right = None
        # Удаляем родителя, потомка и вставляем новую ветку в дерево
        nodes_effected.remove(deleting_node.val)
        nodes_effected.remove(parent_node.val)
        for node in nodes_effected:
            insert(root, node)

    return 'Successfully deleted'
