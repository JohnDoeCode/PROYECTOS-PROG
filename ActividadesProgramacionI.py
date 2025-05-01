"""#Primera actividad (9-4-25)
#1.Solicitar al usuario el ingreso por teclado un número, que indicará la cantidad de personas que serán agregadas a una lista.
CantPersonas = int(input("Ingrese el número de personas que desea añadir a la lista: "))
ListaPersonas = []
#2. Luego, en esa cantidad ingresada, pedir el ingreso por teclado de los nombres de personas.
for i in range(CantPersonas):
    PersonaAniadir = input("Ingrese el nombre de la persona a añadir: ")
    ListaPersonas.append(PersonaAniadir)
#3. Al finalizar, mostrar por pantalla los datos ingresados, uno debajo del otro.
for persona in ListaPersonas:
    print(persona)
#4. Luego, solicitar un nombre por teclado (de los que han sido agregados a la lista) y eliminarlo de la misma (por valor).
while True:
    NombreEliminar = input("Ingrese un nombre a eliminar de la lista: ")
    if NombreEliminar in ListaPersonas:
        ListaPersonas.remove(NombreEliminar)
        break
    else:
        print(f"El nombre {NombreEliminar} no ha sido encontrado. Intente nuevamente.")
#5. Volver a mostrar por pantalla los nombres.
for persona in ListaPersonas:
    print(persona) 
#6.Luego, solicitar un número por teclado (mayor a 0 y menor a la cantidad de elementos de la lista) y eliminar el elemento de la lista que coincide con ese índice.
while True:
    IndiceEliminar = int(input("Ingrese el índice del nombre a eliminar: "))
    if IndiceEliminar >= 0 and IndiceEliminar < len(ListaPersonas):
        ListaPersonas.pop(IndiceEliminar)
        break
    else:
        print(f"El número {IndiceEliminar} no es válido, intente nuevamente.")
#7. Volver a mostrar por pantalla los nombres.
for persona in ListaPersonas:
    print(persona)
    
#FIN PRIMERA ACTIVIDAD"""

