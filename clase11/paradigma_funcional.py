lista = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

def filtrar_lista(lista : list, criterio) -> list:
    lista_filtrada = []

    for i in range(len(lista)):
        if criterio(lista[i]):
            lista_filtrada.append(lista[i])
    
    return lista_filtrada

validar_positividad = lambda a: a > 0
validar_negatividad = lambda a: a < 0
validar_paridad = lambda a: a % 2 == 0 

lista_nueva = filtrar_lista(lista, validar_positividad)
lista_negativos = filtrar_lista(lista, validar_negatividad)
lista_pares = filtrar_lista(lista, validar_paridad)

print(lista_nueva)
print(lista_negativos)
print(lista_pares)



























