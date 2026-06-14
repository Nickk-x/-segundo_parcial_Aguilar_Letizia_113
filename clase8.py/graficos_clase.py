def grafico_tres_columnas(valor_a : int, valor_b : int, valor_c : int, caracter_a : str = "\033[31m♥♥\033[0m", caracter_b : str = "\033[32m♥♥\033[0m", caracter_c : str = "\033[34m♥♥\033[0m"):

    mensaje_final = ""

    valor_maximo = valor_a
    if valor_b > valor_maximo:
        valor_maximo = valor_b
    if valor_c > valor_maximo:
        valor_maximo = valor_c

    for i in range(valor_maximo, 0, -1):
        linea_actual = ""

        if valor_a >= i:
            linea_actual += f"{caracter_a} "
        else:
            linea_actual += "   "
        
        if valor_b >= i:
            linea_actual += f"{caracter_b} "
        else:
            linea_actual += "   "

        if valor_c >= i:
            linea_actual += caracter_c
        linea_actual += "\n"
        
        mensaje_final += linea_actual 

    return mensaje_final


print(grafico_tres_columnas(10, 2, 7))

"""
cr = "\033[31m♥♥\033[0m"
cv = "\033[32m♥♥\033[0m"
ca = "\033[34m♥♥\033[0m"
"""
