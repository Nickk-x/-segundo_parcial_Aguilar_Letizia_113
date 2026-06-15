"""
for

1-Mostrar los números ascendentes desde el 1 al 10
2-Mostrar los números descendentes desde el 10 al 1
3-Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.
4-Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:

	5 x 0 = 0
	5 x 1  = 5
	5 x 2 = 10
	5 x 3  = 15 …

5-Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.
6-Imprimir los números múltiplos de 3 entre el 1 y el 10.
7-Mostrar los números pares que hay desde la unidad hasta el número 50.
8-Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:


9-Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.
10Ingresar un número. Determinar si el número es primo o no.
11-Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.
"""

#region ejercicio 1
"""
for i in range(1, 11):
    print(i)
"""
#endregion

#region ejercicio 2
"""
for u in range(10, 0, -1):
    print(u)

    numero_maximo = 25

for j in range(0, numero_maximo):
    print(numero_maximo - j)
"""
#endregion

#region ejercicio 3
"""
numero_ingresado = int(input("Ingrese un numero: "))
for k in range(0, numero_ingresado +1):
    print(k)
"""
#endregion

#region ejercicio 4
"""
tabla_maxima = 10
numero_ingresado = int(input("Ingrese un numero: "))

for i in range(tabla_maxima +1):
    resultado = numero_ingresado * i
    print(f"{numero_ingresado} x {i} = {resultado}")
"""

#endregion

#region ejercicio 5
"""
cantidad_maxima = 10
contador = 0
suma = 0
for i in range(cantidad_maxima):
    numero_ingresado = int(input(f"Ingrese un numero, tiene [{cantidad_maxima - i}]: "))
    if numero_ingresado == 0:
        break
    contador += 1
    suma += numero_ingresado

promedio = suma / contador

print(f"la suma de los numeros ingresados es de {suma}, teniendo un promedio de {promedio:.2f}")
"""
#endregion

#region ejercicio 6 y 7
"""
numero_maximo = 100
numero_minimo = 1
multiplo = 2

for i in range(numero_minimo, numero_maximo):
    if i % multiplo != 0:
        continue 
    print(f"{i} es multiplo de {multiplo}")
"""

#endregion

#region ejercicio 8

numero_ingresado = int(input("Ingrese un numero:  "))
numero_actual = 0

for i in range(1, numero_ingresado + 1 ):
    numero_actual *= 10
    numero_actual += i

    print(numero_actual)
#endregion




#region

#endregion