#2da Actividad, parte 1: (15-4-25)
"""ACTIVIDAD: Estructuras de Control Repetitivas
Enunciado: programando un simulador de cajero automático. El sistema debe:
Comenzar con un saldo inicial ficticio (por ejemplo, $10,000).
Mostrar un menú de opciones en bucle:

=== Cajero Automático ===
1. Consultar saldo
2. Depositar dinero
3. Retirar dinero
4. Salir

Según la opción elegida:
Si elige 1, mostrar el saldo actual.
Si elige 2, pedir un monto a depositar y sumarlo al saldo.
Si elige 3, pedir un monto a retirar. Si hay saldo suficiente, descontarlo; si no, mostrar mensaje de error.
Si elige 4, finalizar el programa con un mensaje de despedida.
Si elige cualquier otra cosa, mostrar un mensaje de "Opción no válida".
El menú se debe repetir hasta que el usuario elija salir.

Instrucciones:
Usar while True: para repetir el menú.
Validar los montos ingresados (no pueden ser negativos o cero).
Usar condicionales anidados donde sea necesario.
Agregar mensajes descriptivos para que el usuario sepa qué está pasando.

# Función para imprimir el saldo:
def impresor_saldo(SaldoFn):
    print(f"Su saldo actual es de ${SaldoFn}.")

# Función de depósito:
def depositar(SaldoFn):
    while True:
        EntradaUsuario = input("Ingrese el monto a depositar u oprima el botón de cancelar (c): ")
        try:
            MontoDepositarFn = float(EntradaUsuario)
            if MontoDepositarFn > 0:
                SaldoFn += MontoDepositarFn
                print(f"El monto ${MontoDepositarFn} ha sido agregado correctamente a su cuenta. Su nuevo saldo es de ${SaldoFn}.")
                return SaldoFn
            else:
                print("El monto a depositar debe ser un número positivo. Intente nuevamente.")
        except ValueError:
            if EntradaUsuario.lower() == "c":
                print("Acción cancelada. Volviendo al menú.")
                return SaldoFn
            else:
                print("ERROR: Debe ingresar un número u oprimir el botón de cancelar (c).")

# Función de retiro:
def retirar(SaldoFn):
    while True:
        EntradaUsuario = input("Ingrese el monto a retirar u oprima el botón de cancelar (c): ")
        try:
            MontoRetirarFn = float(EntradaUsuario)
            if MontoRetirarFn > 0 and MontoRetirarFn <= SaldoFn:
                SaldoFn -= MontoRetirarFn
                print(f"Usted ha retirado ${MontoRetirarFn} de su cuenta. Su nuevo saldo es ${SaldoFn}")
                return SaldoFn
            elif MontoRetirarFn <= 0:
                print("El monto a retirar debe ser mayor a cero. Intente nuevamente.")
            else:
                print(f"Saldo insuficiente. Su saldo actual es ${SaldoFn}. Intente nuevamente.")
        except ValueError:
            if EntradaUsuario.lower() == "c":
                print("Acción cancelada. Volviendo al menú.")
                return SaldoFn
            else:
                print("ERROR: Debe ingresar un número u oprimir el botón de cancelar (c).")

# Función de login:
def login():
    intentos_cuenta = 1
    while intentos_cuenta <= 3:
        NumCuenta = input("Ingrese su número de cuenta: ")
        if NumCuenta in cuentas:
            intentos_pin = 1
            while intentos_pin <= 3:
                PIN = input("Bienvenido! Por favor, ingrese su pin: ")
                if PIN == cuentas[NumCuenta][0]:
                    SaldoUsuario = cuentas[NumCuenta][1]
                    print("Ingreso exitoso!")
                    return NumCuenta, SaldoUsuario
                else:
                    print(f"PIN incorrecto. Le quedan {3 - intentos_pin} intento(s).")
                    intentos_pin += 1
            print("Ha superado el número de intentos para el PIN. Acceso denegado.")
            return None, None
        else:
            print(f"Número de cuenta inválido. Le quedan {3 - intentos_cuenta} intento(s).")
            intentos_cuenta += 1
    print("Ha superado el número de intentos para el número de cuenta. Acceso denegado.")
    return None, None


# Diccionario de cuentas:
cuentas = {
    "1234": ["0000", 10000],
    "5678": ["1234", 5000]
}

saldo = 0

# Llamada al login
NumCuenta, saldo = login()

if NumCuenta is not None:
    while True:
        try:
            OpUsuario = int(input("\n=== Cajero Automático ===\n1. Consultar saldo\n2. Depositar dinero\n3. Retirar dinero\n4. Salir\nIngrese su opción ahora: "))
            if OpUsuario == 1:
                impresor_saldo(saldo)
            elif OpUsuario == 2:
                saldo = depositar(saldo)
            elif OpUsuario == 3:
                saldo = retirar(saldo)
            elif OpUsuario == 4:
                print("Muchas gracias por usar nuestro cajero automático!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("ERROR: Debe ingresar un número entero. Intente nuevamente.")
else:
    print("Gracias por usar el cajero, intente nuevamente más tarde")
    
#Fin segunda actividad parte 1"""

