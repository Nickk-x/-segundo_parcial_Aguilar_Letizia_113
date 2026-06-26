#Facturación del Servicio de Agua Potable

#El acceso al agua potable es un servicio esencial para hogares, comercios e industrias. 
# Para garantizar un uso eficiente del recurso y establecer una estructura justa de costos, se han definido diferentes tarifas y 
# ajustes según el consumo y el tipo de cliente.
#Este sistema de facturación contempla una tarifa base que incluye un cargo fijo y un costo variable por metro cúbico consumido. 
# Además, se aplican bonificaciones y recargos dependiendo del consumo y la categoría del usuario. 
# En algunos casos especiales, también pueden otorgarse descuentos adicionales.
#A continuación, se detallan las reglas del sistema de facturación y los cálculos necesarios para determinar el monto final a pagar.

#ENTRADAS

#Tarifa base:
    #Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
    #El costo por metro cúbico (m³) de agua es de $200/m³.

consumo = int(input("Cuantos m2 consumis: "))
tipo_cliente = input("Ingrese el tipo de cliente(residencial, comercial, industrial): ")
cargo_fijo = 7000
costo_metro_cubico = 200
modificacion = 0 #En vez de tener dos variables "Bonificacion" y "Recargo", juntamos estas dos ya que no esta el caso en que puedan pasar ambas al mismo tiempo
IVA = 1.21 #asi escribimos el cargo por IVA "valor final = subtotal * IVA , valor_final_2 = subtotal * subtotal * IVA_2"
adicional_bonificacion = 0

#PROCESOS
costo_consumo = costo_metro_cubico * consumo
factura_sin_impuestos = costo_consumo + cargo_fijo 

#Cliente Residencial:
    #Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
    #Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.
match tipo_cliente:
    case "residencial":
        if factura_sin_impuestos < 35000:
            adicional_bonificacion = -.05#Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones  es menor a $35000, se aplica un descuento adicional del 5%.
        if consumo < 30:
            modificacion = -.1 #al ser una bonificacion tenemos que restarle al valor original, asi que le ponemos un -, y para evitar poner el "0" ponelos un "." directamente
        elif consumo > 80:
            modificacion = 0.15
                #Cliente Comercial:
                    #Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
                    #Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
                    #Si el consumo es menor a 50 m³, se aplica un recargo del 5%.
    case "comercial":
        if consumo > 300:
            modificacion = -0.12
        elif consumo > 150:
            modificacion = -0.08
        elif consumo < 50:
            modificacion = 0.05
                #Cliente Industrial:
                    #Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
                    #consumo.
                    #Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
                    #Si el consumo es menor a 200 m³, se aplica un recargo del 10%
    case "industrial":
        if  consumo > 1000:
            modificacion = -.3
        elif consumo > 500:
            modificacion = -.2
        elif consumo < 200:
            modificacion = .1
#Casos especiales: 
    #En todos los casos, se aplica el IVA del 21% sobre el total.
    #Requerimientos del programa:
    #Solicitar al usuario:
    #Cantidad de metros consumidos
    #Tipo de cliente, que puede ser: Residencial, Comercial o Industrial.
    #Calcular:
    #Subtotal de consumo.
    #Bonificaciones, si corresponde
    #Recargos, si corresponde
    #Subtotal, con recargos y bonificaciones.
    #IVA aplicado (21%), si corresponde.
    #Total final a pagar.
    #Mostrar en pantalla el desglose de los cálculos.


valor_modificacion = int(costo_consumo * modificacion)  #Pequeños arreglos, para que sean numeros enteros ponemos int(), aqui estan las bonificaciones y recargos resumidos es una variable

adicional_especial = int(costo_consumo * adicional_bonificacion)

subtotal = factura_sin_impuestos + valor_modificacion + adicional_especial 

total_con_iva = int(subtotal * IVA)

#SALIDAS

print(f"Tipo de cliente: {tipo_cliente}, m³ consumidos: {consumo}")

if modificacion < 0:
    print(f"Obtuvo una bonificacion del {modificacion * -100}% sobre el costo del consumo (${costo_consumo}), por un valor de ${valor_modificacion * -1}")
            #ponemos un "* -100" para transformar el decimal en un entero y ya que ya se encuentra negativo lo transforma a positivo
elif modificacion > 0:
    print(f"Obtuvo un recargo del {modificacion * 100}%, por un valor de ${valor_modificacion}")

if adicional_bonificacion  != 0:
    print(f"Obtuvo una bonificacion especial del {adicional_bonificacion * -100}% sobre el costo del consumo (${costo_consumo}), por un valor de ${adicional_especial * -1}")

print (f"El subtotal es de ${subtotal}, y tras aplicar el IVA, el total a pagar es de ${total_con_iva}") 
