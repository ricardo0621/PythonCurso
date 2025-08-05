##el siguiente codigo es para adivinar cual es el palito mas largo
from random import shuffle
#pasos:
#      crear lista inicial
palitos = ['-','--','---','----']

###    mezclar palitos
def mezclar (lista):
    shuffle(lista)
    return lista

###    pedirle intento
def probar_suerte():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input('elige un numero del 1 al 4: ')

    return int(intento)

#####comprobar intento
def chequear_intento(lista,intento):
    if lista[intento-1] == '-':
        print('a lavar PLATOS')
    else:
        print('te has salvado')

    print(f'te ha tocado {lista[intento-1]}')

###aca ya se realiza el envio de informacion para las funciones
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)

