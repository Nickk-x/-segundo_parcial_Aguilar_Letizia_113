"""
FUNCIONES
"""
#region 1 Crear una función que le solicite al usuario el ingreso de un número entero
# y lo retorne.

def numero_entero() -> int:
    
    numero_ingresado = int(input("Ingrese un numero entero: "))
    
    return numero_ingresado

numero_entero_verificado = numero_entero()

print(f"El numero ingresado es {numero_entero_verificado}")

#endregion

#region 2 Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
def numero_float() -> float:
    
    numero_ingresado = float(input("Ingrese un numero flotante: "))
    
    return numero_ingresado

numero_float_verificado = numero_float()

print(f"El numero ingresado es {numero_float_verificado}")
#endregion

#region 3 Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 
def pedir_cadena() -> str:
    
    cadena_ingresada = input("Ingrese una cadena: ")
    
    return cadena_ingresada

cadena = pedir_cadena()

print(f"Ingresaste {cadena}")
#endregion

#region 4 Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 
def area_rectangulo(altura: int, base : int) -> int:
    rectangulo_area = altura * base
    return rectangulo_area

print(area_rectangulo(5,8))
print(area_rectangulo(3,10))
#endregion

#region 5 Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

def area_circulo(radio: int, pi : int = 3.1416) -> int:
    circulo_area = pi * (radio ** 2)
    return circulo_area

resultado = area_circulo(4)

print(f"El area del circulo es {resultado:.2f}")
#endregion


#region 6 Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
def par_o_impar(numero : int) -> str:
    if numero % 2 == 0:
        resultado = f"El numero {numero} es par"
    else:
        resultado = f"El numero {numero} es impar"
    return resultado

print(par_o_impar(3))
#endregion

#region 7 Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

def verificar_par_impar(numero : int) -> bool:
    if numero % 2 == 0:
        bandera = True
    else:
        bandera = False
    return bandera

resultado = verificar_par_impar(3)

print(f"Es par = {resultado}")
#endregion

#region 8 Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

def buscar_el_numero_mayor(numero_1 : int, numero_2 : int, numero_3: int)->int:
    numero_mayor = numero_1
    if numero_2 > numero_mayor:
        numero_mayor = numero_2
    if numero_3 > numero_mayor:
        numero_mayor = numero_3
    return numero_mayor

numero_ingresado_1 = int(input("Ingrese el primer numero: "))
numero_ingresado_2 = int(input("Ingrese el segundo numero: "))
numero_ingresado_3 = int(input("Ingrese el tercer numero: "))

resultado = buscar_el_numero_mayor(numero_ingresado_1, numero_ingresado_2, numero_ingresado_3)
print(f"El numero mayor es {resultado}")


#region 9 Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

def buscar_potencia(base : int, exponente : int): 
    numero_potenciado = base ** exponente
    return numero_potenciado

base_ingresada = int(input("Ingrese la base a potenciar: "))
exponente_ingresado = int(input("Ingrese el exponente: "))

resultado = buscar_potencia(base_ingresada, exponente_ingresado)

print(f"El numero {base_ingresada} elevado a la {exponente_ingresado} es: {resultado}")

#endregion

#region 10 Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.
def buscar_primo(numero : int ) -> int:
    contador_divisores = 0
    for i in range(1 , numero + 1):
        if numero % i == 0:
            contador_divisores +=1
        else: 
            continue
    if contador_divisores == 2:
        mensaje = True
    else:
        mensaje = False
    return mensaje

numero_ingresado = int(input("Ingrese un numero: "))

resultado = buscar_primo(numero_ingresado)

print(f"{resultado}")

#endregion


#region 11 Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre
# la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.

#¿Qué es modularizar?
#Modularizar es como jugar con Legos. En lugar de meter toda la lógica gigante adentro de una sola función, creas piezas pequeñas.
#Como ya sabemos cómo saber si un solo número es primo, podemos usar esa función como una "pieza" dentro de la nueva función que busca en la lista.

def encontrar_primo(numero :int) -> bool:
    if numero < 2:
        return False
    
    bandera_primo = True
    
    for i in range(2, numero ):
        if numero % i == 0:
            bandera_primo = False
            break
    return bandera_primo

def contar_primos (numero_limite : int) -> int:
    contador_primos = 0
    for i in range(numero_limite, 0, -1):
        if encontrar_primo(i):
            print(f"{i} es primo")
            contador_primos += 1
        else:
            print(f"{i} no es primo")
    return contador_primos

