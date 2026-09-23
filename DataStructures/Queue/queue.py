from DataStructures.List import single_linked_list as lt


def new_queue():
    cola = lt.new_list()
    return cola


def enqueue(cola, elem):
    lt.add_last(cola, elem)
    return cola


def dequeue(cola):
    elem = lt.remove_first(cola)
    return elem


def peek(cola):
    elem = lt.first_element(cola)
    return elem


def is_empty(cola):
    return lt.is_empty(cola)


def size(cola):
    return lt.size(cola)
