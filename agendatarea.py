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
    #re.sub(tipo de cadena, patron, reemplazo, texto)
    #tipo de cadena: raw (cada caracter se procesa "crudo", sin tener en cuenta valores especiales o reservados)
    #patrón: lo que debe detectar en el texto.
    #reemplazo: por lo que se debe reemplazar cada incidencia del patrón en el texto.
    #texto: cadena para analizar, se recorre caracter a caracter detectando el patrón y reemplazandolo por el reemplazo.
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
        if "@" in email:
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
        else:
                print("Email inválido. Intente nuevamente!")

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