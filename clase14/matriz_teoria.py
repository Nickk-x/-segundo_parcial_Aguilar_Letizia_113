"""
Pensemos que tenemos dos listas, de nombres y apellidos

                    1         2         3        4        5           6
Y
| lista_nombres   | Gabriel | Nicole  | Tomas  | Lucas  | Lisandro | Victoria
|                                                                    
| lista_apellidos | Pulido  | Cornejo | Dumano | Palmer | Miranda  |

"""
#           Nombre      Apellido Nota Legajo
alumno_1 = ["Gabriel", "Pulido", 70, 11090]
alumno_2 = ["Tomas", "Soengas", 71, 32003]

matriz_alumnos = [alumno_1, alumno_2]

#print(alumno_1[1])
#print(alumno_2[1])

#print(lista_alumnos[1][2])

def mostrar_alumno(alumno : list) -> None:
    print(f'''______________
Apellido y nombre: {alumno[1]}, {alumno[0]}
Nota: {alumno[2]}
Legajo: {alumno[3]}''')
    

def mostrar_alumnos(alumnos : list) -> None:
    for i in range(len(alumnos)):
        mostrar_alumno(alumnos[i])

#                 matriz_al         Soengas
def buscar_alumnos(matriz : list, valor_a_buscar : any, columna : int) -> int:
    indices_encontrados = []
    for i in range(len(matriz)):
        if valor_a_buscar == matriz[i][columna]:
            indices_encontrados.append(i) 

    return indices_encontrados

#mostrar_alumno(alumno_1)
#mostrar_alumno(alumno_2)
#mostrar_alumnos(matriz_alumnos)
indices = buscar_alumnos(matriz_alumnos, 11090, 3)

print(indices)

for i in range(len(indices)):
    mostrar_alumno(matriz_alumnos[indices[i]])