#Tercera actividad (23-4-25)
"""PRÁCTICA
Manejo de una agenda de contactos (la clave del diccionario será el DNI de cada persona). Se debe comprobar
que no existan DNI (claves) duplicadas.
En el Alta pedir el ingreso por teclado de los nombre, DNI, teléfono, email. Al ﬁnalizar el ingreso, mostrar por
pantalla los datos ingresados (clave/valor).
Todas las funcionalidades deben estar contenidas en un Menú.
1: Alta de Contacto - 2: Busqueda de Contacto (x dni) - 3: Actualizar Contacto (x dni) - 4: Eliminar Contacto
(x dni) - 5: Mostrar todos los contactos - 6: Salir
En el caso de la actualización, mostrar las opciones (datos) para actualizar, como si fuera un
submenu."""
"""
#Recursos necesarios:
import re
import os
import platform
import time

#Función limpiar pantalla:
def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
#Función de espera por tiempo:
def pausar_tiempo():
    time.sleep(2)
#Función de espera por tecla:
def pausar_tecla():
    input("Presione una tecla para continuar...")
    limpiar_pantalla()
#Función impresora de contactos:
def ImprimirDatos(diccionario):
    for elemento in diccionario:
        print(f"{elemento}:{diccionario[elemento]}")
        
# Función para limpiar datos:
def LimpiarDato(dato):
    return re.sub(r'[^0-9]', '', dato)

#Función confirmar:
def Confirmar():
    confirmado = 0
    while True:
        EntradaUsuario = input().lower()
        if EntradaUsuario == "s":
            limpiar_pantalla()
            confirmado = 1
            return confirmado
        elif EntradaUsuario == "n":
            limpiar_pantalla()
            return confirmado
        else:
            print("Valor inválido. Intente nuevamente!")
    
#Función alta de contacto:
def AltaContacto(dict_contactos):
    nuevo_contacto = {}
    while True:
            dni=input("Ingrese el DNI del nuevo contacto (Sin puntos o comas): ")
            dni_limpio = LimpiarDato(dni)
            if dni_limpio in dict_contactos:
                print("Este DNI ya existe. No se puede duplicar.")
            else:
                print(f"El DNI ingresado es {dni}. ¿Desea guardarlo así? Oprima S para sí u oprima N para reintentar: ")
                if Confirmar():
                    if len(dni_limpio) >= 7 and len(dni_limpio) <= 8:
                        nuevo_contacto["DNI"] = dni_limpio
                        break
                    else:
                        print("Longitud de DNI inválida. Intente nuevamente!")
                else:
                    print("Redirigiendo para el nuevo ingreso...")
                    pausar_tiempo()
    
    while True:
        nombre = input("Ingrese el nombre del contacto: ")
        print(f"El nombre ingresado es {nombre}. ¿Desea guardarlo así? Oprima S para sí u oprima N para reintentar: ")
        if Confirmar():
            nuevo_contacto["Nombre"] = nombre
            break
        else:
            print("Redirigiendo para el nuevo ingreso...")
            pausar_tiempo()
            
    while True:
        telefono = input("Ingrese el teléfono del contacto (sin guiones o signos): ")
        print(f"El teléfono ingresado es {telefono}. ¿Desea guardarlo así? Oprima S para sí u oprima N para reintentar: ")
        if Confirmar():
            telefono_limpio = LimpiarDato(telefono)
            nuevo_contacto["Teléfono"] = telefono_limpio
            break
        else:
            print("Redirigiendo para el nuevo ingreso...")
            pausar_tiempo()
            
    while True:
        email = input("Ingrese el email del contacto: ")
        if "@" not in email:
            print("Email inválido. Intente nuevamente!")
        else:
            print(f"El email ingresado es {email}. ¿Desea guardarlo así? Oprima S para sí u oprima N para reintentar: ")
            if Confirmar():
                email = email.lower()
                nuevo_contacto["Email"] = email
                break
            else:
                print("Redirigiendo para el nuevo ingreso...")
                pausar_tiempo()
                
    print(f"El nuevo contacto tiene la siguiente información: \nDNI: {dni} \nNombre: {nombre} \nTeléfono: {telefono} \nEmail: {email} \n¿Desea guardarlo así? Oprima S para sí u oprima N para reintentar: ")
    if Confirmar():
        dict_contactos[dni_limpio] = nuevo_contacto
        print("Contacto agregado correctamente!")
        limpiar_pantalla()
    else:
        print("Redirigiendo para el nuevo ingreso...")
        pausar_tiempo()
        
def BuscarContacto(dict_contactos):
    while True:
        dni_buscar = input("Ingrese el DNI del contacto a buscar (Sin puntos o comas): ")
        dni_buscar_limpio = LimpiarDato(dni_buscar)
        print(f"El DNI ingresado para la búsqueda es {dni_buscar}. ¿Es correcto? Oprima S para sí u oprima N para reintentar: ")
        if Confirmar():
            if dni_buscar_limpio in dict_contactos.keys():
                contacto_encontrado = dict_contactos[dni_buscar_limpio]
                print("Contacto encontrado! Imprimiendo datos...")
                ImprimirDatos(contacto_encontrado)
                pausar_tecla()
                break
            else:
                print("Contacto no encontrado. Desea buscar otro (S/N)?: ")
                if Confirmar() == 0:
                    break
        else:
            print("Redirigiendo para el nuevo ingreso...")
            pausar_tiempo()


def ActualizarContacto(dict_contactos):
    while True:
        dni_actualizar = input("Ingrese el DNI del contacto que quiere actualizar (Sin puntos o comas): ")
        dni_actualizar_limpio = LimpiarDato(dni_actualizar)
        print(f"El DNI ingresado para actualizar es {dni_actualizar}. ¿Es correcto? Oprima S para sí u oprima N para reintentar: ")
        if Confirmar():
            if dni_actualizar_limpio in dict_contactos.keys():
                contacto_encontrado = dict_contactos[dni_actualizar_limpio]
                print("Contacto encontrado! Imprimiendo datos...")
                ImprimirDatos(contacto_encontrado)
                dato_actualizar = input("Ingrese el dato que quiere actualizar:\n1. DNI\n2. Nombre\n3. Teléfono\n4. Email\n5. Cancelar\nIngrese su opción ahora: ")
                if dato_actualizar == "1":
                    nuevo_dni = input("Dato correcto! Ingrese el nuevo DNI: ")
                    nuevo_dni_limpio = LimpiarDato(nuevo_dni)
                    if nuevo_dni_limpio in dict_contactos:
                        print("El DNI ingresado ya existe. No puede haber duplicados.")
                    elif len(nuevo_dni_limpio) < 7 or len(nuevo_dni_limpio) > 8:
                        print("Longitud de DNI inválida.")
                    else:
                        contacto_encontrado["DNI"] = nuevo_dni_limpio
                        dict_contactos[nuevo_dni_limpio] = contacto_encontrado
                        del dict_contactos[dni_actualizar_limpio]
                        print("DNI actualizado correctamente! Imprimiendo contacto para revisión...")
                        ImprimirDatos(contacto_encontrado)
                        pausar_tecla()
                        break
                elif dato_actualizar == "2":
                    nuevo_nombre = input("Dato correcto! Ingrese el nuevo nombre actualizado: ")
                    contacto_encontrado["Nombre"] = nuevo_nombre
                    print("Nombre actualizado correctamente! Imprimiendo contacto para revisión...")
                    ImprimirDatos(contacto_encontrado)
                    pausar_tecla()
                    break
                elif dato_actualizar == "3":
                    nuevo_telefono = input("Dato correcto! Ingrese el nuevo teléfono: ")
                    nuevo_telefono_limpio = LimpiarDato(nuevo_telefono)
                    contacto_encontrado["Teléfono"] = nuevo_telefono_limpio
                    print("Teléfono actualizado correctamente! Imprimiendo contacto para revisión...")
                    ImprimirDatos(contacto_encontrado)
                    pausar_tecla()
                    break
                elif dato_actualizar == "4":
                    nuevo_email = input("Dato correcto! Ingrese el nuevo email: ")
                    contacto_encontrado["Email"] = nuevo_email
                    print("Email actualizado correctamente! Imprimiendo contacto para revisión...")
                    ImprimirDatos(contacto_encontrado)
                    pausar_tecla()
                    break
                elif dato_actualizar == "5":
                    print("Cancelando actualización...")
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
            else:
                print("Contacto no encontrado! Intente nuevamente...")
        else:
            print("Redirigiendo para el nuevo ingreso...")

def EliminarContacto(dict_contactos):
    while True:
        dni_eliminar = input("Ingrese el DNI del contacto que quiere borrar (Sin puntos o comas): ")
        dni_eliminar_limpio = LimpiarDato(dni_eliminar)
        print(f"El DNI ingresado para actualizar es {dni_eliminar}. ¿Es correcto? Oprima S para sí u oprima N para reintentar: ")
        if Confirmar():
            if dni_eliminar_limpio in dict_contactos.keys():
                print("¿Está seguro de querer eliminarlo? Oprima S para sí u oprima N para reintentar: ")
                if Confirmar():
                    print("Eliminando contacto. Por favor espere...")
                    del dict_contactos[dni_eliminar_limpio]
                    pausar_tiempo()
                    print("Contacto eliminado correctamente.")
                    pausar_tecla()
                    break
                else:
                    print("Eliminación cancelada. Redirigiendo al menú principal...")
                    pausar_tiempo()
                    break
            else:
                print("Contacto no encontrado! Intente nuevamente...")
        else:
            print("Redirigiendo para nuevo ingreso...")
            pausar_tiempo()
            
def MostrarContactos(dict_contactos):
    i = 1
    for dni, datos in dict_contactos.items():
        print(f"Contacto {i} (DNI: {dni}): ")
        ImprimirDatos(datos)
        print("<---------->")
        i += 1
    pausar_tecla()
        
contactos = {
     "12345678": {
        "DNI": "12345678",
        "Nombre": "Juan Pérez",
        "Teléfono": "123456789",
        "Email": "juan.perez@mail.com"
    },
    "87654321": {
        "DNI": "87654321",
        "Nombre": "Ana García",
        "Teléfono": "987654321",
        "Email": "ana.garcia@mail.com"
    },
    "11223344": {
        "DNI": "11223344",
        "Nombre": "Carlos Rodríguez",
        "Teléfono": "1122334455",
        "Email": "carlos.rodriguez@mail.com"
    },
    "99887766": {
        "DNI": "99887766",
        "Nombre": "Laura Gómez",
        "Teléfono": "9988776655",
        "Email": "laura.gomez@mail.com"
    }
}
while True:
    try:
        OpUsuario = int(input("\n=== Agenda telefónica ===\n1. Dar de alta un contacto\n2. Buscar un contacto \n3. Actualizar un contacto\n4. Eliminar contacto\n5. Mostrar todos los contactos\n6. Salir\nIngrese su opción ahora: "))
        if OpUsuario == 1:
            AltaContacto(contactos)
        elif OpUsuario == 2:
            BuscarContacto(contactos)
        elif OpUsuario == 3:
            ActualizarContacto(contactos)
        elif OpUsuario == 4:
            EliminarContacto(contactos)
        elif OpUsuario == 5:
            MostrarContactos(contactos)
        elif OpUsuario == 6:
            print("Muchas gracias por usar nuestra agenda. Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente...")
    except ValueError:
        print("ERROR: debe ingresar un número entre el 1 al 6. Intente nuevamente.")
        
"""
#Cosas para agregar:
#1. Opción de cancelar para el alta, búsqueda, actualización, eliminación


