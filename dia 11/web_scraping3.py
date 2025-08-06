
# obtener todos los titulos de los libros que tengan mas de 3 o 4 estrellas
import bs4
import requests

# crear una url sin numero de pagina
url = "https://books.toscrape.com/catalogue/page-{}.html"


#lista de titulos con 4 o 5 estrellas
titulos_rating_alto = [] # Inicializa una lista para almacenar los títulos de los libros con 4 o 5 estrellas

#iterar por las paginas del catalogo
for pagina in range(1, 51):  # Itera desde la página 1 hasta la 50

    #crear sopa para cada pagina
    url_pagina = url.format(pagina) # Formatea la URL con el número de página actual
    respuesta = requests.get(url_pagina)  # Realiza una solicitud HTTP a la URL de la página actual
    sopa = bs4.BeautifulSoup(respuesta.text, 'lxml')  # Parsear el contenido HTML de la página web

    #buscar libros en la pagina
    libros = sopa.select('.product_pod')  # Selecciona todos los elementos con la clase 'product_pod', que representan los libros en la página

    #iterar por los libros encontrados
    for libro in libros:  # Itera sobre cada libro encontrado en la página

        #chequear si tiene 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) > 0 or len(libro.select('.star-rating.Five')) > 0:
            # Si el libro tiene 4 o 5 estrellas, extrae el título
            titulo = libro.select('a')[1]['title']

        #agregar libro a lalista
            titulos_rating_alto.append(titulo)

# Imprimir los títulos de los libros con 4 o 5 estrellas
print("Títulos de libros con 4 o 5 estrellas:")
for titulo in titulos_rating_alto:
    print(titulo)  # Imprime cada título de libro con 4 o 5 estrellas
