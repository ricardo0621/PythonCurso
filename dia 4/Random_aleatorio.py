from random import *

aleatorio = randint(1,50)
print(aleatorio)

ale = round(uniform(1,6),2)
print(ale)

a = random()###da una fraccion de un entero entre 0 y 1
print(a)

colores = ['azul','rojo','blanco']
b = choice(colores)# para aleatorio con string
print(b)

numero = list(range(5,50,5))
shuffle(numero)##mezcla los numeros de una lista, no se puede usar con string
print(numero)
