"""
Alumnos:
* Corti Pedro Pablo
* Franzois Guillermo Arturo Nestor
"""
#Constantes con los precios de la yerba por tonelada
PRECIO_TONELADA_HOJA_VERDE = 36830
PRECIO_TONELADA_YERBA_CANCHADA = 139954
#Función que define el tipo de yerba
def definir_tipo_yerba():
    while True:
        try:
            tipo_yerba = int(input("Los tipos de yerba disponibles son: \n1. Yerba de hoja verde, con un precio por tonelada de $36.830\n2. Yerba Canchada, con un precio por tonelada de $139.954\nIngrese ahora su opción: "))
            if tipo_yerba == 1 or tipo_yerba == 2:
                return tipo_yerba
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("ERROR: Debe ingresar sólo números enteros entre 1 y 2.")
#Función que determina la cantidad de toneladas a comprar
def toneladas_a_comprar_fn():
    while True:
        try:
            toneladas_a_comprar = int(input("Ingrese la cantidad de toneladas que desea comprar: "))
            confirmar = input(f"Usted ha ingresado {toneladas_a_comprar} toneladas. ¿Es correcto? (S/N): ")
            if confirmar.lower() == "s":
                return toneladas_a_comprar
            elif confirmar.lower() == "n":
                continue
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("ERROR: Debe ingresar sólo números enteros para las toneladas a comprar. Intente nuevamente.")
#Función que define el primer subtotal, el del producto entre el precio del tipo de yerba y su cantidad
def definir_subtotal(cantidad_toneladas, tipo_yerba):
    if tipo_yerba == 1:
        return cantidad_toneladas * PRECIO_TONELADA_HOJA_VERDE
    elif tipo_yerba == 2:
        return cantidad_toneladas * PRECIO_TONELADA_YERBA_CANCHADA
#Función que aplica el descuento por cantidad, así como guardar el beneficio obtenido para la impresión final
def descuento_por_cantidad(subtotal, cantidad_toneladas):
    beneficio = 0
    if cantidad_toneladas >= 1 and cantidad_toneladas < 2:
        beneficio = ((subtotal * 10)/100)
    elif cantidad_toneladas >= 2 and cantidad_toneladas < 5:
        beneficio = ((subtotal * 20)/100)
    elif cantidad_toneladas >= 5:
        beneficio = ((subtotal * 35)/100)
    subtotal_con_descuento = subtotal - beneficio
    return beneficio, subtotal_con_descuento
#Función que define la forma de pago de la compra
def definir_forma_de_pago():
    opciones_validas = [1,2,3]
    while True:
        try:
            forma_de_pago = int(input("Formas de pago admitidas:\n1. Efectivo\n2. Tarjeta de crédito\n3. Pagaré\nIngrese ahora: "))
            if forma_de_pago not in opciones_validas:
                print("Forma de pago inválida, intente nuevamente.")
            else:
                return forma_de_pago
        except ValueError:
            print("ERROR: debe ingresar solo números del 1 al 3. Intente nuevamente.")
#Función que aplica descuento o recargo según la forma de pago elegida, así como guardar si es un descuento o un recargo con tipo de operación, para hacer más legible el mensaje final
def aplicar_descuento_o_recargo(subtotal, forma_de_pago):
    tipo_operacion = 1
    if forma_de_pago == 1:
        subtotal = subtotal - ((subtotal * 5)/100)
        tipo_operacion = 1
    elif forma_de_pago == 2:
        subtotal = subtotal + ((subtotal * 10)/100)
        tipo_operacion = 2
    elif forma_de_pago == 3:
        subtotal = subtotal + ((subtotal * 15)/100)
        tipo_operacion = 2
    return subtotal, tipo_operacion
#Función que define el monto del envío
def envio_fn():
    adicional_envio = 0
    envio = ""
    while True:
        opciones_validas = ["s","n"]
        envio = input("¿Desea envio? (S/N): ").lower()
        if envio not in opciones_validas:
            print("Opción inválida. Intente nuevamente.")
        elif envio == "n":
            return adicional_envio
        else:
            while True:
                try:
                    km_envio = int(input("Ingrese la cantidad de kilómetros que debe recorrer el envio: "))
                    if km_envio >= 100:
                        adicional_envio = int((km_envio / 100)) * 50000
                        return adicional_envio
                    else:
                        return adicional_envio
                except ValueError:
                    print("ERROR: Debe ingresar un número entero para los kilómetros. Intente nuevamente.")
#Función que imprime el mensaje final
def mostrar_final(tipo_yerba, cantidad_toneladas, beneficio_cantidad_comprada, subtotal_inicial, descuento_o_recargo, cantidad_descuento_o_recargo, envio, total_final):
    if tipo_yerba == 1:
        tipo_yerba_verboso = "Hoja Verde"
    else:
        tipo_yerba_verboso = "Yerba canchada"
    print(f"El final de su orden queda de la siguiente manera: \nTipo de Yerba: {tipo_yerba_verboso}.\nCantidad de toneladas compradas: {cantidad_toneladas}\nSubTotal Inicial: ${subtotal_inicial}\nDescuento obtenido por la cantidad comprada: ${beneficio_cantidad_comprada}")
    if descuento_o_recargo == 1:
        print(f"Descuento Obtenido: ${abs(cantidad_descuento_o_recargo)}")
    else:
        print(f"Recargo aplicado: ${abs(cantidad_descuento_o_recargo)}")
    print(f"Envio: ${envio}")
    print(f"Su total final es de: ${total_final}")
#Función de ejecución del resto de funciones
def ejecucion():
    tipo_yerba = definir_tipo_yerba()
    cantidad_toneladas = toneladas_a_comprar_fn()
    subtotal = definir_subtotal(cantidad_toneladas, tipo_yerba)
    beneficio, subtotal_descontado_cantidad = descuento_por_cantidad(subtotal, cantidad_toneladas)
    forma_de_pago = definir_forma_de_pago()
    subtotal_descontado_o_recargado, tipo_operacion = aplicar_descuento_o_recargo(subtotal_descontado_cantidad, forma_de_pago)
    beneficio_forma_pago = subtotal_descontado_cantidad - subtotal_descontado_o_recargado
    cantidad_envio = envio_fn()
    total_final = subtotal_descontado_o_recargado + cantidad_envio
    mostrar_final(tipo_yerba, cantidad_toneladas, beneficio, subtotal, tipo_operacion, beneficio_forma_pago, cantidad_envio, total_final)

#Llamada de la función de ejecución
ejecucion()