#<----->
#Recursos importantes:
import re
import os
import platform
import time
#<----->
# Función limpiar pantalla:
def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
#<----->
# Función de espera por tiempo:
def pausar_tiempo():
    time.sleep(2)
#<----->
# Función de espera por tecla:
def pausar_tecla():
    input("Presione una tecla para continuar...")
    limpiar_pantalla()
#<----->
# Función impresora de datos:
def ImprimirDatos(diccionario):
    for elemento in diccionario:
        print(f"{elemento}:{diccionario[elemento]}")
#<----->
# Función para limpiar datos:
def LimpiarDato(dato):
    return re.sub(r'[^0-9]', '', dato)
#<----->
# Función confirmar:
def Confirmar():
    confirmado = 0
    while True:
        EntradaUsuario = input().lower()
        if EntradaUsuario == "s":
            limpiar_pantalla()
            confirmado = 1
            return confirmado
        elif EntradaUsuario == "n":
            limpiar_pantalla()
            return confirmado
        elif EntradaUsuario == "c":
            print("Operación cancelada.")
            pausar_tecla()
            limpiar_pantalla()
            return None
        else:
            print("Valor inválido. Intente nuevamente!")
#<----->
# Función alta de contacto:
def AltaContacto(dict_contactos):
    nuevo_contacto = {}
    while True:
        dni = input("Ingrese el DNI del nuevo contacto (Sin puntos o comas): ")
        dni_limpio = LimpiarDato(dni)
        
        if len(dni_limpio) < 7 or len(dni_limpio) > 8:
            print("Longitud de DNI inválida. Intente nuevamente!")
        elif dni_limpio in dict_contactos:
            print("Este DNI ya existe. No se puede duplicar.")
        else:
            print(f"El DNI ingresado es {dni}. ¿Desea guardarlo así? Oprima S para sí, N para reintentar o C para cancelar: ")
            confirmacion = Confirmar()
            if confirmacion is None:
                return
            elif confirmacion == 1:
                nuevo_contacto["DNI"] = dni_limpio
                pausar_tecla()
                break
            else:
                print("Redirigiendo para nuevo ingreso...")
                pausar_tiempo()

    while True:
        nombre = input("Ingrese el nombre del contacto: ")
        print(f"El nombre ingresado es {nombre}. ¿Desea guardarlo así? Oprima S para sí, N para reintentar o C para cancelar: ")
        confirmacion = Confirmar()
        if confirmacion is None:
            return
        elif confirmacion == 1:
            nuevo_contacto["Nombre"] = nombre
            pausar_tecla()
            break
        else:
            print("Redirigiendo para nuevo ingreso...")
            pausar_tiempo()

    while True:
        telefono = input("Ingrese el teléfono del contacto (sin guiones o signos): ")
        telefono_limpio = LimpiarDato(telefono)
        print(f"El teléfono ingresado es {telefono}. ¿Desea guardarlo así? Oprima S para sí, N para reintentar o C para cancelar: ")
        confirmacion = Confirmar()
        if confirmacion is None:
            return
        elif confirmacion == 1:
            nuevo_contacto["Teléfono"] = telefono_limpio
            pausar_tecla()
            break
        else:
            print("Redirigiendo para nuevo ingreso...")
            pausar_tiempo()

    while True:
        email = input("Ingrese el email del contacto: ")
        if "@" not in email:
            print("Email inválido. Intente nuevamente!")
        else:
            print(f"El email ingresado es {email}. ¿Desea guardarlo así? Oprima S para sí, N para reintentar o C para cancelar: ")
        confirmacion = Confirmar()
        if confirmacion is None:
            return
        elif confirmacion == 1:
            nuevo_contacto["Email"] = email
            pausar_tecla()
            break
        else:
            print("Redirigiendo para nuevo ingreso...")
            pausar_tiempo()

    print(f"El nuevo contacto tiene la siguiente información: \nDNI: {dni} \nNombre: {nombre} \nTeléfono: {telefono} \nEmail: {email} \n¿Desea guardarlo así? Oprima S para sí, N para reintentar o C para cancelar: ")
    confirmacion = Confirmar()
    if confirmacion is None:
        return
    elif confirmacion == 1:
        dict_contactos[dni_limpio] = nuevo_contacto
        print("Contacto agregado correctamente!")
        pausar_tiempo()
        limpiar_pantalla()
    else:
        print("Redirigiendo para nuevo ingreso...")
        pausar_tiempo()
