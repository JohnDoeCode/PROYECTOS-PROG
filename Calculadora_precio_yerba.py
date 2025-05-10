"""Consigna:Programa que calcule el precio a pagar según la cantidad y 
tipo de toneladas de yerba mate a comprar (toneladas ingresadas por teclado).

Tener cuenta los siguientes descuentos:
más de 1 tonelada: 10% dto
más de 2 toneladas: 20% dto
más de 5 toneladas: 35% dto ✅ 

El precio base de la tonelada es:
$ 36.830 para la tonelada de hoja verde (tipo: 1) y $139.954 para la tonelada de 
yerba mate canchada (tipo: 2) ✅ 

Además, debe ingresar la forma de pago por teclado, la cual si es en efectivo (1) 
recibe un 5% de descuento adicional y si es por tarjeta de crédito se aplica un
10% de recargo y pagaré un 15% de recargo. ✅ 

Formas de pago admitidas (no admitir otro tipo):
1: efectivo
2: tarjeta de crédito
3: pagaré ✅ 

Si además el comprador retira el producto no hay recargo pero si prefiere el envío 
deberá abonar un adicional de $ 50.000 por cada 100KM, con lo cual el comprador 
debe indicar a cuantos km se encuentra desde el punto de venta.

Mostrar un mensaje que indique el producto, total a comprar, el beneficio/ obtenido 
por la cantidad comprada, mostrar el subtotal a pagar, por separado mostrar la bonificación
ó recargo aplicado según forma de pago, y el importe total, forma de pago elegida, y mostrar 
el recargo si prefiere el envío. Al finalizar la transacción debe mostrar por pantalla todos 
los componentes que aplica al pago y el total obviamente (bien formateado como $).

Controlar bien de no admitir valores incorrectos de tipo forma de pago y de tipo de yerba, en
todo caso mostrar por pantalla cuales son los admitidos."""
#Constantes con los precios de la yerba por tonelada
PRECIO_TONELADA_HOJA_VERDE = 36830
PRECIO_TONELADA_YERBA_CANCHADA = 139954

def envio_fn():
    adicional_envio = 0
    while envio != "s":
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
                        print(adicional_envio)
                        return adicional_envio
                    else:
                        print(adicional_envio)
                        return adicional_envio
                except ValueError:
                    print("ERROR: Debe ingresar un número entero para los kilómetros. Intente nuevamente.")

def descuento_por_cantidad(subtotal, cantidad_comprar_toneladas):
    if cantidad_comprar_toneladas >= 1 and cantidad_comprar_toneladas < 2:
        subtotal = subtotal - ((subtotal * 10)/100)
    elif cantidad_comprar_toneladas >= 2 and cantidad_comprar_toneladas < 5:
        subtotal = subtotal - ((subtotal * 20)/100)
    elif cantidad_comprar_toneladas >= 5:
        subtotal = subtotal - ((subtotal * 30)/100)
    return subtotal

def forma_de_pago_fn():
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

def aplicar_descuento_o_recargo(subtotal, forma_de_pago):
    if forma_de_pago == 1:
        subtotal = subtotal - ((subtotal * 5)/100)
        return subtotal
    elif forma_de_pago == 2:
        subtotal = subtotal + ((subtotal * 10)/100)
    elif forma_de_pago == 3:
        subtotal = subtotal + ((subtotal * 15)/100)


envio_fn()