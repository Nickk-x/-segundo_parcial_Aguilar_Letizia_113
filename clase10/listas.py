"""
Vector

¿Que es un vector?
Un arreglo unidimensional, tambien conocido como vector, es una estructura de datos que organiza elementos 
de manera lineal, es decir, dispuestos uno tras otro en una sola dimension. Cada elemento tiene una posicion 
unica y puede ser accedido utilizando un unico indice.
"""
"""
lista = [2, 4, 10, 5, 15, 3]
#        0  1   2  3   4  5

print(lista[4])

"""

"""
Beneficios del uso de vectores/listas:

~Organizacion y gestion de datos: Las listas permiten agrupar datos relacionados en una sola estructura, 
                                simplificando su manejo y organizacion.
~Acceso y manipulacion eficiente: Las listas facilitan el acceso, la iteracion y la modificacion de datos mediante
                                indices, lo que es mas eficiente que manejar variables individuales.
~Escalabilidad: Las listas son flexibles y escalables, permitiendo ajustar la cantidad de datos sin necesidad de crear
                nuevas variables.
~Operaciones en lote: Las listas permiten realizar operaciones en grupo, como ordenar y filtrar, de manera mas
                    eficiente que aplicar operaciones individuales a cada variable.
"""
import inputs as I #Voy a usar esta
"""
notas_alumnos = []

seguir = "s"

while seguir == "s":

    nueva_nota = I.pedir_entero("Ingrese la nota: ", "Error: La nota debe estar entre 2 y 10: ", 2, 10 )
    notas_alumnos.append(nueva_nota)

    seguir = input("¿Desea seguir? (s/n)")

print(notas_alumnos)

notas_alumnos = [4, 7, 5, 2, 7, 10, 8, 6]
acumulador_notas = 0

for i in range(len(notas_alumnos)):
    acumulador_notas += notas_alumnos[i]
    print(f"{i} -> {notas_alumnos[i]}")
    

print(acumulador_notas)

"""


"""
.append

ve nuestra lista y añade despues de la ultima posicion el valor ingresado
[] -> [x]

[0, 0, 0] -> [0, 0, 0, x]

"""







