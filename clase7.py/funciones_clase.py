"""
promedio mas saludar alumno
"""
#region
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

def pedir_entero(mensaje: str, mensaje_error : str = "ERROR: ingrese un numero valido: ", minimo : int = False, maximo : int = False, reintentos: int = 1 ):
    numero_ingresado = int(input(mensaje))

    while (minimo != False and numero_ingresado < minimo) or (maximo != False and numero_ingresado > maximo):
        if reintentos < 0:
            numero_ingresado = None
            break
        numero_ingresado = int(input(mensaje_error))
        reintentos -= 1

    return numero_ingresado

def obtener_promedio(numero_a : int, numero_b : int, numero_c : int) -> float:
    resultado_suma = numero_a + numero_b + numero_c
    promedio = resultado_suma / 3
    return promedio

nombre_alumno = input("Ingrese el nombre del alumno: ")


nota_primer_trimestre = pedir_entero("Ingrese la nota del primer trimestre: ", "ERROR: la nota solo puede ir del 1 al 10: ", 1, 10, 3)
nota_segundo_trimestre = pedir_entero("Ingrese la nota del primer trimestre: ", "ERROR: la nota solo puede ir del 1 al 10: ", 1, 10, 3)
nota_tercer_trimestre = pedir_entero("Ingrese la nota del primer trimestre: ", "ERROR: la nota solo puede ir del 1 al 10: ", 1, 10, 3)

promedio_anual = obtener_promedio(nota_primer_trimestre, nota_segundo_trimestre, nota_tercer_trimestre)

saludar_alumno(nombre_alumno, nota = promedio_anual)

#endregion

"""
Para buscar numeros random puedes usar: 
"""
import random

print(random.randint(0, 10))















