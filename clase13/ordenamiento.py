lista_a = [1, 7, 4, 8, 3, 9, 5, 14, 7, 4, 3]

lista_b = [5, 7, 2, 3, 4]

"""
Algoritmos de ordenamiento

¿Que son?
    Los algoritmos de ordenamiento son un conjunto de instrucciones que buscan organizar elementos en un orden 
    particular (criterio de ordenamiento)
¿Para que sirven?
    para ordenar como querramos o quiera el usuario.

Clasificacion
    La cantidad de intercambios
    El numero de comparaciones
    La cantidad de espacio adicional requerido
    Utilizan recursividad o no

Bubble sort
                                a > b ?
    lista = [5, 7, 2, 3, 4] 5 = a | 7 = b b recorre toda la lista y n encuentra un numero menor que 2

            [2, 7, 5, 3, 4] 7 = a | 5 = b recorre la lista y encuentra que 3 es menor que todos los restantes
            [2, 3, 7, 5, 4] 7 = a | 5 = b recorre la lista y encuentra que 4 es menor que todos los restantes
            [2, 3, 4, 7, 5] 7 = a | 5 = b recorre la lista y encuentra que 5 es menor que todos los restantes
            [2, 3, 4, 5, 7] Lista ordenada
"""

def ordenar_lista(lista : list) -> None:
    for a in range(len(lista)-1):
        for b in range(a+1, len(lista)):

            if lista[a] > lista[b]:
                aux = lista[a]
                lista[a] = lista[b]
                lista[b] = aux

ordenar_lista(lista_b)
print(lista_b)


ordenar_lista(lista_a)
print(lista_a)


