#<----->
# Función para buscar contacto:
def BuscarContacto(dict_contactos):
    while True:
        dni_buscar = input("Ingrese el DNI del contacto a buscar (Sin puntos o comas): ")
        dni_buscar_limpio = LimpiarDato(dni_buscar)
        print(f"El DNI ingresado para la búsqueda es {dni_buscar}. ¿Es correcto? Oprima S para sí, N para reintentar o C para cancelar: ")
        confirmacion = Confirmar()
        if confirmacion is None:
            return
        elif confirmacion == 1:
            if dni_buscar_limpio in dict_contactos.keys():
                contacto_encontrado = dict_contactos[dni_buscar_limpio]
                print("Contacto encontrado! Imprimiendo datos...")
                ImprimirDatos(contacto_encontrado)
                pausar_tecla()
                break
            else:
                print("Contacto no encontrado. ¿Desea buscar otro (S/N)?")
                confirmacion = Confirmar()
                if confirmacion is None or confirmacion == 0:
                    break
                else:
                    pass
        else:
            print("Redirigiendo para nuevo ingreso...")
            pausar_tiempo()

# Función para actualizar contacto:
def ActualizarContacto(dict_contactos):
    while True:
        dni_actualizar = input("Ingrese el DNI del contacto que quiere actualizar (Sin puntos o comas): ")
        dni_actualizar_limpio = LimpiarDato(dni_actualizar)
        print(f"El DNI ingresado para actualizar es {dni_actualizar}. ¿Es correcto? Oprima S para sí, N para reintentar o C para cancelar: ")
        confirmacion = Confirmar()
        if confirmacion is None:
            return
        elif confirmacion == 1:
            if dni_actualizar_limpio in dict_contactos:
                contacto_encontrado = dict_contactos[dni_actualizar_limpio]
                print("Contacto encontrado! Imprimiendo datos...")
                ImprimirDatos(contacto_encontrado)
                dato_actualizar = input("Ingrese el dato que quiere actualizar:\n1. DNI\n2. Nombre\n3. Teléfono\n4. Email\n5. Cancelar\nIngrese su opción ahora: ")
                if dato_actualizar == "1":
                    nuevo_dni = input("Dato correcto! Ingrese el nuevo DNI: ")
                    nuevo_dni_limpio = LimpiarDato(nuevo_dni)
                    if nuevo_dni_limpio in dict_contactos:
                        print("El DNI ingresado ya existe. No puede haber duplicados.")
                    elif len(nuevo_dni_limpio) < 7 or len(nuevo_dni_limpio) > 8:
                            print("Longitud de DNI inválida.")
                    else:                            
                        contacto_encontrado["DNI"] = nuevo_dni_limpio
                        dict_contactos[nuevo_dni_limpio] = contacto_encontrado
                        del dict_contactos[dni_actualizar_limpio]
                        print("DNI actualizado correctamente! Imprimiendo contacto para revisión...")
                        ImprimirDatos(contacto_encontrado)
                        pausar_tecla()
                        break
                elif dato_actualizar == "2":
                    nuevo_nombre = input("Dato correcto! Ingrese el nuevo nombre actualizado: ")
                    contacto_encontrado["Nombre"] = nuevo_nombre
                    print("Nombre actualizado correctamente! Imprimiendo contacto para revisión...")
                    ImprimirDatos(contacto_encontrado)
                    pausar_tecla()
                    break
                elif dato_actualizar == "3":
                    nuevo_telefono = input("Dato correcto! Ingrese el nuevo teléfono: ")
                    nuevo_telefono_limpio = LimpiarDato(nuevo_telefono)
                    contacto_encontrado["Teléfono"] = nuevo_telefono_limpio
                    print("Teléfono actualizado correctamente! Imprimiendo contacto para revisión...")
                    ImprimirDatos(contacto_encontrado)
                    pausar_tecla()
                    break
                elif dato_actualizar == "4":
                    nuevo_email = input("Dato correcto! Ingrese el nuevo email: ")
                    contacto_encontrado["Email"] = nuevo_email
                    print("Email actualizado correctamente! Imprimiendo contacto para revisión...")
                    ImprimirDatos(contacto_encontrado)
                    pausar_tecla()
                    break
                elif dato_actualizar == "5":
                    print("Cancelando actualización...")
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
            else:
                print("Contacto no encontrado! Intente nuevamente...")
        else:
            print("Redirigiendo para el nuevo ingreso...")
            pausar_tiempo()  

