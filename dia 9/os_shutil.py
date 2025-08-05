import os
print(os.getcwd()) # Muestra el directorio de trabajo actual

archivo = open('curso.txt', 'w')  # Crea un archivo llamado curso.txt
archivo.write('Curso de Python')  # Escribe en el archivo
archivo.close()  # Cierra el archivo

print(os.listdir()) # Muestra los archivos en el directorio actual


# shutil es una libreria que nos permite mover, copiar, eliminar archivos y directorios
import shutil
nueva_ruta = "C:\\Users\\PC_WIN10\\Desktop\\UDEMY\\Curso Phyton\\Clase 9"  # Define la nueva ruta
shutil.move('curso.txt',  nueva_ruta) # Mueve el archivo curso.txt al escritorio

import send2trash # send2trash es una libreria que nos permite enviar archivos a la papelera de reciclaje
send2trash.send2trash(nueva_ruta)  # Envía el archivo curso.txt a la papelera de reciclaje


print(os.walk("C:\\Users\\PC_WIN10\\Desktop\\UDEMY\\Curso Phyton\\Clase 9")) # Muestra los archivos y directorios en la ruta especificada
ruta = "C:\\Users\\PC_WIN10\\Desktop\\UDEMY\\Curso Phyton\\Clase 9"
for carpeta, subcarpetas, archivos in os.walk(ruta): # Recorre la ruta especificada
    print(f'en la carpeta: {carpeta}') # Muestra la carpeta actual
    print(f'subcarpetas son:')
    for sub in subcarpetas:# Muestra las subcarpetas en la carpeta actual
        print(f'\t{sub}')
    print(f'archivos son:')
    for arch in archivos:# Muestra los archivos en la carpeta actual
        if arch.startswith('2015'):# Filtra los archivos que comienzan con '2015'
            print(f'\t{arch}') # Muestra los archivos que comienzan con '2015'
    print('\n')


