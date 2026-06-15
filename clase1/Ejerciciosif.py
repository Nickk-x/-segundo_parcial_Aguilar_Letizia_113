#IF - ELSE -ELIF

#ENTRADAS
#A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
#Menos de 160 cm: Base
#Entre 160 cm y 179 cm: Escolta
#Entre 180 cm y 199 cm: Alero
#200 cm o más: Ala-Pívot o Pívot
altura = int(input("Ingrese la altura del jugador: "))
nota = int(input("Ingrese su nota: "))
posicion = "No tienes una"
calificacion = "Indeterminada"

#PROCESOS
if nota >= 1 and nota <=10:
    if nota <= 3:
        calificacion = "Desaprobado"
    elif nota <= 5:
        calificacion = "Aprobado"
    else:
        calificacion = "Promocion directa" 

    print(f"Tu calificacion es {calificacion}")
    print(f"la nota es: {nota}")

    if calificacion == "Aprobado" or calificacion == "Promocion directa":
        if altura < 160:
            posicion = "Base"
        elif altura >= 160 and altura <= 179:
            posicion = "Escolta"
        elif altura >= 180 and altura <= 199:
            posicion = "Alero"
        else:
            posicion = "Ala-Pivot"
        print(f"tu posicion es: {posicion}")
    else:
        print("Buena suerte para la proxima <3")

else: #El else no tiene que tener una condicion al lado
    print("Nota invalida, debe estar entre el 1 y el 10!!")
#> izquierda es mayor que derecha
#< izquierda es menor que la derecha

#SALIDAS