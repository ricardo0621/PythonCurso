# A = escribir a partir del ultimo punto. del archivo, W = es para sobreescribir

#archivo = open('prueba.txt','r')# cuando no escribimos el segundo parametro se entiende que es solo lectura 'r'
#archivo = open('prueba1.txt','w')# con la w va a sobre escribir todo lo que tenia en el archivo o crea un nuevor archivo

###archivo.write('''soy el nuevo texto
#este es un nuevo
#salto de linea''')# esto es para escribir en el archivo

#archivo.writelines(['hola','esta','es','una','prueba'])

archivo = open('prueba1.txt','a')
archivo.write('bienvenido')


archivo.close()

#######################################
archivo = open('mi_archivo.txt','w')
archivo.write("Nuevo texto")

archivo.close()
archivo = open("mi_archivo.txt", "r")
print(archivo.read())

## Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

registro = open("registro.txt", "a")
for item in registro_ultima_sesion:
    registro.writelines(item + '\t')

registro.close()
registro = open("registro.txt", "r")
print(registro.read())
