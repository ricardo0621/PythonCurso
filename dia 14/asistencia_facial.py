import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime


# crear base de datos
ruta = 'Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])


print(nombres_empleados)

#codificar imagenes
def codificar(imagenes):

    #crear lista nueva
    lista_codificada = []

    #pasar imagenes a rgb
    for i in imagenes:
        i = cv2.cvtColor(i,cv2.COLOR_BGR2RGB)

        #codificar
        codificado = fr.face_encodings(i)[0]

        #agregar a la lista
        lista_codificada.append(codificado)

    #devolver lista codificada
    return lista_codificada


# registrar los ingresos
def registrar_ingresos(persona):
    f =open('registro.csv','r+')
    lista_datos = f.readlines()
    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registro.append(ingreso[0])

    if persona not in nombres_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona},{string_ahora}')



lista_empleados_codificada = codificar(mis_imagenes)

# tomar una imagen de camara web
captura = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#leer la imagen de la camara
exito, imagen = captura.read()

if not exito:
    print('no se ha podido tomar la foto')
else:
    #reconocer cara en foto
    cara_captura = fr.face_locations(imagen)

    #codificar cara capturada
    cara_captura_codificada = fr.face_encodings(imagen,cara_captura)

    #buscar coincidencias
    for fotocodif, fotoubi in zip(cara_captura_codificada, cara_captura):

        coindidencia = fr.compare_faces(lista_empleados_codificada,fotocodif)
        distancias = fr.face_distance(lista_empleados_codificada,fotocodif)

        print(distancias)

        indice_coincidencias = numpy.argmin(distancias)

        # mostrar coincidencias si las hay
        if distancias[indice_coincidencias] > 0.6:
            print('No coincide con ninguno de los empleados')
        else:
            # buscar el nombre del empleado
            nombre = nombres_empleados[indice_coincidencias]

            y1,x2,y2,x1 = fotoubi
            cv2.rectangle(imagen,(x1,y1),(x2,y2), (0,255,0),2)
            cv2.rectangle(imagen,(x1, y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(imagen,nombre, (x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255),2)

            #llamar funcion que registra el ingreso en archivo
            registrar_ingresos(nombre)


            #mostrar imagen obtenida
            cv2.imshow('Imagen web',imagen)
            print(f'bienvenido {nombre}')

            #mantener ventana abierta
            cv2.waitKey(0)























