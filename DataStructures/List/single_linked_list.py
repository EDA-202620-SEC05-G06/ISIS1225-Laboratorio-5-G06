"""
  Implementación del TAD Lista usando una estructura de nodos encadenados
  simples (SingleLinkedList).

  La lista se representa como un diccionario con las llaves:
    - 'first': referencia al primer nodo de la lista.
    - 'last': referencia al último nodo de la lista.
    - 'size': número de elementos almacenados en la lista.

  Cada nodo es un diccionario con las llaves 'info' y 'next'.
"""

from DataStructures.List import list_node as nodo


def new_list():
    """ Crea una lista encadenada vacía.

        :returns: Un diccionario que representa la lista vacía.
        :rtype: dict
    """
    nueva_lista = {
        'first': None,
        'last': None,
        'size': 0,
    }
    return nueva_lista


def add_first(mi_lista, elemento):
    """ Agrega un elemento al inicio de la lista.

        :param mi_lista: La lista a modificar.
        :type mi_lista: dict
        :param elemento: El elemento a agregar.
        :type elemento: any

        :returns: La lista con el nuevo elemento al inicio.
        :rtype: dict
    """
    nodo_nuevo = nodo.new_single_node(elemento)
    nodo_nuevo['next'] = mi_lista['first']
    mi_lista['first'] = nodo_nuevo
    if mi_lista['size'] == 0:
        mi_lista['last'] = nodo_nuevo
    mi_lista['size'] += 1
    return mi_lista


def add_last(mi_lista, elemento):
    """ Agrega un elemento al final de la lista.

        :param mi_lista: La lista a modificar.
        :type mi_lista: dict
        :param elemento: El elemento a agregar.
        :type elemento: any

        :returns: La lista con el nuevo elemento al final.
        :rtype: dict
    """
    nodo_nuevo = nodo.new_single_node(elemento)
    if mi_lista['size'] == 0:
        mi_lista['first'] = nodo_nuevo
    else:
        mi_lista['last']['next'] = nodo_nuevo
    mi_lista['last'] = nodo_nuevo
    mi_lista['size'] += 1
    return mi_lista


def is_empty(mi_lista):
    """ Indica si la lista está vacía.

        :param mi_lista: La lista a examinar.
        :type mi_lista: dict

        :returns: True si la lista está vacía, False en caso contrario.
        :rtype: bool
    """
    return mi_lista['size'] == 0


def size(mi_lista):
    """ Retorna el número de elementos de la lista.

        :param mi_lista: La lista a examinar.
        :type mi_lista: dict

        :returns: El número de elementos de la lista.
        :rtype: int
    """
    return mi_lista['size']


def first_element(mi_lista):
    """ Retorna la información del primer elemento de la lista.

        :param mi_lista: La lista a examinar.
        :type mi_lista: dict

        :returns: La información del primer elemento de la lista.
        :rtype: any
    """
    if mi_lista['first'] is None:
        return None
    return mi_lista['first']['info']


def last_element(mi_lista):
    """ Retorna la información del último elemento de la lista.

        :param mi_lista: La lista a examinar.
        :type mi_lista: dict

        :returns: La información del último elemento de la lista.
        :rtype: any
    """
    if mi_lista['last'] is None:
        return None
    return mi_lista['last']['info']


def get_element(mi_lista, posicion):
    """ Retorna la información del elemento en la posición dada (0-indexado).

        :param mi_lista: La lista a examinar.
        :type mi_lista: dict
        :param posicion: La posición del elemento a retornar.
        :type posicion: int

        :returns: La información del elemento en la posición indicada.
        :rtype: any
    """
    nodo_actual = mi_lista['first']
    posicion_actual = 0
    while posicion_actual < posicion and nodo_actual is not None:
        nodo_actual = nodo_actual['next']
        posicion_actual += 1
    if nodo_actual is None:
        return None
    return nodo_actual['info']


def remove_first(mi_lista):
    """ Elimina el primer elemento de la lista y retorna su información.

        :param mi_lista: La lista a modificar.
        :type mi_lista: dict

        :returns: La información del elemento eliminado.
        :rtype: any
    """
    if mi_lista['first'] is None:
        return None
    nodo_eliminado = mi_lista['first']
    mi_lista['first'] = nodo_eliminado['next']
    mi_lista['size'] -= 1
    if mi_lista['size'] == 0:
        mi_lista['last'] = None
    return nodo_eliminado['info']


