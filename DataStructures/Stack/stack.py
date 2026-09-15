from DataStructures.List import single_linked_list as lt


def new_stack():
    stack = lt.new_list()
    return stack


def push(my_stack, element):
    lt.add_last(my_stack, element)
    return my_stack


def pop(my_stack):
    element = lt.remove_last(my_stack)
    return element


def is_empty(my_stack):
    return lt.is_empty(my_stack)


def top(my_stack):
    element = lt.last_element(my_stack)
    return element


def size(my_stack):
    return lt.size(my_stack)
