
from time import time

def prueba_for(numero):
    lista = []
    for i in range(1,numero+1):
        lista.append(i)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista


inicio_for = time()
print("Iniciando prueba con for...")
prueba_for(1000000)
fin_for = time()
print(f"Tiempo con for: {fin_for - inicio_for} segundos")
print('\n')

inicio_while = time()
print("Iniciando prueba con while...")
prueba_while(1000000)
fin_while = time()
print(f"Tiempo con while: {fin_while - inicio_while} segundos")

###########----------------------------------------
print('\n**************************\n')
# Medir el tiempo de ejecución de una función con timeit
import timeit

declaracion_for = """
prueba_for_timeit(20)
"""

mi_setup = """
def prueba_for_timeit(numero):
    lista = []
    for i in range(1, numero + 1):
        lista.append(i)
    return lista
"""
duracion = timeit.timeit(declaracion_for,mi_setup,number=1000000)
print(duracion)


declaracion_while = """
prueba_while_timeit(20)
"""
mi_setup_while = """
def prueba_while_timeit(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
"""

duracion_while = timeit.timeit(declaracion_while,mi_setup_while,number=1000000)
print(duracion_while)
