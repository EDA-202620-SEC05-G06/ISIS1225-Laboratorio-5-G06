from DataStructures.List import single_linked_list as lt


def new_queue():
    queue = lt.new_list()
    return queue


def enqueue(my_queue, element):
    lt.add_last(my_queue, element)
    return my_queue


def dequeue(my_queue):
    element = lt.remove_first(my_queue)
    return element


def peek(my_queue):
    element = lt.first_element(my_queue)
    return element


def is_empty(my_queue):
    return lt.is_empty(my_queue)


def size(my_queue):
    return lt.size(my_queue)
