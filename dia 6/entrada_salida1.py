mi_archivo = open('prueba.txt')
'''
print(mi_archivo.read())# leer el archivo

una_linea = mi_archivo.readline()# para ver una linea
print(una_linea)

una_linea = mi_archivo.readline()# si vuelve a invocar coge la siguiente linea 2
print(una_linea.rstrip())#imprime sin el salto de linea

una_linea = mi_archivo.readline()# guarda la linea 3
print(una_linea)

for i in mi_archivo:   # recorre cada linea e imprime lo que dese dependiendo de las lineas
    print("aqui dice: ",i)
'''
todas = mi_archivo.readlines()# captura todas las linea en una lista se sugiere solo para archivos pequeños
todas.pop() ## eliminar la ultima
print(todas)


mi_archivo.close() # serecomienda cerrar el archivo despues de leerlo read
