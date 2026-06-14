"""
📌 Desafío: Encuesta Tecnológica en UTN Technologies
UTN Technologies, una reconocida software factory, está en la búsqueda de ideas para su próximo desarrollo en 
Python, con el objetivo de revolucionar el mercado.
Las tecnologías en evaluación son:
 🔹 Inteligencia Artificial (IA)
 🔹 Realidad Virtual/Aumentada (RV/RA)
 🔹 Internet de las Cosas (IOT)
Para tomar una decisión informada, la empresa ha lanzado una encuesta entre sus empleados con el propósito 
de analizar ciertas métricas.
El sistema deberá permitir ingresar los datos de 10 empleados mediante la terminal.

🔹 Requisitos del Programa
 ✔️ Los datos deben solicitarse y validarse correctamente.✔️
 ✔️ Utilizar variables adecuadas para almacenar la información y facilitar su análisis.
 ✔️ Presentar los resultados de manera clara y organizada.

"""
#ENTRADA
"""
Cada empleado encuestado deberá proporcionar la siguiente información:
 ✔️ Nombre
 ✔️ Edad (debe ser 18 años o más)
 ✔️ Género (Masculino, Femenino, Otro)
 ✔️ Tecnología elegida (IA, RV/RA, IOT)
"""
cantidad_maxima = 10
contador_casouno = 0
contador_casodos = 0
edad_mayor = 0
tecnologia_elegida_por_mayor = ""
nombre_maculino_mayor = ""
cantidad_maxima = 2
for i in range(cantidad_maxima):

    nombre_ingresado = input("Ingrese su nombre: ")
    
    bandera_edad = True
    while bandera_edad == True:
        edad_ingresada = int(input("Ingrese su edad (debe ser 18 años o más): "))
        if edad_ingresada < 18 or edad_ingresada > 90:
            print("ERROR:No puedes tener menos de 18 años o mas de 90 años, reintente.")
            
        else:
            bandera_edad = False

    genero_ingresado = input("Ingrese su genero (Masculino, Femenino, Otro): ")
    while genero_ingresado != "Masculino" and genero_ingresado != "Femenino" and genero_ingresado != "Otro":
        genero_ingresado = input("ERROR: Tiene que ser una de estas tres opciones (Masculino, Femenino, Otro): ")
    tecnologia_elegida = input("Ingrese la tecnologia que eligio (IA, RV/RA, IOT): ")
    while tecnologia_elegida != "IA" and tecnologia_elegida != "RV/RA" and tecnologia_elegida != "IOT":
        genero_ingresado = input("ERROR: Tiene que ser una de estas tres opciones (IA, RV/RA, IOT): ")
    

    #PROCESOS
    """
    El sistema deberá permitir ingresar los datos de 10 empleados mediante la terminal.
    🔹 Análisis de Datos
    A partir de las respuestas, se deben calcular las siguientes métricas:

    1️⃣ Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años 
    (inclusive).

    2️⃣ Porcentaje de empleados que NO votaron por IA, siempre y cuando:
    Su género no sea Femenino 
    Su edad está entre los 33 y 40 años.

    3️⃣ Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó.

    """

    if genero_ingresado == "Masculino":
        if edad_ingresada >= 25 and edad_ingresada <= 50 and (tecnologia_elegida == "IOT" or tecnologia_elegida == "IA"):
            contador_casouno += 1

        if edad_mayor < edad_ingresada :
            edad_mayor = edad_ingresada
            nombre_maculino_mayor = nombre_ingresado
            tecnologia_elegida_por_mayor = tecnologia_elegida
    if genero_ingresado != "Femenino" and tecnologia_elegida != "IA" and edad_ingresada >= 33 and edad_ingresada <= 40:
        contador_casodos += 1

porcentaje_caso_dos = (contador_casodos * 100) / cantidad_maxima

print(f"La cantidad de empleados de genero masculino que votaron por IOT o IA uya edad esté entre 25 y 50 años es de {contador_casouno}")

print(f"El porcentaje de empleados que NO votaron por IA, que su género no sea Femenino y su edad está entre los 33 y 40 años es {porcentaje_caso_dos}%.")

print(f"El empleado masculino de mayor edad es {nombre_maculino_mayor}, eligio de tecnologia {tecnologia_elegida_por_mayor} y tiene {edad_mayor}")









