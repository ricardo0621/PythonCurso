# caracteres especiales
#digito numerico \d
#caracter alfa \w
# caracteres especiales \s en blanco
#caracteres especiales \D # no numerico
#caracteres especiales \W # no alfanumerico
#caracteres especiales \S # no en blanco


import re

texto = 'si necesitas ayuda, llama al (123)-456-7890 o envía un correo ayuda'
patron = 'ayuda'

busqueda = re.search(patron, texto)# busca el patron en el texto
busqueda = re.findall(patron, texto)  # encuentra todas las coincidencias del patron en el texto
print(busqueda)#
print('***')
print(len(busqueda))

for hallazgo in  re.finditer(patron,texto):
    print('//////')
    print(hallazgo.group())  # Imprime cada coincidencia encontrada
    print(hallazgo.start())  # Imprime la posición de inicio de la coincidencia
    print(hallazgo.end())    # Imprime la posición final de la coincidencia
    print(hallazgo.span())   # Imprime un tuple con las posiciones de inicio y fin


#---------------------------------------------
def verificar_email(email):
    patron = r'@\w+\.com' # Patrón para verificar si el email termina con @algo.com
    verificar = re.search(patron, email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")
verificar_email('ricardo@hotmail.com.br')

#####3------------------------------
print('\n')

texto_2 = 'llama al (123)-456-7890 o envía un correo'
patron_2 = r'\(\d{3}\)-\d{3}-\d{4}'  # Patrón para un número de teléfono en formato 123-456-7890
#patron_2 = r'\(\d\d\d\)-\d\d\d-\d\d\d\d'  # Otra forma de definir el patrón
patron_compilado = re.compile(r'(\(\d{3}\))-(\d{3})-(\d{4})')  # Compila el patrón para mejorar el rendimiento en búsquedas repetidas

busqueda_2 = re.search(patron_2, texto_2)# busca el patrón en el texto
busqueda_compilado = re.search(patron_compilado,texto_2)  # Busca el patrón compilado en el texto

print(busqueda_2.group())# Imprime la coincidencia encontrada
print(busqueda_compilado.group(2))

#####3------------------------------
#verificador de clave si cumple con el patrón lo muesta
print('\n')

clave = input('ingrese una clave: ')
patron_clave = r'\D{1}\w{7}' # Patrón para una clave que comienza con un carácter no numérico seguido de 7 caracteres alfanuméricos

cheque_clave = re.search(patron_clave, clave)  # Busca el patrón en la clave ingresada

print(cheque_clave)



#####------------------------------
print('\n')

frase = 'no atendemos los lunes por la tarde'
buscar = re.search(r'lunes|martes',frase)# busca si hay coincidencia con lunes o martes
b2 = re.search(r'.demos',frase)  # busca si hay coincidencia con cualquier carácter seguido de demos
b3 = re.search(r'...emos',frase)  # busca si hay coincidencia con demos precedido de cualquier carácter
b4 = re.search(r'demos....',frase)  # busca si hay coincidencia con demos seguido de cualquier carácter
b5 = re.search(r'^\D',frase) # busca si la frase comienza con un carácter no numérico
b6 = re.search(r'\D$',frase) # busca si la frase termina con un carácter no numérico
b7 = re.findall(r'[^\s]+',frase)

print(buscar.group())
print(b2)
print(b3.group())
print(b4.group())
print(b5)
print(b6)
print(''.join(b7))



