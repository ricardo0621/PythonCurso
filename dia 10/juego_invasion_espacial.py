import pygame
import random
import math
from pygame import mixer

## esto es para el ejecutable .exe
import sys
import os

def ruta_recurso(rel_path):
    """ Devuelve la ruta correcta para recursos dentro del .exe o en .py """
    try:
        base_path = sys._MEIPASS  # PyInstaller crea un directorio temporal
    except AttributeError:
        base_path = os.path.abspath(".")  # Cuando se ejecuta como .py
    return os.path.join(base_path, rel_path)
#############------------------------------


# inicializar pygame
pygame.init()

# crear una pantalla de 800x600 píxeles
pantalla = pygame.display.set_mode((800, 600)) # 800 ancho, 600 alto

# establecer el título de la ventana e icono
pygame.display.set_caption("Invasion Espacial") # Título de la ventana
#icono = pygame.image.load('ovni.png') # Cargar el icono de la ventana
icono = pygame.image.load(ruta_recurso('ovni.png')) # Cargar el icono de la ventana desde la ruta correcta
pygame.display.set_icon(icono) # Establecer el icono de la ventana
#fondo = pygame.image.load('fondo.jpg') # Cargar la imagen de fondo
fondo = pygame.image.load(ruta_recurso('fondo.jpg')) # Cargar la imagen de fondo desde la ruta correcta


# agregar música de fondo
#mixer.music.load('MusicaFondo.mp3') # Cargar la música de fondo
mixer.music.load(ruta_recurso('MusicaFondo.mp3'))
mixer.music.set_volume(0.3)
mixer.music.play(-1) # Reproducir la música de fondo en un bucle infinito

# variables del Jugador
#img_jugador = pygame.image.load('cohete.png') # Cargar la imagen del jugador
img_jugador = pygame.image.load(ruta_recurso('cohete.png')) #
jugador_x = 368  # Posición inicial del jugador en el eje X
jugador_y = 520  # Posición inicial del jugador en el eje Y
jugador_x_cambio = 0 # Variable para controlar el movimiento del jugador en el eje X
jugador_y_cambio = 0 # Variable para controlar el movimiento del jugador en el eje Y


# variables del enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8  # Cantidad de enemigos en el juego

for i in range(cantidad_enemigos):
    #img_enemigo.append(pygame.image.load('enemigo.png'))  # Cargar la imagen del enemigo
    img_enemigo.append(pygame.image.load(ruta_recurso('enemigo.png')))
    enemigo_x.append(random.randint(10, 736))  # Posición inicial del enemigo en el eje X
    enemigo_y.append(random.randint(10, 200))  # Posición inicial del enemigo en el eje Y
    enemigo_x_cambio.append(0.5)  # Variable para controlar el movimiento o velocidad del enemigo en el eje X
    enemigo_y_cambio.append(50)  # Variable para controlar el movimiento o velocidad del enemigo en el eje Y


#variable de la bala
balas = []
#img_disparo = pygame.image.load('bala.png') # Cargar la imagen del disparo
img_disparo = pygame.image.load(ruta_recurso('bala.png'))
bala_x = 0  # Posición inicial del disparo en el eje X
bala_y = 520  # Posición inicial del disparo en el eje Y
bala_x_cambio = 0  # Variable para controlar el movimiento del disparo en
bala_y_cambio = 3  # Velocidad del disparo en el eje Y
###bala_visible = False  # Variable para controlar si el disparo está visible o no

#puntaje
puntaje = 0  # Inicializar el puntaje del jugador
fuente = pygame.font.Font('freesansbold.ttf', 32)  # Cargar la fuente para el puntaje
texto_x = 10  # Posición del texto del puntaje en el eje X
texto_y = 10  # Posición del texto del puntaje en el eje Y


# Función para mostrar el texto de "GAME OVER"
fuente_final = pygame.font.Font('freesansbold.ttf', 64)  # Cargar la fuente para el texto de "GAME OVER"


# Función para mostrar el texto de "GAME OVER"
def texto_final():
    mi_fuente_final = fuente_final.render('GAME OVER', True, (255, 0, 0))  # Renderizar el texto de "GAME OVER"
    pantalla.blit(mi_fuente_final, (250, 250))  # Dibujar el texto de "GAME OVER" en la pantalla


