class Animal:
    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('este animal ha nacido')

    def hablar(self):
        print('este animal emite un sonido')


# nueva clase que hereda de Animal
class Pajaro(Animal):

    def __init__(self,edad,color,altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print('pio')

    def volar(self,metros):
        print(f'el pajaro vuela {metros}metros')





piolin = Pajaro(3,'amarillo',500)
piolin.nacer()
piolin.hablar()
piolin.volar(100)

mi_animal = Animal(5,'negro')

######3****************************************************
#ejemplo 2 para herencia multiple
print('\n****************************************\n')


class Padre:
    def hablar(self): #estos son metodos
        print('ya puedo decir hola')

class Madre:
    def reir(self):
        print('ja ja ja')

    def hablar(self):
        print('que tal')

class Hijo(Padre,Madre):#una clase puede heredar mas de una clase
    pass

class Nieto(Hijo):
    pass


mi_nieto = Nieto()
mi_nieto.hablar()#este se va a imprimir dependiendo del orden que esta heredando ejemplo primero esta Padre
mi_nieto.reir()



















