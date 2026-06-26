

variable = "hola"

print(type(variable))

variable = 1.0

print(type(variable))

#    H O L A
#    0 1 2 3

for letra in "Hola":
    print(letra)


def validar_str_a_float(cadena : str) -> bool: #es un boleano por que estas descubriendo si puede devolver un flotante o no
    for caracter in cadena:
        print(caracter)

    return False

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

cadena_a_transformar = "1.16.4"
cadena_a_transformar_int = "127.3"
print(validar_str_a_int(cadena_a_transformar_int))


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

cadena_a_transformar_float = "1273"
print(validar_str_a_float(cadena_a_transformar_float))

print(ord("a"))


cadena_con_mayus = "Hola Mundo"

def transformar_lower(cadena : str) -> str:
    cadena_final = ""
    for caracter in cadena:
        indice_caracter = ord(caracter)
        if indice_caracter >= 65 and indice_caracter <= 90:
            indice_caracter += 32
        nuevo_caracter = chr(indice_caracter)
        cadena_final += nuevo_caracter

    return cadena_final

print(transformar_lower(cadena_con_mayus))

def transformar_upper(cadena : str) -> str:
    cadena_final = ""
    for caracter in cadena:
        indice_caracter = ord(caracter)
        if indice_caracter >= 97 and indice_caracter <= 122:
            indice_caracter -= 32
        nuevo_caracter = chr(indice_caracter)
        cadena_final += nuevo_caracter

    return cadena_final

print(transformar_upper(cadena_con_mayus))

"""
caracter = "a"

numero_caracter = ord(caracter)
if numero_caracter >= 65 and numero_caracter <= 90: 
    numero_caracter += 32

nuevo_caracter = chr(numero_caracter)

print(nuevo_caracter)
"""








