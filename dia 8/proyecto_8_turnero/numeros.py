
def turno_seccion(prefijo):
    """
    Esta función devuelve el número de turno para la sección.
    """
    for numero in range(1,5):
        yield f'{prefijo}-{numero}'


# Generadores para cada sección
# Cada generador produce un número de turno único para cada sección
generador_perfume = turno_seccion('P')
generador_farmacia = turno_seccion('F')
generador_cosmeticos = turno_seccion('C')


def decorar_turno(generador):
    """
    Decorador que imprime un mensaje antes y después de obtener el turno.
    """
    def turno():
        try:
            print('\n'+'*'*23)
            print('Su turno es:')
            print(next(generador))
            print('espere su turno con paciencia')
            print('*' * 23+'\n')
        except StopIteration:
            print('NO HAY MAS TURNOS')
    return turno

perfume = decorar_turno(generador_perfume)
farmacia = decorar_turno(generador_farmacia)
cosmeticos = decorar_turno(generador_cosmeticos)



