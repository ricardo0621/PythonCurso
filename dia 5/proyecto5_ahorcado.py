from random import *

#se crea la lista con las palabras
lista_colores = ['rojo','azul','amarillo','blanco','negro']
nombre = input('hola cual es tu nombre: ')
print(f'hola {nombre.upper()} tienes 6 intentos para adivinar la palabra secreta.\nA continuacion se visualiza la longitud de la palabra.')

#funcion que elige palabra aleatoria de la lista
def color_aleatorio(a):
    palabra = choice(a)
    return list(palabra)

#funcion que reemplaza la palabra en lineas
def palabra_en_lineas(b):
    lista_reemplazada = []
    for i in b:
        lista_reemplazada.append("_")
    return lista_reemplazada

#funcion para pedir letra
def pedir_letra():

    while True: ## crea un bucle infinito hasta que llegue al return o break
        letra = input('por favor ingrese una letra,La cual considere que esta en la palabra: ')
        if letra.isalpha() and len(letra)==1:
            return letra.lower()
        else:
            print('Entrada inválida. Debes ingresar solo UNA letra.')

#funcion que valida si la letra esta en la palabra secreta
def validar_letra_en_palabra(letra, palabra):
    posiciones = []
    for indice,caracter in enumerate(palabra):
        if caracter == letra:
            posiciones.append(indice)
    return posiciones

#funcion reemplaza letra en las posciones
def reemplaza_letra(letra,posiciones,guiones):
    mi_lista = guiones

    for i in posiciones:
        if 0 <= i < len(mi_lista):
            mi_lista[i] = letra
    return mi_lista

# ==== Lógica del juego ====
color = color_aleatorio(lista_colores) ## variable de la palabra secreta
num_linea = palabra_en_lineas(color) ## variable de palabra secreta en lineas
print(" ".join(num_linea))
intentos = 0
letras_acertadas = []# lista que guarda las letras ingresadas

while intentos < 6 and '_' in num_linea:

    letra_usuario = pedir_letra()##  variable de la letra que ingresa el usuario
    if letra_usuario in letras_acertadas: # compara si la letra esta dentro de la lista
        print(f'ya usaste la letra {letra_usuario} intenta con otra')
        continue

    posiciones = validar_letra_en_palabra(letra_usuario,color)## variable que contiene las posciciones si tiene, sino retorna lista en blanco

    if posiciones: # esto es lo mismo que if len(posiciones) > 0:
        print(f'¡Bien! La letra {letra_usuario} está en la palabra.')
        num_linea = reemplaza_letra(letra_usuario,posiciones,num_linea)
        print(" ".join(num_linea))
        letras_acertadas.append(letra_usuario)
    else:
        print(f'la letra {letra_usuario} no esta en la palabra')
        print(f'llevas {intentos + 1} intentos de 6')
        intentos += 1

if '_' not in num_linea:
    print('\n¡Felicidades! Adivinaste la palabra:',"".join(color))
else:
    print('\n¡Has perdido. La palabra era:',"".join(color))