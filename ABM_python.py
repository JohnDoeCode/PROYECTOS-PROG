#<----->
# Recursos importantes:
import platform
import os
import time
import re
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
# Función alta de usuario:
contador_id = 1            
def AltaUsuario(lista_usuarios):
    global contador_id
    nuevo_usuario = {}
    while True:
        id_usuario = contador_id
        nuevo_usuario["ID"] = id_usuario
        contador_id += 1
        break

    while True:
        dni = input("Ingrese el DNI del nuevo contacto (Sin puntos o comas): ")
        dni_limpio = LimpiarDato(dni)
        
        if len(dni_limpio) < 7 or len(dni_limpio) > 8:
            print("Longitud de DNI inválida. Intente nuevamente!")
        elif any(usuario["DNI"] == dni_limpio for usuario in lista_usuarios):
            print("Este DNI ya existe. No se puede duplicar.")
        else:
            print(f"El DNI ingresado es {dni}. ¿Desea guardarlo así? Oprima S para sí, N para reintentar o C para cancelar: ")
            confirmacion = Confirmar()
            if confirmacion is None:
                return
            elif confirmacion == 1:
                nuevo_usuario["DNI"] = dni_limpio
                pausar_tecla()
                break
            else:
                print("Redirigiendo para nuevo ingreso...")
                pausar_tiempo()

    while True:
        nombre_apellido = input("Ingrese el nombre y apellido del usuario: ")
        print(f"El nombre ingresado es {nombre_apellido}. ¿Desea guardarlo así? Oprima S para sí, N para reintentar o C para cancelar: ")
        confirmacion = Confirmar()
        if confirmacion is None:
            return
        elif confirmacion == 1:
            nuevo_usuario["Nombre y Apellido"] = nombre_apellido
            pausar_tecla()
            break
        else:
            print("Redirigiendo para nuevo ingreso...")
            pausar_tiempo()

    while True:
        telefono = input("Ingrese el teléfono del usuario (sin guiones o signos): ")
        telefono_limpio = LimpiarDato(telefono)
        print(f"El teléfono ingresado es {telefono}. ¿Desea guardarlo así? Oprima S para sí, N para reintentar o C para cancelar: ")
        confirmacion = Confirmar()
        if confirmacion is None:
            return
        elif confirmacion == 1:
            nuevo_usuario["Teléfono"] = telefono_limpio
            pausar_tecla()
            break
        else:
            print("Redirigiendo para nuevo ingreso...")
            pausar_tiempo()

    while True:
        email = input("Ingrese el email del usuario: ")
        if "@" in email:
            print(f"El email ingresado es {email}. ¿Desea guardarlo así? Oprima S para sí, N para reintentar o C para cancelar: ")
            confirmacion = Confirmar()
            if confirmacion is None:
                return
            elif confirmacion == 1:
                nuevo_usuario["Email"] = email
                pausar_tecla()
                break
            else:
                print("Redirigiendo para nuevo ingreso...")
                pausar_tiempo()
        else:
            print("Email inválido. Intente nuevamente!")
    print(f"El nuevo usuario tiene la siguiente información:\nID: {id_usuario} \nDNI: {dni} \nNombre: {nombre_apellido} \nTeléfono: {telefono} \nEmail: {email} \n¿Desea guardarlo así? Oprima S para sí, N para reintentar o C para cancelar: ")
    confirmacion = Confirmar()
    if confirmacion is None:
        return
    elif confirmacion == 1:
        lista_usuarios.append(nuevo_usuario) 
        print("Contacto agregado correctamente!")
        pausar_tiempo()
        limpiar_pantalla()
    else:
        print("Redirigiendo para nuevo ingreso...")
        pausar_tiempo()

# Función para eliminar contacto:
def EliminarUsuario(lista_usuarios):
    while True:
        id_usuario_eliminar = int(input("Ingrese el ID del usuario que quiere borrar: "))
        try:
            print(f"El ID ingresado para eliminar es {id_usuario_eliminar}. ¿Es correcto? Oprima S para sí, N para reintentar o C para cancelar: ")
            confirmacion = Confirmar()
            if confirmacion is None:
                return
            elif confirmacion == 1:
                encontrado = False
                for usuario in lista_usuarios:
                    if usuario["ID"] == id_usuario_eliminar:
                        encontrado = True
                        print("Usuario encontrado. ¿Está seguro de querer eliminarlo? Oprima S para sí, N para reintentar o C para cancelar: ")
                        confirmacion = Confirmar()
                        if confirmacion is None:
                            return
                        elif confirmacion == 1:
                            print("Eliminando usuario. Espere un momento, por favor...")
                            lista_usuarios.remove(usuario)
                            pausar_tiempo()
                            print("Contacto eliminado correctamente.")
                            pausar_tecla()
                            break
                        else:
                            print("Redirigiendo para el nuevo ingreso...")
                            pausar_tiempo()
            if not encontrado:
                print("Usuario no encontrado! Intente nuevamente...")
                pausar_tiempo()
            else:
                print("Redirigiendo para el nuevo ingreso...")
                pausar_tiempo()
        except ValueError:
            print("ERROR: recuerde ingresar un número entero. Intente nuevamente!")

