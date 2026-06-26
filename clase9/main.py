import inputs

from inputs import pedir_entero

from inputs import * #Esto es para importar todo

import inputs as I #Voy a usar esta

edad_ingresada = inputs.pedir_entero("Ingrese su edad: ")

edad_ingresada_2 = pedir_entero("Ingrese su edad otra vez: ")

edad_ingresada = I.pedir_entero("Ingrese su edad por tercera vez: ")