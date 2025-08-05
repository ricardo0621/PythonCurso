class Pajaro:

    alas = True

    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio')

    def volar(self,metros):
        print(f'el pajaro vuela {metros} mts')
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f'ahora el pajaro es {self.color}')

    ## estos son metodos de clase
    @classmethod
    def poner_huevos(cls,cantidad):
        print(f'puso {cantidad} huevos')
        cls.alas = False
        print(Pajaro.alas)

    #### estos son lo metodos staticos, estos no pueden acceder a los atributos de la clase ni a los de las intancia
    @staticmethod
    def mirar():
        print('el pajaro mira')






piolin = Pajaro('amarillo','canario')
piolin.volar(70)
piolin.alas = False
print(piolin.alas)
####
print('******************')
#los metosod de clase no necesitan una instancia para poder llamarlos
Pajaro.poner_huevos(5)

print('******************')
Pajaro.mirar()

##-------------------
print('******************')
class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

Mascota.respirar()
##-------------------
class Jugador:
    vivo = True

    @classmethod
    def revivir(cls):
        cls.vivo = False
        print(f'usted esta vivo {cls.vivo}')


Jugador.revivir()

#------------------------------------

print('******************')

class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad -= 1

p = Personaje(4)
print(f"esta es la cantidad de flechas {p.cantidad}")
p.lanzar_flecha()
print(f"Después de 1 lanzamiento: {p.cantidad}")
p.lanzar_flecha()
print(f"Después de 2 lanzamiento: {p.cantidad}")
p.lanzar_flecha()
print(f"Después de 3 lanzamiento: {p.cantidad}")
p.lanzar_flecha()
print(f"Después de 4 lanzamiento: {p.cantidad}")
p.lanzar_flecha()
print(f"Después de 5 lanzamiento: {p.cantidad}")











