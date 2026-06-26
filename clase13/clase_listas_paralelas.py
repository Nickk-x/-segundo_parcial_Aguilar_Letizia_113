import inputs as I

"""
Listas Paralelas y ordenamiento
"""


def buscar_indices(lista : list, valor_a_buscar : any) -> list:
    lista_indices = []

    for i in range(len(lista)):
        if lista[i] == valor_a_buscar:
            lista_indices.append(i)

    return lista_indices

def agregar_alumno(lista_notas : int, lista_nombres : list, lista_asistencias : list) -> None:
    nota_a_agregar = I.pedir_entero("Ingrese la nota del nuevo alumno: ", "ERROR: La nota tiene que estarv entre 2 y 10: ", 2, 10)
    nombre_a_agregar =input("Ingrese el nombre del nuevo alumno: ")
    asistencia_a_agregar = I.pedir_float("Ingrese la asistencia del alumno: ", "ERROR: La asistencia tiene que estar entre 0 y 1: ", 0, 1)

    lista_notas.append(nota_a_agregar)
    lista_nombres.append(nombre_a_agregar)
    lista_asistencias.append(asistencia_a_agregar)

def modificar_alumno(lista_notas : list, lista_nombres : list, lista_asistencias : list, indice : int, ) -> None:
    nota_modificada = I.pedir_entero("Ingrese la nota del nuevo alumno: ", "ERROR: La nota tiene que estar entre 2 y 10: ", 2, 10)
    nombre_modificado = input("Ingrese el nombre del nuevo alumno: ")
    asistencia_modificada = I.pedir_float("Ingrese la asistencia del alumno: ", "ERROR: La asistencia tiene que estar entre 0 y 1: ", 0, 1)

    lista_notas[indice] = nota_modificada
    lista_nombres[indice] = nombre_modificado
    lista_asistencias[indice] = asistencia_modificada

def eliminar_alumno(lista_notas : list, lista_nombres : list, lista_asistencias : list, indice : int, ) -> None:
    lista_notas.pop(indice)
    lista_nombres.pop(indice)
    lista_asistencias.pop(indice)
    pass

def mostrar_alumnos(lista_notas : list, lista_nombres : list, lista_asistencias : list) -> None:
    for i in range(len(lista_nombres)):
        if lista_notas[i] < 10:
            nota_parseada = f"0{lista_notas[i]}/10"
        else:
            nota_parseada = "10/10"
        print(f"{i} -> {lista_nombres[i]}\t || {nota_parseada} || {lista_asistencias[i] * 100}%")

def ordenar_lista(lista : list) -> None:
    for a in range(len(lista)-1):
        for b in range(a+1, len(lista)):

            if lista[a] > lista[b]:
                aux = lista[a]
                lista[a] = lista[b]
                lista[b] = aux

def ordenar_listas_paralelas(lista_a_ordenar : list, indice_criterio : int = 0) -> None:

    lista_criterio = lista_a_ordenar[indice_criterio]

    for i in range(len(lista_criterio)-1):
        for j in range(i+1, len(lista_criterio)):
            if lista_criterio[i] > lista_criterio[j]:
                for k in range(len(lista_a_ordenar)):
                    """
                    k 0 -> nombres_alumnos
                    k 1 -> notas_alumnos
                    k 2 -> asistencia_alumnos

                    k 0 -> intercambiar_posiciones(lista_nombres, i, j)
                    k 1 -> intercambiar_posiciones(lista_notas, i, j)
                    k 2 -> intercambiar_posiciones(lista_asistencia, i, j)
                    """
                    intercambiar_posiciones(lista_a_ordenar[k], i, j)

def intercambiar_posiciones(lista : list, indice_i : int, indice_j : int) ->None:
    aux = lista[indice_i]
    lista[indice_i] = lista[indice_j]
    lista[indice_j] = aux 

"""
def ordenar_listas_paralelas(lista_notas : list, lista_nombres : list, lista_asistencia : list) -> None:
    for i in range(len(lista_notas)-1):
        for j in range(i+1, len(lista_notas)):
            if lista_notas[i] > lista_notas[j]:

                aux = lista_notas[i]
                lista_notas[i] = lista_notas[j]
                lista_notas[j] = aux

                aux = lista_nombres[i]
                lista_nombres[i] = lista_nombres[j]
                lista_nombres[j] = aux

                aux = lista_asistencia[i]
                lista_asistencia[i] = lista_asistencia[j]
                lista_asistencia[j] = aux 

Desventajas de def ordenar listas_paralelas
    Si quiero mas listas, tengo que modificar el codigo
    repeticion del codigo
    lo vamos a mejorar..
"""

notas_alumnos = [4, 7, 8, 2, 10, 9, 4, 6, 7, 7]
nombres_alumnos = ["Agustin", "Gabriel", "Nicolas", "Pepito", "Eduardo", "Alejo", "Lucas", "Melina", "Joaquin", "Eduardo"]
asistencia_alumnos = [.8, 1, .6, .7, .9, .7, .8, .2, .6, 1]

#agregar_alumno(notas_alumnos, nombres_alumnos, asistencia_alumnos)
#modificar_alumno(notas_alumnos, nombres_alumnos, asistencia_alumnos, 1)
eliminar_alumno(notas_alumnos, nombres_alumnos, asistencia_alumnos, 4)
ordenar_lista(notas_alumnos)
ordenar_listas_paralelas([nombres_alumnos, notas_alumnos, asistencia_alumnos], 2)
mostrar_alumnos(notas_alumnos, nombres_alumnos, asistencia_alumnos)


nombre_a_buscar = "Eduardo"
indices_obtenidos = buscar_indices(nombres_alumnos, nombre_a_buscar)

for i in range(len(indices_obtenidos)):
    indice_actual = indices_obtenidos[i]
    nota_eduardo = notas_alumnos[indice_actual]

    print(f"La nota de {nombre_a_buscar} es {nota_eduardo}/10 y su asistencia {asistencia_alumnos[indice_actual] * 100}%")



