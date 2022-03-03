from linked_list import *


def create_queue():
    return LinkedList()


def enqueue(queue, item):
    queue.push(item)


def dequeue(queue):
    queue.pop()


def front(queue):
    return queue.head


def rear(queue):
    return queue.last

