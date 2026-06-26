"""
Arrays unidimensionales

1- Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.
2- Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1.
3- Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números. 
4- Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.
5- Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.
6- Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.
7- Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.
8- Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
    a. Una lista de nombres (lista_nombres).
    b. Un nombre a buscar en la lista (nombre_antiguo).
    c. Un nombre de reemplazo (nombre_nuevo).
La función debe realizar las siguientes acciones:
Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por nombre_nuevo.
Retornar la cantidad total de reemplazos realizados.
9- Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la intersección de los dos arrays.
10- Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la unión de los dos arrays.
11- Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la diferencia de los dos arrays.
"""

import inputs as I

def crear_lista(largo : int, valor_predeterminado : any = 0) -> list:
    lista_vacia = []
    for i in range(largo):
        lista_vacia.append(valor_predeterminado)
    
    return lista_vacia
"""
lista_nueva = crear_lista(5)
print(lista_nueva)
"""
def crear_lista_cargada(largo : int):
    lista_nueva = crear_lista(largo)

    for i in range(largo):
        lista_nueva[i] = I.pedir_entero(f"Ingrese un numero para el indice {i}: ")
    return lista_nueva

#lista_cargada = crear_lista_cargada(5)

def promediar_lista(lista : list) -> float:
    largo_lista = len(lista)
    acumulador = 0

    for i in range(largo_lista):
        acumulador += lista[i]

    promedio = acumulador / largo_lista

    return promedio

def multiplicar_lista(lista : list) -> int:
    producto = 1

    for i in range(largo_lista):
        productor *= lista[i]

    return producto

def filtrar_lista(lista: list, valor : int = 0, mayor_que : bool = True) ->list:
    lista_nueva = []

    for i in range(len(lista)):
        if mayor_que:
            if lista[i] > valor:
                lista_nueva.append(lista[i])
        else:
            if lista[i] < valor:
                lista_nueva.append(lista[i])
    return lista_nueva

def promediar_lista_positivos(lista: list) -> float:
    lista_positivos = filtrar_lista(lista, 0, True)
    promedio =promediar_lista(lista_positivos)
    return promedio
"""
lista_cargada = crear_lista_cargada(5)
print(promediar_lista(lista_cargada))
print(lista_cargada)


lista_a_promediar = [-1, 6, -3, -7, 4, 8]

promedio_obtenido = promediar_lista_positivos(lista_a_promediar)
print(promedio_obtenido)

"""

def hallar_maximo(lista : int) -> int:
    """
    Variable que contanga el maximo
    Variable que contenga el indice
    Recorrer la lista
    Comprobar si el valor es superior a la variable
    """

    valor_maximo = lista[0]
    indice_valor_maximo = 0

    for i in range(1, len(lista)):
        if lista[i] > valor_maximo:
            valor_maximo = lista[i]
            indice_valor_maximo = i

    return indice_valor_maximo

def hallar_maximo(lista : list) -> None:
    valor_maximo = lista[0]
    """
    esto es para mostrar posicion
    for i in range(1, len(lista)):
        if lista[i] > valor_maximo:
            valor_maximo = lista[i]
    
    for i in range(len(lista)):
        if lista[i] == valor_maximo:
            print(i)
    """

    for i in range(1, len(lista)):
        if lista [i] > valor_maximo:
            valor_maximo = lista[i]
            lista_indices_maximos = [i]
        elif lista[i] == valor_maximo:
            lista_indices_maximos.append(i)
    
    print(lista_indices_maximos)
"""
lista_a_hallar_maximo = [10, 604, 7, 39, 604, 48, 604, 10, 30, 604]
indice_maximo_hallado = hallar_maximo(lista_a_hallar_maximo)
#print(indice_maximo_hallado)
"""

def reemplaza_nombres(lista_nombres : list, nombre_antiguo : str, nombre_nuevo : str) -> int:
    contador_reemplazos = 0
    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_antiguo:
            lista_nombres[i] = nombre_nuevo
            contador_reemplazos += 1
    return contador_reemplazos

lista_a_reemplazar = ["Lisandro", "josep", "Juan", "Agustin", "Nicolas", "josep", "Pepito", "Osvaldo", "josep"]
nombre_viejo = "josep"
nombre_actual = "joseppsito"


print(lista_a_reemplazar)
cantidad_reemplazos = reemplaza_nombres(lista_a_reemplazar, nombre_viejo, nombre_actual)
print(lista_a_reemplazar)










































