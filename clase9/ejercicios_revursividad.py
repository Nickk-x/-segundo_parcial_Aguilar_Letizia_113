"""
1- Realizar una funcion recursiva que calcule la suma de los primeros numeros naturales
2- Realizar una funcion recursiva que calcule la potencia de un numero
3- Realizar una funcion recursiva que permita realizar la suma de los digitos de un numero:
4- Realizar una funcion recursiva para calcular el numero de Fibonacci de un numero ingresado por consola
"""

def sumar_naturales(numero : int) -> int:
    if numero <= 1:
        resultado = numero
    else:
        resultado = numero + sumar_naturales(numero -1)

    return resultado

def calcular_potencia(base: int, exponente : int) ->int:
    if exponente == 0:
        resultado = 1
    else:
        resultado = base * calcular_potencia(base, exponente - 1)

    return resultado

def sumar_digitos(numero : int) -> int:
    if numero < 10:
        resultado = numero
    else:
        ultimo_digito = numero % 10
        resto_de_digitos = numero // 10
        resultado = ultimo_digito + sumar_digitos(resto_de_digitos)
    return resultado

def calcular_fibonacci(numero : int) -> int:
    if numero == 0 or numero == 1:
        resultado = numero
    else:
        resultado =calcular_fibonacci(numero -1) + calcular_fibonacci(numero - 2)

    return resultado

#print(sumar_naturales(10))
#print(calcular_potencia(2,6))
#print(sumar_digitos(172))
print(calcular_fibonacci(40))





