def remove_last(mi_lista):
    """ Elimina el último elemento de la lista y retorna su información.

        :param mi_lista: La lista a modificar.
        :type mi_lista: dict

        :returns: La información del elemento eliminado.
        :rtype: any
    """
    if mi_lista['first'] is None:
        return None
    if mi_lista['size'] == 1:
        nodo_eliminado = mi_lista['first']
        mi_lista['first'] = None
        mi_lista['last'] = None
    else:
        nodo_previo = mi_lista['first']
        while nodo_previo['next'] is not mi_lista['last']:
            nodo_previo = nodo_previo['next']
        nodo_eliminado = mi_lista['last']
        nodo_previo['next'] = None
        mi_lista['last'] = nodo_previo
    mi_lista['size'] -= 1
    return nodo_eliminado['info']


def insert_element(mi_lista, elemento, posicion):
    """ Inserta un elemento en la posición dada de la lista.

        :param mi_lista: La lista a modificar.
        :type mi_lista: dict
        :param elemento: El elemento a insertar.
        :type elemento: any
        :param posicion: La posición en la que se inserta el elemento.
        :type posicion: int

        :returns: La lista con el elemento insertado.
        :rtype: dict
    """
    nodo_nuevo = nodo.new_single_node(elemento)
    if posicion == 0:
        nodo_nuevo['next'] = mi_lista['first']
        mi_lista['first'] = nodo_nuevo
        if mi_lista['size'] == 0:
            mi_lista['last'] = nodo_nuevo
    elif posicion >= mi_lista['size']:
        mi_lista['last']['next'] = nodo_nuevo
        mi_lista['last'] = nodo_nuevo
    else:
        nodo_previo = mi_lista['first']
        for _ in range(posicion - 1):
            nodo_previo = nodo_previo['next']
        nodo_nuevo['next'] = nodo_previo['next']
        nodo_previo['next'] = nodo_nuevo
    mi_lista['size'] += 1
    return mi_lista


def is_present(mi_lista, elemento, funcion_comparacion):
    """ Informa si un elemento está presente en la lista.

        :param mi_lista: La lista a examinar.
        :type mi_lista: dict
        :param elemento: El elemento a buscar.
        :type elemento: any
        :param funcion_comparacion: Función de comparación. Retorna 0 si los
            elementos son iguales.
        :type funcion_comparacion: function

        :returns: La posición del elemento si se encuentra, -1 en caso
            contrario.
        :rtype: int
    """
    posicion = -1
    nodo_actual = mi_lista['first']
    posicion_actual = 0
    while nodo_actual is not None and posicion == -1:
        if funcion_comparacion(elemento, nodo_actual['info']) == 0:
            posicion = posicion_actual
        nodo_actual = nodo_actual['next']
        posicion_actual += 1
    return posicion


def delete_element(mi_lista, posicion):
    """ Elimina el elemento en la posición dada de la lista.

        :param mi_lista: La lista a modificar.
        :type mi_lista: dict
        :param posicion: La posición del elemento a eliminar.
        :type posicion: int

        :returns: La lista sin el elemento eliminado.
        :rtype: dict
    """
    if mi_lista['first'] is None or posicion < 0 or posicion >= mi_lista['size']:
        return mi_lista
    nodo_previo = None
    nodo_actual = mi_lista['first']
    for _ in range(posicion):
        nodo_previo = nodo_actual
        nodo_actual = nodo_actual['next']
    if nodo_previo is None:
        mi_lista['first'] = nodo_actual['next']
    else:
        nodo_previo['next'] = nodo_actual['next']
    if nodo_actual is mi_lista['last']:
        mi_lista['last'] = nodo_previo
    mi_lista['size'] -= 1
    if mi_lista['size'] == 0:
        mi_lista['first'] = None
        mi_lista['last'] = None
    return mi_lista


def change_info(mi_lista, posicion, nueva_info):
    """ Cambia la información del elemento en la posición dada.

        :param mi_lista: La lista a modificar.
        :type mi_lista: dict
        :param posicion: La posición del elemento a modificar.
        :type posicion: int
        :param nueva_info: La nueva información del elemento.
        :type nueva_info: any

        :returns: La lista con la información modificada.
        :rtype: dict
    """
    nodo_actual = mi_lista['first']
    for _ in range(posicion):
        nodo_actual = nodo_actual['next']
    nodo_actual['info'] = nueva_info
    return mi_lista


def exchange(mi_lista, posicion_1, posicion_2):
    """ Intercambia la información de las posiciones posicion_1 y posicion_2.

        :param mi_lista: La lista a modificar.
        :type mi_lista: dict
        :param posicion_1: La posición del primer elemento.
        :type posicion_1: int
        :param posicion_2: La posición del segundo elemento.
        :type posicion_2: int

        :returns: La lista con los elementos intercambiados.
        :rtype: dict
    """
    info_posicion_1 = get_element(mi_lista, posicion_1)
    info_posicion_2 = get_element(mi_lista, posicion_2)
    change_info(mi_lista, posicion_1, info_posicion_2)
    change_info(mi_lista, posicion_2, info_posicion_1)
    return mi_lista