# Función para eliminar contacto:
def EliminarContacto(dict_contactos):
    while True:
        dni_eliminar = input("Ingrese el DNI del contacto que quiere borrar (Sin puntos o comas): ")
        dni_eliminar_limpio = LimpiarDato(dni_eliminar)
        print(f"El DNI ingresado para eliminar es {dni_eliminar}. ¿Es correcto? Oprima S para sí, N para reintentar o C para cancelar: ")
        confirmacion = Confirmar()
        if confirmacion is None:
            return
        elif confirmacion == 1:
            if dni_eliminar_limpio in dict_contactos.keys():
                print("Contacto encontrado. ¿Está seguro de querer eliminarlo? Oprima S para sí, N para reintentar o C para cancelar: ")
                confirmacion = Confirmar()
                if confirmacion is None:
                    return
                elif confirmacion == 1:
                    print("Eliminando contacto. Espere un momento, por favor...")
                    del dict_contactos[dni_eliminar_limpio]
                    pausar_tiempo()
                    print("Contacto eliminado correctamente.")
                    pausar_tecla()
                    break
                else:
                    print("Redirigiendo para el nuevo ingreso...")
                    pausar_tiempo()
            else:
                print("Contacto no encontrado! Intente nuevamente...")
                pausar_tiempo()
        else:
            print("Redirigiendo para el nuevo ingreso...")
            pausar_tiempo()