# Función para mostrar el puntaje en la pantalla
def mostrar_puntaje(x, y):
    texto = fuente.render(f'puntaje: {puntaje}', True, (255, 255, 255))  # Renderizar el texto del puntaje
    pantalla.blit(texto, (x, y))  # Dibujar el texto del punt


# Función para dibujar al jugador en la pantalla
def jugador(x,y):
    pantalla.blit(img_jugador, (x, y))  # Dibujar la imagen del jugador en la pantalla

# Funcion para dibujar al enemigo en la pantalla
def enemigo(x,y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))  # Dibujar la imagen del enemigo en la pantalla

# Función para disparar
###def disparar(x, y):
   ### global bala_visible  # Usar la variable global para controlar la visibilidad del disparo
    ###bala_visible = True  # Hacer que el disparo sea visible
    ###pantalla.blit(img_disparo, (x + 16, y + 10))  # Dibujar el disparo en la pantalla


# funcion detectar colisión
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2,2) + math.pow(y_2 - y_1,2))  # Calcular la distancia entre dos puntos
    if distancia < 27:  # Si la distancia es menor que 27 (radio de colisión)
        return True  # Retornar True si hay colisión
    else:
        return False


#----------------------------------------------------------
# loop del juego
se_ejecuta = True # variable para controlar el bucle principal
while se_ejecuta:

    # Por ahora, solo llenamos la pantalla con un color de fondo
    #pantalla.fill((205, 144, 228))  # Color de fondo de la pantalla
    #jugador_x += 0.1 # Mover el jugador hacia la derecha lentamente automáticamente

    #imagen de fondo
    pantalla.blit(fondo, (0, 0))  # Dibujar la imagen de fondo en la pantalla


    # Manejar eventos
    for evento in pygame.event.get():

        # Evento de cierre de ventana
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # evento presionar teclas
        if evento.type ==  pygame.KEYDOWN:  # Evento de tecla presionada
            if evento.key == pygame.K_LEFT:  # Si se presiona la tecla izquierda
                jugador_x_cambio -= 1  # Mover el jugador hacia la izquierda y la velocidad que se representa con el numero
            if evento.key == pygame.K_RIGHT:  # Si se presiona la tecla derecha
                jugador_x_cambio += 1  # Mover el jugador hacia la derecha y la velocidad que se representa con el numero
            ####if evento.key == pygame.K_UP:
                ####jugador_y_cambio -= 1  # Mover el jugador hacia arriba
            ####if evento.key == pygame.K_DOWN:
                ####jugador_y_cambio += 1  # Mover el jugador hacia abajo
            if evento.key == pygame.K_SPACE:  # Si se presiona la barra espaciadora
                #sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala = mixer.Sound(ruta_recurso('disparo.mp3'))
                sonido_bala.play()
                ###nueva_bala = {"x": jugador_x,"y": jugador_y,"velocidad": -5}  # Crear un nuevo diccionario para la bala con su posición y velocidad}
                ###balas.append(nueva_bala)
                if puntaje >= 20:
                    # Tres balas: izquierda, centro y derecha
                    balas.append({"x": jugador_x - 30, "y": jugador_y, "velocidad": -5})
                    balas.append({"x": jugador_x + 30, "y": jugador_y, "velocidad": -5})
                    balas.append({"x": jugador_x, "y": jugador_y, "velocidad": -5})
                elif puntaje  >= 10:
                    # Dos balas: izquierda y derecha
                    balas.append({"x": jugador_x - 30, "y": jugador_y, "velocidad": -5})
                    balas.append({"x": jugador_x + 30, "y": jugador_y, "velocidad": -5})
                else:
                    # Una bala: centro
                    balas.append({"x": jugador_x, "y": jugador_y, "velocidad": -5})

                ###if not bala_visible:  # Si el disparo no está visible (solo se puede disparar una bala a la vez)
                   ### bala_x = jugador_x  # Establecer la posición del disparo en el eje X al mismo que el jugador
                   ### disparar(bala_x,bala_y)

        # evento de tecla liberada
        if evento.type == pygame.KEYUP:  # Evento de tecla liberada
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:  # Si se libera la tecla izquierda o derecha
                jugador_x_cambio = 0  # Detener el movimiento del jugador en el eje X
           #### if evento.key == pygame.K_UP or evento.key ==pygame.K_DOWN:
            #####    jugador_y_cambio = 0  # Detener el movimiento del jugador en el eje Y



    # Actualizar la posición del jugador
    jugador_x += jugador_x_cambio  # Actualizar la posición del jugador en el eje X
    ####jugador_y += jugador_y_cambio  # Actualizar la posición del jugador en el eje Y


    # Limitar el movimiento del jugador dentro de la pantalla
    if jugador_x <= 0:  # Si el jugador se sale por la izquierda
        jugador_x = 0  # Mantener al jugador en el borde izquierdo
    elif jugador_x >= 736:  # Si el jugador se sale por la derecha
        jugador_x = 736  # Mantener al jugador en el borde derecho
    ####if jugador_y <= 400:  # Si el jugador se sale por la parte superior
        ####jugador_y = 400  # Mantener al jugador en el borde superior
        ####elif jugador_y >= 530:  # Si el jugador se sale por la parte inferior
        ####jugador_y = 530  # Mantener al jugador en el borde inferior


    # movimiento del enemigo
    for i in range(cantidad_enemigos):

        # fin del juego
        if enemigo_y[i] > 480:  # Si el enemigo llega a una posición Y mayor a 250
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break


        enemigo_x[i] += enemigo_x_cambio[i]  # Actualizar la posición del enemigo en el eje X


        # mantener el movimiento del enemigo dentro de la pantalla
        if enemigo_x[i] <= 0:  # Si el enemigo se sale por la izquierda
            enemigo_x_cambio[i] = 0.5  # Cambiar la dirección del movimiento del enemigo
            enemigo_y[i] += enemigo_y_cambio[i] # Mover el enemigo hacia abajo


        elif enemigo_x[i] >= 736:  # Si el enemigo se sale por la derecha
            enemigo_x_cambio[i] = -0.5  # Cambiar la dirección del movimiento del enemigo
            enemigo_y[i] += enemigo_y_cambio[i] # Mover el enemigo hacia abajo

        # colision
        for bala in balas: # Verificar colisión entre la bala y el enemigo
            colision_bala_enemigo = hay_colision(enemigo_x[i], enemigo_y[i], bala["x"], bala["y"])
            if colision_bala_enemigo:
                #sonido_colision = mixer.Sound("Golpe.mp3")
                sonido_colision = mixer.Sound(ruta_recurso('Golpe.mp3'))
                sonido_colision.play()
                balas.remove(bala) # Eliminar la bala que colisionó con el enemigo
                puntaje += 1
                enemigo_x[i] = random.randint(0, 736)
                enemigo_y[i] = random.randint(20, 200)
                break

        enemigo(enemigo_x[i], enemigo_y[i], i) # Llamar a la función para dibujar al enemigo

        # colosión entre el disparo y el enemigo
      ###  colision = hay_colicion(enemigo_x[i], enemigo_y[i], bala_x, bala_y)  # Verificar si hay colisión entre el disparo y el enemigo
      ###  if colision:  # Si hay colisión
       ###     sonido_colicion = mixer.Sound('golpe.mp3')
        ###    sonido_colicion.play()
       ###     bala_y = 520  # Reiniciar la posición del disparo
       ###     bala_visible = False  # Hacer que el disparo no sea visible
       ###     puntaje += 1  # Incrementar el puntaje del jugador
       ###     enemigo_x[i] = random.randint(10, 736)  # Reiniciar la posición del enemigo en el eje X
        ###    enemigo_y[i] = random.randint(10, 200)  # Reiniciar la posición del enemigo en el eje Y

      ###  enemigo(enemigo_x[i], enemigo_y[i], i)  # Llamar a la función para dibujar al enemigo

    # movimiento bala
    for bala in balas:
        bala['y'] += bala['velocidad']  # Actualizar la posición de la bala en el eje Y
        pantalla.blit(img_disparo, (bala['x'] + 16, bala['y'] + 10))  # Dibujar la bala en la pantalla
        if bala['y'] < 0:  # Si la bala sale de la pantalla
            balas.remove(bala)


    # movimiento bala
   ### if bala_y <= -35:  # Si el disparo sale de la pantalla por arriba
    ###    bala_y = 500
     ###   bala_visible = False

   ### if bala_visible:  # Si el disparo está visible
     ###   disparar(bala_x, bala_y)  # Dibujar el disparo en la pantalla
     ###   bala_y -= bala_y_cambio


    jugador(jugador_x, jugador_y) # Llamar a la función para dibujar al jugador
    mostrar_puntaje(texto_x, texto_y)  # Llamar a la función para mostrar el puntaje en la pantalla


    # Actualizar la pantalla
    pygame.display.update()