numero_ingresado = int(input("Ingrese un numero: "))

resultado = contar_primos(numero_ingresado)
print("_________________________________________")
print(f"Se encontraron {resultado} numeros primos.")
#endregion


#region 12 Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. 
# La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.
def multiplicar_numero(numero : int, numero_inicio : int = 1, numero_final : int = 10) -> int:
    for i in range(numero_inicio, numero_final +1):
        resultado = i * numero
        print(f"{numero} x {i} = {resultado}")

numero_ingresado = int(input("Ingrese el numero a multiplicar: "))

multiplicar_numero(numero_ingresado)
#endregion

#region 13 Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.

#region 1 Crear una función que le solicite al usuario el ingreso de un número entero
# y lo retorne.
print(ord(" "))

def validar_numero_entero(numero: str , mensaje_error : str ="ERROR: Tienes que ingresar solo numeros, intenta nuevamente: ") -> int:
    bandera_verificar = True
    numero_a_verificar = numero
    while bandera_verificar == True:
        bandera_int = True

        for i in numero_a_verificar:

            if ord(i) >= 48 and ord(i) <= 57:
                continue
            elif ord(i) == 32:
                bandera_int = False
                break
            else: 
                bandera_int = False
                break

        if bandera_int == True and numero_a_verificar != "":
            numero_verificado = int(numero_a_verificar)
            bandera_verificar = False
        else: 
            numero_a_verificar = input(mensaje_error)

    return numero_verificado

numero_ingresado = input("Ingrese su edad: ")

numero_entero_verificado = validar_numero_entero(numero_ingresado)

print(f"Tu edad es {numero_entero_verificado}")

codigo_ingresado = input("Ingrese un codigo postal: ")
codigo_valido = validar_numero_entero(codigo_ingresado, "ERROR: no es un codigo postal, ingrese solo numeros, intentelo nuevamente: ")

print(f"Tu codigo postal es {codigo_valido}")
#endregion

#region 2 Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
def validar_numero_flotante(numero: str , mensaje_error : str ="ERROR: Tienes que ingresar solo numeros decimales, intenta nuevamente: ") -> float:
    bandera_verificar = True
    numero_a_verificar = numero

    while bandera_verificar == True:
        bandera_float = True
        contador_punto = 0
        for i in numero_a_verificar:

            if ord(i) == 46:
                contador_punto += 1
                if contador_punto > 1:
                    bandera_float = False
                    break
                else:
                    continue

            if ord(i) >= 48 and ord(i) <= 57:
                continue
            elif ord(i) == 32:
                bandera_float = False
                break
            else: 
                bandera_float = False
                break

        if bandera_float == True and numero_a_verificar != "" and contador_punto == 1:
            numero_verificado = float(numero_a_verificar)
            bandera_verificar = False
        else: 
            numero_a_verificar = input(mensaje_error)

    return numero_verificado

numero_ingresado = input("Ingrese su peso: ")

numero_float_verificado = validar_numero_flotante(numero_ingresado)

print(f"Tu peso es {numero_float_verificado}")

#endregion


#region 3 Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 
def validar_cadena(cadena : str, mensaje_error : str = "ERROR: Solo puede ingresar letras, intente nuevamente: ") -> str:
    bandera_reinicio = True
    cadena_evaluada = cadena

    while bandera_reinicio == True:
        bandera_str = True
        cadena_ordenada = ""

        for i in cadena_evaluada:
            codigo_ascii = ord(i)

            if codigo_ascii >= 65 and codigo_ascii <= 90:
                codigo_minuscula = codigo_ascii + 32
                letra_minuscula = chr(codigo_minuscula)
                cadena_ordenada += letra_minuscula
                continue
            elif codigo_ascii >= 97 and codigo_ascii <= 122:
                cadena_ordenada += i
                continue
            elif ord(i) == 32:
                bandera_str = False
                break
            else: 
                bandera_str = False
                break
                
        if bandera_str == True and cadena_evaluada != "":
            cadena_verificada = cadena_ordenada

            bandera_reinicio = False
        else:
            cadena_evaluada = input(mensaje_error)
    return cadena_verificada

cadena_ingresada = input("Ingrese una cadena de texto: ")
cadena = validar_cadena(cadena_ingresada)

print(f"Ingresaste {cadena}")
#endregion
#endregion


















