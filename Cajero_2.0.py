#Recursos necesarios:
import os
import platform
import datetime

#Lista de movimientos:
Movimientos = []

#Función limpiar pantalla:
def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

#Función de espera:
def pausar():
    input("Presione una tecla para continuar...")
    limpiar_pantalla()

# Función para imprimir el saldo:
def impresor_saldo(SaldoFn):
    print(f"Su saldo actual es de ${SaldoFn}.")

#Función de registro de movimientos:
def registrar_movimiento(TipoMovimiento, Cantidad, ListaMovimientos, hora_movimiento=None):
    if hora_movimiento is None:
        hora_movimiento = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
    movimiento_registrar = {"Tipo": TipoMovimiento,"Cantidad": Cantidad,"Hora": hora_movimiento}
    ListaMovimientos.append(movimiento_registrar)
    return

#Función de mostrar movimientos:
def mostrar_movimientos(ListaMovimientos):
    if ListaMovimientos:
        i = 1
        for movimiento in ListaMovimientos:
            print(f"Movimiento {i}: {movimiento}")
            i+=1
    else:
        print("No hay movimientos recientes!")

# Función de depósito:
def depositar(SaldoFn):
    while True:
        EntradaUsuario = input("Ingrese el monto a depositar u oprima el botón de cancelar (c): ")
        try:
            MontoDepositarFn = float(EntradaUsuario)
            if MontoDepositarFn > 0:
                SaldoFn += MontoDepositarFn
                print(f"El monto ${MontoDepositarFn} ha sido agregado correctamente a su cuenta. Su nuevo saldo es de ${SaldoFn}.")
                registrar_movimiento("Depósito", MontoDepositarFn, Movimientos)
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
                registrar_movimiento("Retiro", MontoRetirarFn, Movimientos)
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
        print("DEBUG: Números de cuenta válidos con su respectiva contraseña: [1234 : 0000], [5678 : 1234]")
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
    limpiar_pantalla()
    while True:
        try:
            OpUsuario = int(input("\n=== Cajero Automático ===\n1. Consultar saldo\n2. Depositar dinero\n3. Retirar dinero\n4. Mostrar movimientos\n5. Salir\nIngrese su opción ahora: "))
            if OpUsuario == 1:
                impresor_saldo(saldo)
                pausar()
            elif OpUsuario == 2:
                saldo = depositar(saldo)
                pausar()
            elif OpUsuario == 3:
                saldo = retirar(saldo)
                pausar()
            elif OpUsuario == 4:
                mostrar_movimientos(Movimientos)
            elif OpUsuario == 5:
                print("Muchas gracias por usar nuestro cajero automático!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("ERROR: Debe ingresar un número entero. Intente nuevamente.")
else:
    print("Gracias por usar el cajero, intente nuevamente más tarde")