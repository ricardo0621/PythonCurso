class Animal:
    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        return 'este animal ha nacido'


class Pajaro(Animal):
     pass
class Perro(Animal):
    pass


piolin = Pajaro(2,'amarillo')
print(f'{piolin.nacer()} con una eda de {piolin.edad} años y de color {piolin.color}')

hanna = Perro(12,'negro-blanco')
print(f'{hanna.nacer()} con una eda de {hanna.edad} años y de color {hanna.color}')


##----------------

class Vehiculo:
    def acelerar(self):
        print('esto es acelerar')

    def frenar(self):
        print('esto es frenar')


class Automovil(Vehiculo):
    pass

vols = Automovil()
vols.frenar()
vols.acelerar()

