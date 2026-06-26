import inputs as I

matriz_alumnos = [["Gabriel", "Pulido", 70, 11090],
                  ["Tomas", "Soengas", 71, 32003]]


def mostrar_alumno(alumno : list) -> None:
    print(f'''______________
Apellido y nombre: {alumno[1]}, {alumno[0]}
Nota: {alumno[2]}
Legajo: {alumno[3]}''')
    

def mostrar_alumnos(alumnos : list) -> None:
    for i in range(len(alumnos)):
        mostrar_alumno(alumnos[i])

#                 matriz_al         Soengas
def buscar_alumnos(matriz : list, valor_a_buscar : any, columna : int, cantidad : int = -1) -> int:
    indices_encontrados = []
    for i in range(len(matriz)):
        if valor_a_buscar == matriz[i][columna]:
            indices_encontrados.append(i) 
            if len(indices_encontrados) == cantidad:
                break

    return indices_encontrados


def buscar_indices(lista : list, valor_a_buscar : any) -> list:
    lista_indices = []

    for i in range(len(lista)):
        if lista[i] == valor_a_buscar:
            lista_indices.append(i)

    return lista_indices

def agregar_alumno(matriz : int) -> None:
    nombre_nuevo = input("Ingrese un nombre: ")
    apellido_nuevo = input("Ingrese un apellido: ")
    nota_nueva = I.pedir_entero("Ingrese la nota (0-100)","ERROR: La nota debe estar entre 0 y 100", 0, 100)

    legajo_nuevo = I.pedir_entero("Ingrese el legajo del alumno (5 digitos): ","ERROR: El legajo debe contener 5 digitos: ", 10000, 99999)

    legajo_encontrado = buscar_alumnos(matriz, legajo_nuevo, 3, 1)

    while len(legajo_encontrado) !=0:
        legajo_nuevo = I.pedir_entero("ERROR: Ese legajo ya se encuentra regsitrado: ","ERROR: El legajo debe contener 5 digitos: ", 10000, 99999)
        legajo_encontrado = buscar_alumnos(matriz, legajo_nuevo, 3, 1)
    
    alumno_nuevo = [nombre_nuevo, apellido_nuevo, nota_nueva, legajo_nuevo]
    matriz.append(alumno_nuevo)

def modificar_alumno(matriz : list, lista_encabezados : list) -> None:
    mensaje = "Ingrese un alumno a modificar:\n"
    for i in range(len(matriz)):
        mensaje += f"{i}\t || {matriz[i][1]} {matriz[i][0]}\n"

    alumno_seleccionado = I.pedir_entero(mensaje, "ERROR: El alumno no se encuentra registrado", 0, len(matriz))

    mensaje = "Ingrese un campo a modificar:\n"
    for i in range(len(lista_encabezados)):
        mensaje += f"{i}\t || {lista_encabezados[i]}\n"

    match campo_seleccionado:
        case 0:
            dato_nuevo = input("Ingrese el nuevo nombre: ")
        case 1:
            dato_nuevo = input("Ingrese el nuevo apellido: ")
        case 2:
            dato_nuevo = I.pedir_entero("Ingrese la nota (0-100)","ERROR: La nota debe estar entre 0 y 100", 0, 100)
        case 3:
            dato_nuevo = I.pedir_entero("Ingrese el legajo del alumno (5 digitos): ","ERROR: El legajo debe contener 5 digitos: ", 10000, 99999)
            legajo_encontrado = buscar_alumnos(matriz, dato_nuevo, 3, 1)
            while len(legajo_encontrado) !=0:
                dato_nuevo = I.pedir_entero("ERROR: Ese legajo ya se encuentra regsitrado: ","ERROR: El legajo debe contener 5 digitos: ", 10000, 99999)
                legajo_encontrado = buscar_alumnos(matriz, dato_nuevo, 3, 1)
            
    matriz[alumno_seleccionado][campo_seleccionado] = dato_nuevo

    campo_seleccionado = I.pedir_entero(mensaje, "ERROR: El campo no es valido: ", 0, len(lista_encabezados))

modificar_alumno(matriz_alumnos,["Nombre", "Apellido", "Nota", "Legajo"])

#agregar_alumno(matriz_alumnos)
#mostrar_alumnos(matriz_alumnos)

indices_encontrados = buscar_alumnos(matriz_alumnos, 70, 2, 1)

print(indices_encontrados)
for i in range(len(indices_encontrados)):
    mostrar_alumno(matriz_alumnos[indices_encontrados[i]])




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

