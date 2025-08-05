class Vaca:
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice muuu')

class Oveja:
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice beee')

vaca1 = Vaca('aurora')
obeja1 = Oveja('nube')

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
'''
animales = [vaca1,obeja1]

for animal in animales:
    animal.hablar()
'''
###--------------------
print("\n*************************\n")

class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

mago1 = Mago()
arquero1 = Arquero()
samurai1 = Samurai()

personajes = [arquero1,mago1,samurai1]

for i in personajes:
    i.atacar()
