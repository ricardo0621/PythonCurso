import bs4
import requests

resultado = requests.get('https://www.vendetunave.co/vehiculos/carrosycamionetas/Lexus/LX/Lexus-LX-700h-Luxury-2025-97835')
#print(resultado.text) # Imprime el contenido HTML de la página web

sopa = bs4.BeautifulSoup(resultado.text, 'lxml') # Crea un objeto BeautifulSoup para analizar el HTML de la página web
#print(sopa.select('title')[0].getText()) # Imprime el título de la página web

parrafo_especial = sopa.select('p')[16].getText() # Selecciona el cuarto párrafo de la página web
#print(parrafo_especial) # Imprime el texto del primer párrafo con clase "special"

columna = sopa.select('.col-md-11 p') # Selecciona todos los párrafos dentro de la columna con clase "col-md-11"
#columna = [print(p.getText()) for p in columna]  # Extrae el texto de cada párrafo
# Imprime el texto de cada párrafo en la columna
#print(columna)


#capturar imagenes
imagenes = sopa.select('img') # Selecciona todas las imágenes de la página web
imagen_con_clases = sopa.select('.styles_Image__5J3mo') # Selecciona las imágenes con la clase específica 'styles_Image__5J3mo'
for i in imagenes:
    print(i)

print('\n')

for i in imagen_con_clases:
    print(i)

print('\n')

solo_url_imagenes = sopa.select('.styles_Image__5J3mo')[0]['src']  # Obtiene la URL de la primera imagen con la clase 'styles_Image__5J3mo'
print(solo_url_imagenes)  # Imprime la URL de la imagen

print('\n')

imagen_camioneta_1 = requests.get(solo_url_imagenes)# Descarga la imagen de la URL obtenida
f = open('camioneta_1.jpg', 'wb')  # Abre un archivo en modo escritura binaria
# f = open('c:\\...camioneta_1.jpg', 'wb') #opcionalmente, puedes especificar una ruta completa para guardar la imagen
f.write(imagen_camioneta_1.content)  # Escribe el contenido de la imagen en el archivo
f.close()  # Cierra el archivo