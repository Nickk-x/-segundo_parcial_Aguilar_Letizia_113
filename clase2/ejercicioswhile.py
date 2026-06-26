"""
WHILE
#Contadores - Acumuladores - Máximos y mínimos

"""

#region Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.
variable = 11

while variable > 1:
    variable -=1

    print(variable)

#endregion

#region Mostrar 10 repeticiones de números descendentes desde el 10 al 1

descendente = 0

while descendente < 10:
    descendente += 1
    print(descendente)
#endregion

#Region mostrar la suma de los números desde el 1 hasta el 10.

resultado = 0 

numero = 1 # Puedes empezar en 1 directamente

while numero <= 10: # 2. Condición (mientras numero sea menor o igual a 10)
    resultado += numero 
    numero += 1

print(f"La suma total de los numeros es: {resultado}")

#endregion

#region mostrar la suma de los números pares desde el 1 hasta el 10.

numero = 1
suma_par = 0

while numero <= 10:
    if numero % 2 == 0: #Esto sirve para filtrar los numeros pares
        suma_par += numero
    numero += 1 

print(f"La suma de los numeros pares es: {suma_par}")

#endregion

#regionSolicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. 
# Mostrar la suma y el promedio por pantalla.

intentos = 1

suma = 0

while intentos <= 5:
    numero = int(input("Ingresa un numero: "))
    intentos += 1
    suma += numero

promedio = suma / intentos

print(f"La suma de los numeros es: {suma}, y el promedio es: {promedio}")

#endregion

#region Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números ingresados y el promedio de los mismos.

clave = input("Ingrese lo que quiera: ")

while clave != "basta":
    clave = input("Ingrese lo que quiera: ")

print(f"Hasta la proximaa 👋👋")

#endegion

#region Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números positivos y el producto de los negativos.

suma_positiva = 0

suma_negativa = 0

while True:
    numero = input("Ingrese el numero que quiera: ")

    if numero == "ya ta" or "":
        break #<=== Con el break rompo el bucle, debo poner el while con el break
    else:
        numero_a_sumar = int(numero)
        if numero_a_sumar > 0:
            suma_positiva += numero_a_sumar
        elif numero_a_sumar < 0:
            suma_negativa += numero_a_sumar

print(f"Esta es la suma de los numeros positivos: {suma_positiva} y los negativos: {suma_negativa}")
#endregion

#region Ingresar 10 números enteros. Determinar el máximo y el mínimo.

while True:
    numero = input("Ingrese el numero que quiera: ")

    if numero == "ya ta" or "":
        break #<=== Con el break rompo el bucle, debo poner el while con el break
    else:
        numero_a_sumar = int(numero)
        if numero_a_sumar > 0:
            suma_positiva += numero_a_sumar
        elif numero_a_sumar < 0:
            suma_negativa += numero_a_sumar

print(f"Esta es la suma de los numeros positivos: {suma_positiva} y los negativos: {suma_negativa}")
#endregion

#region Solicitar al usuario que ingrese como mínimo 5 números. 
# Calcular la suma de los números ingresados y el promedio de los mismos.

intentos = 5
suma_numeros = 0

while intentos != 0:
    numero_ingresado = int(input(f"Ingrese un numero, tiene {intentos} intentos: "))
    suma_numeros += numero_ingresado
    intentos -= 1

promedio = suma_numeros / 5

print(f"La suma de los numeros es {suma_numeros} y el promedio de los numeros es {promedio}")
#endregion

#region Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. 
# Calcular la suma de los números ingresados y el promedio de los mismos.

numero_maximo = 0

numero_minimo = 0

intentos = 10
minimos_intentos = 5
suma_numeros = 0
primer_bandera = True
segunda_bandera = True

while intentos != 0:
    numero_ingresado = int(input(f"Ingrese un numero tiene {intentos} intentos: "))
    if primer_bandera == True or numero_ingresado > numero_maximo:
        numero_maximo = numero_ingresado
        primer_bandera = False
    if segunda_bandera == True or numero_ingresado < numero_minimo:
        numero_minimo = numero_ingresado
        segunda_bandera = False
    suma_numeros += numero_ingresado
    intentos -=1

promedio = suma_numeros / 10
print(f"El numero mayor es {numero_maximo} y el menor es {numero_minimo},")
print(f"la suma de los numeros es {suma_numeros} y el promedio de estos es {promedio}")

#endregion


















































