"""
Modulo que contiene las funciones de entrada y validacion de datos
"""

#region inputs
def pedir_entero(mensaje: str, mensaje_error : str = "ERROR: ingrese un numero valido: ", minimo : int = False, maximo : int = False, reintentos: int = 1 ):
    numero_ingresado = int(input(mensaje))
    while (minimo != False and numero_ingresado < minimo) or (maximo != False and numero_ingresado > maximo):
        if reintentos < 0:
            numero_ingresado = None
            break
        numero_ingresado = int(input(mensaje_error))
        reintentos -= 1

    return numero_ingresado
#endregion

def validar_str_a_int(cadena : str) -> bool: #es un boleano por que estas descubriendo si puede devolver un flotante o no
    if type(cadena) == str:
        validado = True
        for caracter in cadena:
            validado_actual = False
            for caracter_valido in "0123456789":
                if caracter == caracter_valido:
                    validado_actual = True
                    break
            if not validado_actual: #Es lo mismo que validado_actual == False
                validado = False
                print(f"{caracter} fallo la validacion")
                break
    else:
        validado = False
        
    return validado

def validar_str_a_float(cadena : str) -> bool: #es un boleano por que estas descubriendo si puede devolver un flotante o no
    if type(cadena) == str:
        validado = True
        contador_punto = 0

        for caracter in cadena:
            validado_actual = False

            if caracter == ".":
                contador_punto += 1
                if contador_punto >= 2:
                    validado = False
                    break
                continue

            for caracter_valido in "0123456789":
                if caracter == caracter_valido:
                    validado_actual = True
                    break
            if not validado_actual: #Es lo mismo que validado_actual == False
                validado = False
                print(f"{caracter} fallo la validacion")
                break
    else:
        validado = False
        
    return validado

def pedir_float(mensaje: str, mensaje_error : str = "ERROR: ingrese un numero valido: ", minimo : int = False, maximo : int = False, reintentos: int = 1 ):
    numero_ingresado = float(input(mensaje))
    while (minimo != False and numero_ingresado < minimo) or (maximo != False and numero_ingresado > maximo):
        if reintentos < 0:
            numero_ingresado = None
            break
        numero_ingresado = int(input(mensaje_error))
        reintentos -= 1

    return numero_ingresado