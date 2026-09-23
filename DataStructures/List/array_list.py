"""
  Implementación del TAD Lista usando una estructura de arreglo (ArrayList).

  La lista se representa como un diccionario con las llaves:
    - 'elements': lista nativa de Python con los elementos almacenados.
    - 'size': número de elementos almacenados en la lista.
"""


def new_list():
    """ Crea una lista vacía.

        :returns: Un diccionario que representa la lista vacía.
        :rtype: dict
    """
    nueva_lista = {
        'elements': [],
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
    mi_lista['elements'].insert(0, elemento)
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
    mi_lista['elements'].append(elemento)
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
    """ Retorna el primer elemento de la lista.

        :param mi_lista: La lista a examinar.
        :type mi_lista: dict

        :returns: El primer elemento de la lista.
        :rtype: any
    """
    if mi_lista['size'] == 0:
        return None
    return mi_lista['elements'][0]


def last_element(mi_lista):
    """ Retorna el último elemento de la lista.

        :param mi_lista: La lista a examinar.
        :type mi_lista: dict

        :returns: El último elemento de la lista.
        :rtype: any
    """
    if mi_lista['size'] == 0:
        return None
    return mi_lista['elements'][mi_lista['size'] - 1]


def get_element(mi_lista, posicion):
    """ Retorna el elemento en la posición dada de la lista (0-indexado).

        :param mi_lista: La lista a examinar.
        :type mi_lista: dict
        :param posicion: La posición del elemento a retornar.
        :type posicion: int

        :returns: El elemento en la posición indicada.
        :rtype: any
    """
    return mi_lista['elements'][posicion]


def remove_first(mi_lista):
    """ Elimina el primer elemento de la lista y lo retorna.

        :param mi_lista: La lista a modificar.
        :type mi_lista: dict

        :returns: El elemento eliminado.
        :rtype: any
    """
    if mi_lista['size'] == 0:
        return None
    elemento = mi_lista['elements'].pop(0)
    mi_lista['size'] -= 1
    return elemento


def remove_last(mi_lista):
    """ Elimina el último elemento de la lista y lo retorna.

        :param mi_lista: La lista a modificar.
        :type mi_lista: dict

        :returns: El elemento eliminado.
        :rtype: any
    """
    if mi_lista['size'] == 0:
        return None
    elemento = mi_lista['elements'].pop()
    mi_lista['size'] -= 1
    return elemento


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
    mi_lista['elements'].insert(posicion, elemento)
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
    tam_lista = mi_lista['size']
    posicion = -1
    if tam_lista > 0:
        seguir_buscando = True
        indice = 0
        while indice < tam_lista and seguir_buscando:
            info = get_element(mi_lista, indice)
            if funcion_comparacion(elemento, info) == 0:
                posicion = indice
                seguir_buscando = False
            indice += 1
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
    if 0 <= posicion < mi_lista['size']:
        del mi_lista['elements'][posicion]
        mi_lista['size'] -= 1
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
    mi_lista['elements'][posicion] = nueva_info
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
    elementos = mi_lista['elements'][posicion:posicion + num_elementos]
    sublista['elements'] = list(elementos)
    sublista['size'] = len(sublista['elements'])
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


def merge_sort(lista, crit):
    tam = size(lista)
    if tam > 1:
        mitad = tam // 2
        izq = sub_list(lista, 0, mitad)
        der = sub_list(lista, mitad, tam - mitad)
        merge_sort(izq, crit)
        merge_sort(der, crit)
        mezclar(lista, izq, der, crit)
    return lista


def mezclar(lista, izq, der, crit):
    t_izq = size(izq)
    t_der = size(der)
    i_izq = 0
    i_der = 0
    i_res = 0
    while i_izq < t_izq and i_der < t_der:
        e_izq = get_element(izq, i_izq)
        e_der = get_element(der, i_der)
        if crit(e_izq, e_der):
            change_info(lista, i_res, e_izq)
            i_izq += 1
        else:
            change_info(lista, i_res, e_der)
            i_der += 1
        i_res += 1
    while i_izq < t_izq:
        change_info(lista, i_res, get_element(izq, i_izq))
        i_izq += 1
        i_res += 1
    while i_der < t_der:
        change_info(lista, i_res, get_element(der, i_der))
        i_der += 1
        i_res += 1
    return lista


def quick_sort(lista, crit):
    tam = size(lista)
    if tam > 1:
        p_piv = tam // 2
        piv = get_element(lista, p_piv)
        men = new_list()
        may = new_list()
        for idx in range(tam):
            if idx != p_piv:
                elem = get_element(lista, idx)
                if crit(elem, piv):
                    add_last(men, elem)
                else:
                    add_last(may, elem)
        quick_sort(men, crit)
        quick_sort(may, crit)
        i_res = 0
        for idx in range(size(men)):
            change_info(lista, i_res, get_element(men, idx))
            i_res += 1
        change_info(lista, i_res, piv)
        i_res += 1
        for idx in range(size(may)):
            change_info(lista, i_res, get_element(may, idx))
            i_res += 1
    return lista
