
# insert, delete, search
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def __repr__(self):
        return f"{self.key}"


# Вставки нового узла с заданным ключом
def insert(node, key):
    # Если дерево пустое вернем новый элемент
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node


# Функция удаляет ключ и возвращает новый корень
def deleteNode(root, key):

    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)
        return root
    elif key > root.key:
        root.right = deleteNode(root.right, key)
        return root

    # Достигли удаляемого узла

    # Если элемент это лист
    if root.left is None and root.right is None:
        return None

    # Если есть один потомок
    if root.left is None:
        temp = root.right
        root = None
        return temp
    elif root.right is None:
        temp = root.left
        root = None
        return temp

    # Если оба потомка
    succParent = root

    # Поиск приемника
    succ = root.right

    while succ.left:
        succParent = succ
        succ = succ.left

    if succParent != root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right

    # Копируем данные приемника
    root.key = succ.key
    return root


def search(root, key):

    if root is None or root.key == key:
        return root

    if root.key < key:
        return search(root.right, key)

    return search(root.left, key)


def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.key, end=" ")
        print_tree(root.right)


