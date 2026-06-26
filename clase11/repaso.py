import inputs as I

lista_notas_alumnos = [6, 8, 7, 2, 4, 6, 10, 6, 8, 9]
#                      ^  ^  ^  ^  ^  ^  ^
#                      0  1  2  3  4  5  6


#region LECTURA Y ESCRITURA DE DATOS
print(lista_notas_alumnos[3])
lista_notas_alumnos[3] = 4
print(lista_notas_alumnos[3])
#endregion

#region Adicion y subtraccion de elementos
lista_notas_alumnos.append(8)
lista_notas_alumnos.pop(1) #Si no especificamos se elimina uno al azar
#endregion

"""
Para evitar hacer esto vamos a usar for!
promedio = (lista_notas_alumnos[0] + lista_notas_alumnos[1] + lista_notas_alumnos[2]...) / 7
"""

"""
RANGE
-----

start -> Numero desde el cual se empieza
end -> Numero en el que termina
step -> Salto que se da entre numero y numero

range(10) -> ( =0, 10, =1)
range(5, 15) -> [5;15)

range()

"""
"""
# 0, 1, 2, 3, 4, 5, 6
#Es lectura y escritura
for i in range(7):
    print(f"Nota del alumno {i + 1}: {lista_notas_alumnos[i]}")

#solo lectura
for nota in lista_notas_alumnos:
    nota *= 10
"""

#region recorrer lista y aplicar calculos

acumulador = 0
largo_lista = len(lista_notas_alumnos)

#El len es fundamental para que abarque todos los datos

for i in range(largo_lista):
    print(f"Nota del alumno {i+1}: {lista_notas_alumnos[i]}")
    acumulador += lista_notas_alumnos[i]

promedio = acumulador / largo_lista
print(f"{promedio:.2f}")
#endregion

























print(lista_notas_alumnos)