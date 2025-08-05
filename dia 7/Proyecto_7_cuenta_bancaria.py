import random
from os import system


class Persona:# Clase base para representar una persona
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):# Clase derivada que representa a un cliente, hereda de persona
    def __init__(self,nombre,apellido,numero_cuenta,saldo):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido}, Cuenta: {self.numero_cuenta}, Saldo: ${self.saldo}'

    def depositar(self,cantidad):
        if cantidad > 0:
            self.saldo = self.saldo + cantidad
            system('cls')  # Limpiar consola antes de mostrar el menú
            print(f'{self.nombre} {self.apellido} Depósito exitoso.')
            print('-' * 40)
        else:
            print('Cantidad a depositar debe ser mayor que cero.')

    def retirar(self,cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo = self.saldo - cantidad
            system('cls')  # Limpiar consola antes de mostrar el menú
            print(f'{self.nombre} {self.apellido} Retiro exitoso.')
            print('-' * 40)
        else:
            print(f'Cantidad a retirar debe ser mayor que cero y no puede exceder el saldo disponible.\n Tu saldo actual es: ${self.saldo}')

def crear_cliente():
    nombre = input('Ingrese el nombre del cliente: ')
    apellido = input('Ingrese el apellido del cliente: ')
    system('cls')  # Limpiar consola al inicio
    numero_cuenta = random.randint(1000000, 9999999)  # Genera un número de cuenta aleatorio entre 1000000 y 9999999
    saldo = 0
    return Cliente(nombre, apellido, numero_cuenta, saldo)

def inicio():
    system('cls')  # Limpiar consola al inicio
    print("**** Bienvenido al sistema bancario ****")
    # Se crea un cliente nuevo
    cliente = crear_cliente()
    while True:

        print(cliente)
        print('-' * 40)
        print('\n')
        accion = input("¿Desea depositar (d) o retirar (r) dinero? (s para salir): ").lower().strip()# convierte la entrada a minúsculas
        if accion not in ['d', 'r', 's']:
            print("Opción no válida. Por favor, elija 'd' para depositar, 'r' para retirar o 's' para salir.")
            continue
        # Si la opción es válida, se procede a depositar o retirar dinero
        if accion == 'd':
            cantidad = input("Ingrese la cantidad a depositar: ")
            if cantidad.isdigit():# verifica si la entrada es un número entero positivo
                cantidad = int(cantidad)  # Convierte la entrada a entero
            else:
                print("Cantidad inválida. Debe ser un número positivo.")
                continue
            cliente.depositar(cantidad)# llama al método depositar de la clase Cliente

        elif accion == 'r':
            if cliente.saldo == 0:
                print("No puede retirar dinero, su saldo es cero.")
                continue
            cantidad = input("Ingrese la cantidad a retirar: ")
            if cantidad.isdigit():
                cantidad = int(cantidad)  # Convierte la entrada a entero
            else:
                print("Cantidad inválida. Debe ser un número positivo.")
                continue
            cliente.retirar(cantidad)

        elif accion == 's':
            print("Gracias por usar el sistema bancario. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
inicio()





