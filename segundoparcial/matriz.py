def modificar_matriz(matriz : list) -> None:
    archivo_txt = matriz
    matriz_numerica = []

    for fila in archivo_txt:
        fila_de_datos = []

        for letra in fila:
            if ord(letra) >= 65 and ord(letra) <= 90:

                codigo_letra = ord(letra)

                match letra:
                    case "A":
                        dato_nuevo = 1
                    case "B":
                        dato_nuevo = 2
                    case "C":
                        dato_nuevo = 3
                    case "D":
                        dato_nuevo = 4
                    case "E":
                        dato_nuevo = 5
                    case "F":
                        dato_nuevo = 6
                    case "G":
                        dato_nuevo = 7
                    case "H":
                        dato_nuevo = 8
                    case "I":
                        dato_nuevo = 9
                    case "J":
                        dato_nuevo = 10
                    case "K":
                        dato_nuevo = 11
                    case "L":
                        dato_nuevo = 12
                    case "M":
                        dato_nuevo = 13
                    case "N":
                        dato_nuevo = 14
                    case "O":
                        dato_nuevo = 15
                    case "P":
                        dato_nuevo = 16
                    case "Q":
                        dato_nuevo = 17
                    case "R":
                        dato_nuevo = 18
                    case "S":
                        dato_nuevo = 19
                    case "T":
                        dato_nuevo = 20
                    case "U":
                        dato_nuevo = 21
                    case "V":
                        dato_nuevo = 22
                    case "W":
                        dato_nuevo = 23
                    case "X":
                        dato_nuevo = 24
                    case "Y":
                        dato_nuevo = 25
                    case "Z":
                        dato_nuevo = 26
                    case _ :
                        continue
                fila_de_datos.append(dato_nuevo)
                if len(fila_de_datos) == 3:
                    matriz_numerica.append(fila_de_datos)
                    fila_de_datos = []
                    
    return matriz_numerica

with open("segundoparcial/datos.txt", "r", encoding="UTF=8") as archivo:
    
    resultado = modificar_matriz(archivo)
print(resultado)

