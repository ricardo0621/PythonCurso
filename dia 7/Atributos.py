# se crea la clase
class Pajaro:

    ### metodo constructor, se pasan dos parametros, self, y otro con nombre cualquiera
    #def __init__(self,mi_parametro): este es un ejemplo pero se deberia escribir el atributo y parametro con el mismo nombre
        #self.atributo = mi_parametro

    alas = True

    def __init__(self,color,especie):
        self.color = color
        self.especie = especie


mi_pajaro = Pajaro('negro','tucan')

print(f'mi pajaro es un {mi_pajaro.color} y es de color {mi_pajaro.especie}')
print(mi_pajaro.alas)
print(Pajaro.alas)


#####################
class Casa:
    def __init__(self,color,cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos


casa_blanca = Casa('blanco',4)
print(f'mi casa es de color{casa_blanca.color} y tiene {casa_blanca.cantidad_pisos} pisos')

######################
class Cubo:
    caras = 6
    def __init__(self,color):
        self.color = color
cubo_rojo = Cubo('rojo')

########################
class Personaje:
    real = False
    def __init__(self,especie,magico,edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_potter = Personaje('Humano',True,17)
print(harry_potter.real,harry_potter.especie,harry_potter.magico)












class Personaje:
    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad


harry_potter = Personaje("humano", True, 17)
















