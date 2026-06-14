#Match

#ENTRADAS
#Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 

estacion = input("Ingrese la estacion del año en la que viaja (invierno, verano, otoño, primavera): ")
destino = input("Ingrese el destino del viaje (Bariloche, Mar del plata y cataratas): ")

#PROCESOS
#Si es invierno: solo se viaja a Bariloche.
#Si es verano: se viaja a Mar del plata y Cataratas.
#Si es otoño: se viaja a todos los lugares.
#Si es primavera: se viaja a todos los lugares menos Bariloche.

match estacion:
    case "invierno":
        match destino:
            case "bariloche":
                print(f"Se viaja a {destino}")
            case _:
                print("No se viaja")
    case "verano":
        match destino:
            case "mar del plata":
                print(f"Se viaja a {destino}")
            case "cataratas":
                print(f"Se viaja a {destino}")
            case _:
                print("No se viaja")
    case "otoño":
        print(f"Se viaja a {destino}")
    case "primavera":
        match destino:
            case "bariloche":
                print("No se viaja")
            case "mar del plata":
                print(f"Se viaja a {destino}")
            case "cataratas":
                print(f"Se viaja a {destino}")
    case _:
        print("Estacion no valida")


#SALIDAS


#En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
