import os
from pathlib import Path
import re
from leer_archivos import ruta
import datetime
import timeit
import math



ruta_carpetas = ruta /'Mi_Gran_Directorio' # Define la ruta del directorio donde estan todos los archivos
patron_codigo = re.compile(r'N\D{3}-\d{5}') # Define el patrón para buscar códigos en los archivos
lista_resultados = []  # Lista de tuplas (archivo, [códigos encontrados])
hoy = datetime.date.today()


def encontrar_codigos_y_archivos(ruta):
    for carpeta_actual, subcarpetas, archivos in os.walk(ruta):
        if archivos:
            for i in archivos:
                archivo_ruta = Path(carpeta_actual) / i  # Construye la ruta completa del archivo
                try:
                    with open(archivo_ruta, 'r', encoding='utf-8') as f:
                        contenido = f.read()
                        codigos_encontrados = patron_codigo.findall(contenido)  # Encuentra todos los códigos en el contenido del archivo
                        if codigos_encontrados:  # Si se encontraron códigos en el archivo
                            lista_resultados.append((archivo_ruta.name, codigos_encontrados)) # Agrega el archivo y los códigos encontrados a la lista de resultados
                except Exception as e:
                    print(f"⚠️ Error leyendo {i}: {e}")


def iniciar():
    print('cristian baboso rebaboso')

    print('📅 Fecha de búsqueda: ',hoy.strftime('%d/%m/%y')) # Imprime la fecha de búsqueda en formato día/mes/año
    print('ARCHIVOS\t\tNRO. SERIE\n--------\t\t----------') # Imprime el encabezado de la tabla
    encontrar_codigos_y_archivos(ruta_carpetas)
    cantidad_codigos = [] # Lista para almacenar todos los códigos encontrados
    if lista_resultados:
        for archivo, codigos in lista_resultados:
            print(f"{archivo}\t{', '.join(codigos)}")
            cantidad_codigos.extend(codigos) # Agrega los códigos encontrados a la lista de cantidad_codigos
    else:
        print('❌ No se encontraron archivos con códigos.')
    print(f'Cantidad de numeros encontrados: ',len(cantidad_codigos))




if __name__ == "__main__":
    duracion = timeit.timeit(iniciar, number=1)# Mide el tiempo de ejecución de la función iniciar
    print(f'⏱️ Duración de la ejecución: {math.ceil(duracion):.4f} segundos') # Mide y muestra la duración de la ejecución de la función iniciar






