from random import *
nombre_jugador = input('cual es tu nombre: ')
print(f"""bueno,{nombre_jugador} he pensado un número entre 1 y 100,
y tienes solo ocho intentos para adivinar cuál crees que es el número""")
num_aleatorio = randint(1,100)
vidas = 0
numero_usuario = 0

while vidas < 8:
    numero_usuario = int(input('cual es tu numero: '))
    vidas += 1

    if numero_usuario not in range(1,101):
        print('tu numero no esta ene l rango de 1 a 100')
    elif numero_usuario < num_aleatorio:
        print(f'su respuesta es incorrecta el numero que eligio es Menor al secreto')
        #continue
    elif numero_usuario > num_aleatorio:
        print(f'su respuesta es incorrecta el numero que eligio es Mayor al secreto')
        #continue
    elif numero_usuario == num_aleatorio:
        print(f'has ganado {nombre_jugador} has adivinado en {vidas} intentos')
        break###interrumpe el while en general para realizar otra cosa cuando se acabe el while

if num_aleatorio != numero_usuario:
    print(f'perdiste el numero secreto es: {num_aleatorio}')


