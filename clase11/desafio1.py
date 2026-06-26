import inputs as I

"""
Menu de Opciones con Listas y Funciones
Desarrollar un programa en Python que presente un menu de opciones donde el usuario pueda realizar distintas operaciones con un conjunto de numeros

Opciones del Menu:
xIngresar datos: Permitir al usuario ingresar 10 numeros enteros en el rango de -1000 a 1000.
xCantidad de positivos y negativos : Mostrar cuantos numeros ingresados son positivos y cuantos son negativos.
xSuma de los numeros pares: Calcular y mostrar la sumatoria de los numeros pares.
-Mayor numero impar: Identificar y mostrar el mayor numero impar ingresado.
xListar los numeros ingresados: Mostrar todos los numeros en el orden en que fueron ingresados.
xListar los numeros pares: Mostrar unicamente los numeros pares de la lista
-Listar los numeros en posiciones impares: Mostrar los numeros que se encuentran en posiciones impares dentro de la lista.
xSalir del programa.

Condiciones:
    >El usuario debe ingresar los numeros antes de acceder a las opciones 2 a 7.
    >El programa debe estar estructurado en funciones, siguiendo el paradigma de programacion funcional:

    Funciones especificas: Para operaciones como determinar si un numero es positivo, negativo o par.
    Funciones generales: Para listar elementos o calcular sumatorias.

Estructura del Codigo:
    El programa debe estar organizadp en modulos:
    Especificas.py:Contendra las funciones especificas.
    Array_Generales.py: Contendra las funciones generales.
Las funciones de entrada de datos deben importarse desde el modulo.

Consejo: desarrollar y probar primero cada funcion individualmente antes de organizarlas en modulos.
"""

lista_numeros = [0] * 10 # = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def cargar_lista(lista : list, min : int, max : int) -> list:
    for i in range(len(lista)):
        lista[i] = I.pedir_entero(f"Ingrese un valor para el indice {i}: ", "ERROR, reingrese el valor: ", min, max)
    
    return lista

def mostrar_lista(lista : list) -> None:
    for i in range(len(lista)):
        print(f"{i} -> {lista[i]}")

def sumatoria_pares(lista : list) -> int:
    acumulador = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            acumulador += lista[i]
    return acumulador

def sumar_lista(lista : list) -> list:
    acumulador = 0

    for i in range(len(lista)):
        acumulador += lista[i]
    
    return acumulador

def filtrar_lista_paridad(lista : list, par : int = True) -> list:
    lista_filtrada = []

    for i in range(len(lista)):
        if par:
            if lista[i] % 2 == 0:
                lista_filtrada.append(lista[i])
        else:
            if lista[i] % 2 != 0:
                lista_filtrada.append(lista[i])
    return lista_filtrada

def contar_positividad(lista : list) -> None:
    contador_positivos = 0
    contador_negativos = 0

    for i in range(len(lista)):
        if lista[i] < 0:
            contador_negativos += 1
        elif lista[i] > 0:
            contador_positivos += 1
    
    print(f"Negativos: {contador_negativos}")
    print(f"Positivos: {contador_positivos}")

def buscar_mayor(lista : list) -> int:
    mayor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]

    return mayor

def mostrar_lista_pos_impar(lista : list, m_end = '\n') -> None:
    for i in range(len(lista)):
        if i % 2 != 0:
            print(f"{i} -> {lista[i]}", end = m_end)
    print()

bandera_lista_ingresada = False

while True:
    opcion_seleccionada = I.pedir_entero('''[1] Ingresar datos.
[2] Cantidad de positivos y negativos.
[3] Suma de los numeros pares.
[4] Mayor numero impar.
[5] Listar los numeros ingresados.
[6] Listar los numeros pares.
[7] Listar los numeros en posiciones impares.
[8] Salir del programa
''', '''ERROR, Ingrese una opcion valida:
[1] Ingresar datos.
[2] Cantidad de positivos y negativos.
[3] Suma de los numeros pares.
[4] Mayor numero impar.
[5] Listar los numeros ingresados.
[6] Listar los numeros pares.
[7] Listar los numeros en posiciones impares.
[8] Salir del programa.
''', 1, 8)

    if opcion_seleccionada != 8 and (opcion_seleccionada != 1 and bandera_lista_ingresada == False):
        print("Primero se debe cargar la lista")
        continue
    
    match opcion_seleccionada:
        case 1:
            lista_numeros = cargar_lista(lista_numeros, -1000, 1000)
            print(lista_numeros)
            bandera_lista_ingresada = True
        case 2:
            contar_positividad(lista_numeros)
        case 3:
            lista_pares = filtrar_lista_paridad(lista_numeros)
            resultado_sumatoria_par = sumar_lista(lista_pares)
            print(f"{resultado_sumatoria_par}")
        case 4:
            lista_impares = filtrar_lista_paridad(lista_numeros, False)
            mayor_impar = buscar_mayor(lista_impares)
            print(mayor_impar)
        case 5:
            mostrar_lista(lista_numeros)
        case 6:
            lista_pares = filtrar_lista_paridad(lista_numeros)
            mostrar_lista(lista_pares)
        case 7:
            mostrar_lista_pos_impar(lista_numeros)
        case 8:
            print("Saliendo del menu..")
            break


















