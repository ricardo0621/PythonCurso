class Pajaro:

    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self,metros):
        print(f'el pajaro vuela {metros} mts')


mi_pajaro = Pajaro('azul','tucan')
mi_pajaro.piar()
mi_pajaro.volar(50)

x = Pajaro('llll','fdgdfgdfgh')
x.volar(4000000)

#################
class Perro:

    def ladrar(self):
        print('guau')

pluto = Perro()
pluto.ladrar()

##########################
class Alarma:
    def postergar(self,cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")