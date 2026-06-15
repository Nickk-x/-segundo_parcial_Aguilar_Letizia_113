"""
Es una funcion que se llama asi misma
"""

def funcion_recursiva(numero : int): 
    print(f"IN {numero}")
    if numero > 0:
        funcion_recursiva (numero - 1)
    print(f"OUT {numero}")

funcion_recursiva(10)

"""
Factorial de un numero

Factorial = Numero entero positivo multiplicado por todos sus menores

ejemplo:
5! = 5 x 4 x 3 x 2 x 1 / 5! = 5 x 4! = 120
4! =     4 x 3 x 2 x 1 / 4! = 4 x 3! = 24
3! =         3 x 2 x 1 / 3! = 3 x 2! = 6
2! =             2 x 1 / 2! = 2 x 1! = 2
1! =                 1 / 1! = 1      = 1

"""
def calcular_fsctorial(numero : int) -> int:

    if numero == 1:
        resultado = 1
    else:
        resultado = numero * calcular_fsctorial(numero - 1)

    return resultado

resultado_factorial = calcular_fsctorial(5)

print(resultado_factorial)

"""
Pautas para que no falle!!

1- Tiene que tener condicion de salida
2- Tiene que modificarse el valor de entrada
3- Tiene que llamarse a si misma

Internamente:
Numero primero comienza en 5, evalua si es igual a 1, no es igual a 1 asi que se le resta 1 y queda en 4
la funcion se llama y evalua si 4 es igual a 1 y no lo es asi que le resta 1, queda en 3
la funcion se llama a si misma y evalua si 3 es igual a 1, no lo es asi que le resta 1 y queda en 2
la funcion se llama a si misma, evalua si dos es igual que 1, no lo es asi que le resta 1 y queda en 1
La funcion vuelve a llamarse a si misma, evalua si 1 es igual a 1 y es correcto, no se vuelve a llamar la funcion ( se cumple con la condicion de salida) y resultado es igual a 1
------
La funcion vuelve para la atenrior funcion, 2 * 1 = 2
La funcion vuelve a la anterior funcion, 3 * 2 = 6
La funcion vuelve a la anterior funcion, 4 * 6 = 24
La funcion vuelve a la anterior funcion, 5 * 24 = 120
------
termino la funcion de recursividad
"""







