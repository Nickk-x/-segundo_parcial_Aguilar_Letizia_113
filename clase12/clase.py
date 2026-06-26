import inputs as I

"""
Listas Paralelas
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

notas_alumnos = [4, 7, 8, 2, 10, 9, 4, 6, 7, 7]
nombres_alumnos = ["Agustin", "Gabriel", "Nicolas", "Pepito", "Eduardo", "Alejo", "Lucas", "Melina", "Joaquin", "Eduardo"]
asistencia_alumnos = [.8, 1, .6, .7, .9, .7, .8, .2, .6, 1]


"""
indice_desaprobado = -1

for i in range(len(notas_alumnos)):
    if notas_alumnos[i] == 2 or asistencia_alumnos[i] < .7:
        print(f"{nombres_alumnos[i]} desaprobo")
"""

#agregar_alumno(notas_alumnos, nombres_alumnos, asistencia_alumnos)
#modificar_alumno(notas_alumnos, nombres_alumnos, asistencia_alumnos, 1)
#eliminar_alumno(notas_alumnos, nombres_alumnos, asistencia_alumnos, 4)
mostrar_alumnos(notas_alumnos, nombres_alumnos, asistencia_alumnos)

nombre_a_buscar = "Eduardo"
indices_obtenidos = buscar_indices(nombres_alumnos, nombre_a_buscar)


#indice_eduardo = buscar_indices(nombres_alumnos, "Eduardo")[0]
#nota_eduardo = notas_alumnos[indice_eduardo]

#print(f"La nota de Eduardo es {nota_eduardo}/10")
for i in range(len(indices_obtenidos)):
    indice_actual = indices_obtenidos[i]
    nota_eduardo = notas_alumnos[indice_actual]

    print(f"La nota de {nombre_a_buscar} es {nota_eduardo}/10 y su asistencia {asistencia_alumnos[indice_actual] * 100}%")




