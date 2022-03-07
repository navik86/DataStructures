
# insert, delete, search
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


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

    elif (key > root.key):
        root.right = deleteNode(root.right, key)
        return root

    if root.left is None and root.right is None:
        return None

    if root.left is None:
        temp = root.right
        root = None
        return temp

    elif root.right is None:
        temp = root.left
        root = None
        return temp

    succParent = root

    succ = root.right

    while succ.left:
        succParent = succ
        succ = succ.left

    if succParent != root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right

    root.key = succ.key

    return root


def search(root, key):

    if root is None or root.val == key:
        return root

    if root.val < key:
        return search(root.right, key)

    return search(root.left, key)


def print_tree(root):
    if root is not None:
        print_tree(root.left)
        print(root.key, end=" ")
        print_tree(root.right)


if __name__ == '__main__':


    root = None
    root = insert(root, 50)
    # root = insert(root, 30)
    # root = insert(root, 20)
    # root = insert(root, 40)
    # root = insert(root, 70)
    # root = insert(root, 60)
    # root = insert(root, 80)

    # print_tree(root)

