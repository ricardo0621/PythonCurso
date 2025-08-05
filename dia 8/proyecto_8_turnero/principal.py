from os import system
import numeros

# Proyecto 8: Turnero para Perfumería, Farmacia y Cosméticos
# Este programa permite a los usuarios obtener un número de turno para diferentes secciones de una tienda


def limpiar_pantalla():
    system('cls')

def preguntar_continuar():
    """
    Pregunta si el usuario desea otro turno.
    Usa try/except para capturar errores inesperados.
    Devuelve True (continuar) o False (salir).
    """
    while True:
        print('\n----------------------------------')
        print('¿Desea solicitar otro turno?')
        print('Presione "s" para continuar o "n" para salir.')

        # Captura la entrada del usuario
        x = input().strip().lower()
        limpiar_pantalla()  # Limpia la pantalla para una mejor visualización
        # Verifica la respuesta del usuario
        if x == 's':
            return True  # Continuar solicitando turnos
        elif x == 'n':
            print('Gracias por usar el sistema de turnos. ¡Hasta luego!')
            return False  # Salir del programa
        else:
            # Maneja entradas no válidas
            print('Por favor, ingrese una opción válida (s/n).')



def ejecutar_programa():
    print('****** Bienvenido al sistema de turnos para Perfumería, Farmacia y Cosméticos ******\n')
    while True:
        opcion = None  # Inicializa la variable opcion
        try:
            print('seleccione el area para asignar turno:')
            opcion = input('(P) Perfume, (F) Farmacia, (C) Cosmeticos: ').lower().strip()
            if opcion not in ('p', 'f', 'c'):
                limpiar_pantalla()
                print('Por favor, ingrese una opción válida (p, f, c).\n')
                continue  # Vuelve al inicio del bucle si la opción no es válida
        except ValueError:
            print('Por favor, ingrese un valor válido.\n')
            continue  # Vuelve al inicio del bucle si hay un error

        if opcion == 'p':
            numeros.perfume()
        elif opcion == 'f':
            numeros.farmacia()
        else:
            numeros.cosmeticos()

        if not preguntar_continuar():
            break


if __name__ == '__main__':
    # Ejecuta el programa principal
    ejecutar_programa()
