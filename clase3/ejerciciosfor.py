#region Mostrar los números ascendentes desde el 1 al 10

for numero in range(1, 11):
    print(numero)

#endregion

#region Mostrar los números descendentes desde el 10 al 1

for numero in range(10, 0, -1):
    print(numero)

#endregion

#region Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.

numero_ingresado = int(input("Ingrese un numero: "))

for numero in range(0, numero_ingresado + 1):
    print(numero)

#endregion

#region Ingresar un número y mostrar la tabla de multiplicar de ese número. 
# Por ejemplo si se ingresa el numero 5:
#	5 x 0 = 0
#	5 x 1  = 5
#	5 x 2 = 10
#	5 x 3  = 15 …

tabla_maxima = 10

numero_ingresado = int(input("Ingrese el numero a multiplicar: "))

for i in range (tabla_maxima + 1):
    resultado = numero_ingresado * i
    print(f" {numero_ingresado} x {i} = {resultado}")

#endregion

#region Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. 
# Mostrar la suma y el promedio de todos los números.

suma_numeros = 0
contador = 0
promedio = 0

for i in range(10):
    #El input debe estar dentro del for para que se repita las veces pedidas
    numero_ingresado = int(input("Ingrese un numero, tiene {intentos} intentos como maximo o ingrese ¨0¨ para detenerel programa: ")) 
    if numero_ingresado == 0:
        break
    else:
        contador += 1
        suma_numeros += numero_ingresado
if contador > 0:
    promedio = suma_numeros / contador 


print(f"La suma de los numeros es {suma_numeros} y el promedio de los numeros es {promedio:.2f}")


#endregion

#region Imprimir los números múltiplos de 3 entre el 1 y el 10.

numero_maximo = 10
numero_minimo = 1
multiplo = 3

for i in range (numero_minimo, numero_maximo):
    if i % multiplo != 0:
        continue

    print(f"{i} es multiplo de {multiplo}")

#endregion

#region Mostrar los números pares que hay desde la unidad hasta el número 50. (inodad es 1)

numero_maximo = 50
numero_minimo = 1
multiplo = 2

for i in range (numero_minimo, numero_maximo):
    if i % multiplo != 0:
        continue

    print(f"{i} es multiplo de {multiplo}")


#endregion

#region Realizar un programa que permita mostrar una pirámide de números. 
# Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:

numero_ingresado = int(input("Ingrese un numero: "))

piramide= 0

for i in range (1, numero_ingresado + 1):
    piramide *= 10
    piramide += i
    
    print(piramide)

#endregion

#region Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. 
# Mostrar la cantidad de divisores encontrados.

numero_ingresado = int(input("Ingrese un numero: "))

contador = 0

for i in range (1, numero_ingresado + 1):
    
    if numero_ingresado % i == 0:
        contador += 1
        print(f"{i} es divisor de {numero_ingresado}")
    else:
        print(f"{i} no es dividor de {numero_ingresado}")

print(f"La cantidad de divisores es {contador}")
    

#endregion

#region Ingresar un número. Determinar si el número es primo o no.

numero_ingresado = int(input("Ingresa un numero: "))

for i in range (1, numero_ingresado + 1):
    if numero_ingresado % i == 0:
        contador_divisores += 1
        if contador_divisores == 2:
            resultado = "es primo"
        else:
            resultado = "no es primo"
    print(f"{i} {resultado}")

#endregion

#region Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. 
# Informar cuántos números primos se encontraron.

numero_ingresado = int(input("Ingrese un numero: "))
contador_primos = 0

for i in range (1, numero_ingresado + 1):
    contador_divisores = 0
    for j in range(1, i + 1):
        if i % j == 0:
            contador_divisores += 1
    if contador_divisores == 2:
        resultado = "es primo"
        contador_primos += 1
    else:
        resultado = "no es primo"
    print(f"{i} {resultado}")

print(f"Se encontraron {contador_primos} primos")


#endregion
