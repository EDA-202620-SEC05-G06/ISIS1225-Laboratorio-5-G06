from DataStructures.List import single_linked_list as lt


def new_stack():
    pila = lt.new_list()
    return pila


def push(pila, elem):
    lt.add_last(pila, elem)
    return pila


def pop(pila):
    elem = lt.remove_last(pila)
    return elem


def is_empty(pila):
    return lt.is_empty(pila)


def top(pila):
    elem = lt.last_element(pila)
    return elem


def size(pila):
    return lt.size(pila)
