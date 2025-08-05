import os

'''
#obtener el directorio actual
#ruta = os.getcwd()

#para la busqueda de la ruta en python debe ser con \\
#cambiar de directorio, encontar archivos de otra ruta
#ruta = os.chdir('C:\\Users\\PC_WIN10\\Desktop\\UDEMY\\Curso Phyton\\Clase 6\\archivos')


#crear directorio o capeta
#ruta = os.makedirs('C:\\Users\\PC_WIN10\\Desktop\\UDEMY\\Curso Phyton\\Clase 6\\archivos\\otra')

#obtener por separados dos elementos
ruta = 'C:\\Users\\PC_WIN10\\Desktop\\UDEMY\\Curso Phyton\\Clase 6\\archivos\\alternativo.txt'
elemento = os.path.basename(ruta)
print(elemento)


#para eliminar carpetas
os.rmdir('C:\\Users\\PC_WIN10\\Desktop\\UDEMY\\Curso Phyton\\Clase 6\\archivos\\otra')


#archivo = open('alternativo.txt')
#print(archivo.read())
'''
#-------------------------------
# abrir un archivo desde una carpeta distinta
otro_archivo = open('C:\\Users\\PC_WIN10\\Desktop\\UDEMY\\Curso Phyton\\archivos_clase6\\alter_2.txt')
print(otro_archivo.read())







