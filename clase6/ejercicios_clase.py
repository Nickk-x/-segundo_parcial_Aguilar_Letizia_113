"""
El nombre de la funcion idealmente tiene que ser un verbo, este siempre termina en ar, er, ir
en el parentesis vamos a meter los parametros

"""
"""
Cohesion y Acoplamiento:

Cohesion: Implica una conexion o union que asegura que las partes de un todo
esten bien integradas y funcionen juntas de manera efectiva.

Acoplamiento: Es la dependencia que tienen las funciones entre si.

                    /\
                    |a
                    |c
                    |o
                    |p
Alto Acomplamiento  |l Alto Acomplamiento
Baja cohesion       |a Alta cohesion
                    |m
                    |i
                    |e
                    |n
                    |t
____________________|o____________________ \
                    |    cohesion          /
                    |
                    |
Bajo Acoplamiento   | Bajo Acoplamiento
Baja cohesion       | Alto cohesion
                    |
                    \/

"""

def saludar(): #ar er ir
    """
    # Tipos de estilos de letras

    Hola!!
    # Hola!!
    ## Hola!!
    # # Hola!!
        # Hola!!
    - Hola!!

    . Hola!!
    """


    print("Hola!♥")

#Parametros, es una variable pero en contexto de una funcion
                    #Los parametros deben ir ordenados, no rompera pero no lo tomara en cuenta
def saludar_alumno(alumno : str, turno : str = "Mañana", nota : int = 4):

    """
    #¿Que hace?
        Saluda a un alumno en base a su turno y calificacion.
    #¿Que recibe?
        - alumno (str): Nombre del alumno que sera saludado.
        - turno (str = "Mañana): Turno del alumno en cuestion.
        - nota (int = 4):"Nota del alumno en cuestion.
    #¿Que retorna?
    """
    if nota > 6:
        agregado = "Felicidades, promocionaste!! "
    elif nota >= 4:
        agregado = "Aprobaste, pero aun se puede promocionar!!"
    else:
        agregado = "Hay que meterle un poquito mas al estudio "
    match turno:
        case "Mañana":
            print(f"Hola {alumno}!👋\n{agregado}")
        case "Tarde":
            print(f"Hola {alumno}!🧉\n{agregado}")
        case "Noche":
            print(f"Hola {alumno}!😴\n{agregado}")

print("Hola perriños y gatiños, como andan?", end = "|")
print("No baje de linea perros")

                #El orden que se escriba el de aca debe ser el mismo que arriba
saludar_alumno("Mani", "Tarde",8)
print() #esto hace un espacio entre los dos impresiones
saludar_alumno("rayo", "Noche",3)
print()
saludar_alumno("loloc", "Mañana") #Cuando no hay tercera opcion esto puede romper, asi que se puede poner un por defecto cuando un dato falte, en este caso sera 4
print()
saludar_alumno("Rocket")#Aqui le ponemos por defecto Mañana y 4 de nota

def sumar(numero_a : int, numero_b : int):
    """
    # ¿Que hace?
        Suma dos numeros
    # ¿Que recibe?
        - numero_a (int): Primer numero a sumar
        - numero_b (int): Segundo numero a sumar
    # ¿Que retorna? 
        int: Suma entre numero_a y numero_b
    """

    resultado = numero_a + numero_b
    return resultado #Sin un print no imprime nada

#Puedo imprimir de estas formas
print(sumar(5, 8))
resultado_suma = sumar(5,8)
print(resultado_suma)

resultado_suma_dos = 0

for i in range(10):
    resultado_suma_dos  = sumar(resultado_suma_dos, i)
    print(resultado_suma_dos)


def obtener_promedio(numero_a : int, numero_b : int) -> float:
    suma = sumar(numero_a , numero_b)
    promedio = suma / 2
    return promedio

nota_primer_parcial = 2 
nota_segundo_parcial = 4

promedio_notas = obtener_promedio(nota_primer_parcial, nota_segundo_parcial)

saludar_alumno("Tayson", "Mañana", promedio_notas)

def verificar_primo(numero : int) -> bool:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    return (es_primo and numero > 1)

numero_ingresado = int(input("Ingrese un numero: "))
contador_primos = 0
for i in range(numero_ingresado + 1):
    primo_verificado = verificar_primo(i)

    if primo_verificado:
        print(f"{i} es primo.")
        contador_primos += 1
    else:
        print(f"{i} no es primo.")
print(f"Se hallaron {contador_primos} primos")




"""
Objetivos de una funcion:
Minificacion: Logramos que el programa sea mas simple de comprender ya que cada
funcion se dedica a realizar una tarea en particular. 

Depuracion: La depuracion queda acotada a cada funcion

Modificacion: Las modificaciones al programa se reducen a cada modulo.

Reutilizacion: Cuando cada funcion esta bien probada, se la puede usar las veces
que se quiera y asi reutilizar codigo.

Independencia: Se obtiene una autonomia del codigo donde cada funcion es 
independiente de otra.

Ejercicios clase:
"""
def pedir_entero(mensaje: str, mensaje_error : str = "ERROR: ingrese un numero valido: ", minimo : int = False, maximo : int = False, reintentos: int = 1 ):
    numero_ingresado = int(input(mensaje))

    while (minimo != False and numero_ingresado < minimo) or (maximo != False and numero_ingresado > maximo):
        if reintentos < 0:
            numero_ingresado = None
            break
        numero_ingresado = int(input(mensaje_error))
        reintentos -= 1

    return numero_ingresado

numero_ingresado = pedir_entero("Ingrese CUALQUIER numero: ")
edad_ingresada = pedir_entero("Ingrese su edad: ")
print(edad_ingresada)
altura_ingresada = pedir_entero("Ingrese su altura en centimetros: ", "ERROR: No puedes medir negativo, reingrese su altura: ", 1)



