# Función para modificar contacto:
def ModificarUsuario(lista_usuarios):
    while True:
        id_actualizar = input("Ingrese el ID del contacto que quiere actualizar (Sin puntos o comas): ")
        print(f"El ID ingresado es {id_actualizar}. ¿Desea continuar? Oprima S para sí, N para reintentar o C para cancelar: ")
        confirmacion = Confirmar()
        if confirmacion is None:
            return
        elif confirmacion == 1:
            encontrado = False
            for usuario in lista_usuarios:
                if (usuario["ID"]) == id_actualizar:
                    encontrado = True
                    print("Usuario encontrado! Imprimiendo datos...")
                    usuario_encontrado = usuario
                    ImprimirDatos(usuario_encontrado)
                    print("¿Desea modificarlo? Oprima S para sí, N para reintentar o C para cancelar: ")
                    confirmacion = Confirmar()
                    if confirmacion is None:
                        return
                    elif confirmacion == 1:
                        dato_actualizar = input("Ingrese el dato que quiere actualizar:\n1. DNI\n2. Nombre\n3. Teléfono\n4. Email\n5. Cancelar\nIngrese su opción ahora: ")
                        if dato_actualizar == "1":
                            nuevo_dni = input("Dato correcto! Ingrese el nuevo DNI: ")
                            nuevo_dni_limpio = LimpiarDato(nuevo_dni)
                            if any(usuario["DNI"] == nuevo_dni_limpio for usuario in lista_usuarios):
                                print("El DNI ingresado ya existe. No puede haber duplicados.")
                            elif len(nuevo_dni_limpio) < 7 or len(nuevo_dni_limpio) > 8:
                                print("Longitud de DNI inválida.")
                            else:
                                usuario_encontrado["DNI"] = nuevo_dni_limpio
                                print("DNI actualizado correctamente! Imprimiendo contacto para revisión...")
                                ImprimirDatos(usuario_encontrado)
                                pausar_tecla()
                                break
                        elif dato_actualizar == "2":
                            nuevo_nombre = input("Dato correcto! Ingrese el nuevo nombre actualizado: ")
                            usuario_encontrado["Nombre y Apellido"] = nuevo_nombre
                            print("Nombre actualizado correctamente! Imprimiendo usuario para revisión...")
                            ImprimirDatos(usuario_encontrado)
                            pausar_tecla()
                            break
                        elif dato_actualizar == "3":
                            nuevo_telefono = input("Dato correcto! Ingrese el nuevo teléfono: ")
                            nuevo_telefono_limpio = LimpiarDato(nuevo_telefono)
                            usuario_encontrado["Teléfono"] = nuevo_telefono_limpio
                            print("Teléfono actualizado correctamente! Imprimiendo usuario para revisión...")
                            ImprimirDatos(usuario_encontrado)
                            pausar_tecla()
                            break
                        elif dato_actualizar == "4":
                            nuevo_email = input("Dato correcto! Ingrese el nuevo email: ")
                            usuario_encontrado["Email"] = nuevo_email
                            print("Email actualizado correctamente! Imprimiendo usuario para revisión...")
                            ImprimirDatos(usuario_encontrado)
                            pausar_tecla()
                            break
                        elif dato_actualizar == "5":
                            break
                        else:
                            print("Opción inválida. Redirigiendo para nuevo ingreso...")
                            pausar_tiempo()
            if not encontrado:
                print("Usuario no encontrado.")
                pausar_tiempo()
                break

def leer(ListaLeer):
    print("Los datos ingresados en la lista son: ")
    for elemento in ListaLeer:
        print(elemento)

usuarios = []
print("Bienvenido al sistema ABM! Ingrese su opción!:")
while True:
    try:
        OpUsuario = int(input("\n1. Alta \n2. Baja \n3. Modificación \n4. Mostrar  \n5. Salir \nIngrese ahora: "))
        if OpUsuario == 1:
            AltaUsuario(usuarios)
            print("\n<------------------------------------>")
        elif OpUsuario == 2:
            EliminarUsuario(usuarios)
            print("\n<------------------------------------>")
        elif OpUsuario == 3:
            ModificarUsuario(usuarios)
            print("\n<------------------------------------>")
        elif OpUsuario == 4:
            leer(usuarios)
            print("\n<------------------------------------>")
        elif OpUsuario == 5:
            print("Muchas gracias por usar el programa! Adiós!\n<------------------------------------>")
            break
        else:
            print("Opción inválida. Intente nuevamente!")
    except ValueError:
        print("ERROR: debe ingresar un número entre el 1 al 6. Intente nuevamente.")