# Función para mostrar todos los contactos:
def MostrarContactos(dict_contactos):
    i = 1
    for dni, datos in dict_contactos.items():
        print(f"Contacto {i} (DNI: {dni}): ")
        ImprimirDatos(datos)
        print("<---------->")
        i += 1
    pausar_tecla()

# Programa principal:
contactos = {
     "12345678": {
        "DNI": "12345678",
        "Nombre": "Juan Pérez",
        "Teléfono": "123456789",
        "Email": "juan.perez@mail.com"
    },
    "87654321": {
        "DNI": "87654321",
        "Nombre": "Ana García",
        "Teléfono": "987654321",
        "Email": "ana.garcia@mail.com"
    },
    "11223344": {
        "DNI": "11223344",
        "Nombre": "Carlos Rodríguez",
        "Teléfono": "1122334455",
        "Email": "carlos.rodriguez@mail.com"
    },
    "99887766": {
        "DNI": "99887766",
        "Nombre": "Laura Gómez",
        "Teléfono": "9988776655",
        "Email": "laura.gomez@mail.com"
    }
}

while True:
    try:
        OpUsuario = int(input("\n=== Agenda telefónica ===\n1. Dar de alta un contacto\n2. Buscar un contacto \n3. Actualizar un contacto\n4. Eliminar contacto\n5. Mostrar todos los contactos\n6. Salir\nIngrese su opción ahora: "))
        if OpUsuario == 1:
            AltaContacto(contactos)
        elif OpUsuario == 2:
            BuscarContacto(contactos)
        elif OpUsuario == 3:
            ActualizarContacto(contactos)
        elif OpUsuario == 4:
            EliminarContacto(contactos)
        elif OpUsuario == 5:
            MostrarContactos(contactos)
        elif OpUsuario == 6:
            print("Muchas gracias por usar nuestra agenda. Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente...")
    except ValueError:
        print("ERROR: debe ingresar un número entre el 1 al 6. Intente nuevamente.")
