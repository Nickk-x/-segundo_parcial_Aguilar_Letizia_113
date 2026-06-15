import entradas

from entradas import pedir_entero

from entradas import * #Esto es para importar todo

import entradas as I #Voy a usar esta

edad_ingresada = entradas.pedir_entero("Ingrese su edad: ")

edad_ingresada_2 = pedir_entero("Ingrese su edad otra vez: ")

edad_ingresada = I.pedir_entero("Ingrese su edad por tercera vez: ")