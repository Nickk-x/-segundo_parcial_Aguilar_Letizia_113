def pedir_entero() -> int:
    numero_ingresado = int(input("Ingrese un numero: "))
    return numero_ingresado

def pedir_flotante() -> float:
    flotante_ingresado = float(input("Ingrese un numero: "))
    return flotante_ingresado

def pedir_cadena() -> str:
    cadena_ingresada = input("Ingrese un texto: ")
    return cadena_ingresada

def calcular_area_rectangulo(base: float , altura: float) -> float:
    area_calculada = base * altura
    return area_calculada

def calcular_area_circulo(radio : float) -> float:
    area_calculada = elevar_potencia(radio, 2) * 3.1415926535
    return area_calculada

def mostrar_paridad(numero : int) -> None:
    if verificar_paridad(numero):
        print("Es par")
    else:
        print(("No es par"))

def verificar_paridad(numero : int) -> bool:
    es_par = (numero % 2 == 0)
    return es_par

def hallar_maximo(numero_a : int, numero_b : int, numero_c : int) -> int:
    numero_maximo = numero_a

    if numero_b > numero_maximo:
        numero_maximo = numero_b
    if numero_c > numero_maximo:
        numero_maximo = numero_c
    return numero_maximo

def elevar_potencia(base : int, exponente : int) -> int:
    resultado = base ** exponente
    return resultado









