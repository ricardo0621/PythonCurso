from pathlib import Path, PureWindowsPath

#PureWindowsPath esta es otra lib para mostrar ruta para window

# de esta manera ya podemos abrir y leer un archivo, solo con pathlib
carpeta = Path('/Users/PC_WIN10/Desktop/UDEMY/Curso Phyton/archivos_clase6/alter_2.txt')
'''
print(carpeta.read_text())## para leer el textos del archivo
print(carpeta.name)##trae el nombre del archivo
print(carpeta.suffix)##trae la extencion del archivo
print(carpeta.stem)## trae solo el nombre sin la extencion
'''

#sabe si el archivo existe
if not carpeta.exists():
    print('este archivo no existe')
else:
    print('genial,existe')