def sub_list(mi_lista, posicion, num_elementos):
    """ Retorna una nueva lista con num_elementos elementos desde posicion.

        :param mi_lista: La lista original.
        :type mi_lista: dict
        :param posicion: La posición inicial de la sublista.
        :type posicion: int
        :param num_elementos: El número de elementos de la sublista.
        :type num_elementos: int

        :returns: Una nueva lista con la sublista solicitada.
        :rtype: dict
    """
    sublista = new_list()
    nodo_actual = mi_lista['first']
    posicion_actual = 0
    while posicion_actual < posicion and nodo_actual is not None:
        nodo_actual = nodo_actual['next']
        posicion_actual += 1
    contador = 0
    while nodo_actual is not None and contador < num_elementos:
        add_last(sublista, nodo_actual['info'])
        nodo_actual = nodo_actual['next']
        contador += 1
    return sublista


# -----------------------------------------------------------------------------
#  Algoritmos de ordenamiento
# -----------------------------------------------------------------------------


def default_sort_criteria(elemento_1, elemento_2):
    """ Función de comparación por defecto para ordenar elementos.

        Compara dos elementos y retorna True si el primer elemento es menor
        que el segundo y False en caso contrario (orden ascendente).

        :param elemento_1: Primer elemento a comparar.
        :type elemento_1: any
        :param elemento_2: Segundo elemento a comparar.
        :type elemento_2: any

        :returns: True si elemento_1 es menor que elemento_2, False en caso
            contrario.
        :rtype: bool
    """
    esta_ordenado = False
    if elemento_1 < elemento_2:
        esta_ordenado = True
    return esta_ordenado


def selection_sort(mi_lista, funcion_criterio):
    """ Ordena la lista usando el algoritmo de selección (Selection Sort).

        :param mi_lista: La lista a ordenar.
        :type mi_lista: dict
        :param funcion_criterio: Función de comparación. Retorna True si
            el primer elemento debe ir antes que el segundo.
        :type funcion_criterio: function

        :returns: La lista ordenada.
        :rtype: dict
    """
    tam_lista = size(mi_lista)
    for indice in range(tam_lista - 1):
        posicion_minimo = indice
        siguiente = indice + 1
        while siguiente < tam_lista:
            if not funcion_criterio(get_element(mi_lista, posicion_minimo),
                                    get_element(mi_lista, siguiente)):
                posicion_minimo = siguiente
            siguiente += 1
        if posicion_minimo != indice:
            exchange(mi_lista, indice, posicion_minimo)
    return mi_lista


def insertion_sort(mi_lista, funcion_criterio):
    """ Ordena la lista usando el algoritmo de inserción (Insertion Sort).

        :param mi_lista: La lista a ordenar.
        :type mi_lista: dict
        :param funcion_criterio: Función de comparación. Retorna True si
            el primer elemento debe ir antes que el segundo.
        :type funcion_criterio: function

        :returns: La lista ordenada.
        :rtype: dict
    """
    tam_lista = size(mi_lista)
    for indice in range(1, tam_lista):
        posicion = indice
        while posicion > 0 and not funcion_criterio(
                get_element(mi_lista, posicion - 1),
                get_element(mi_lista, posicion)):
            exchange(mi_lista, posicion, posicion - 1)
            posicion -= 1
    return mi_lista


def shell_sort(mi_lista, funcion_criterio):
    """ Ordena la lista usando el algoritmo de Shell (Shell Sort).

        :param mi_lista: La lista a ordenar.
        :type mi_lista: dict
        :param funcion_criterio: Función de comparación. Retorna True si
            el primer elemento debe ir antes que el segundo.
        :type funcion_criterio: function

        :returns: La lista ordenada.
        :rtype: dict
    """
    tam_lista = size(mi_lista)
    brecha = 1
    while brecha < tam_lista // 3:
        brecha = 3 * brecha + 1
    while brecha >= 1:
        for indice in range(brecha, tam_lista):
            posicion = indice
            while posicion >= brecha and not funcion_criterio(
                    get_element(mi_lista, posicion - brecha),
                    get_element(mi_lista, posicion)):
                exchange(mi_lista, posicion, posicion - brecha)
                posicion -= brecha
        brecha //= 3
    return mi_lista
