from collections import Counter

numeros = [1,1,1,1,2,2,3,4,4]
print(Counter(numeros))  # Cuenta la frecuencia de cada elemento en la lista
print(Counter(numeros).most_common(2))  # Muestra los dos elementos más comunes


print('\n')
print(Counter('mississippi'))  # Cuenta la frecuencia de cada letra en la cadena
print(Counter('mississippi').most_common(2))  # Muestra las dos letras


print('\n')
frase = 'al pan pan , al vino vino'
palabras = frase.split()  # Divide la frase en palabras
print(Counter(palabras))  # Cuenta la frecuencia de cada palabra


print('\n')
serie = Counter([1,1,1,1,1,2,2,2,2,3,3,4])  # Muestra la frecuencia de cada elemento en la serie
print(serie.most_common(2))  # Muestra los dos elementos más comunes en
print(list(serie)) # Muestra los elementos únicos en la serie


print('\n')
from collections import defaultdict
# defaultdict permite crear un diccionario con un valor por defecto
mi_dic = defaultdict(lambda: 'no existe')  # crea un diccionario con valor por defecto 'no existe'
mi_dic.update({'uno': 'verde', 'dos': 'rojo', 'tres': 'azul'}) # actualiza el diccionario con algunos valores
mi_dic['cuatro'] = 'amarillo'  # agrega un nuevo elemento al diccionario

print(mi_dic['cinco'])  # Imprime 'no existe' porque 'cuatro' no está en el diccionario)
print(mi_dic['dos'])


print('\n')
from collections import namedtuple
# namedtuple permite crear una tupla con nombre para acceder a sus elementos por nombre
Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])  # crea una tupla con nombre
ariel = Persona('Ariel', 1.75, 70)  # crea una instancia de la tupla con valores
print(ariel)  # Imprime la tupla con los valores
print(ariel.nombre)  # Accede al nombre de la persona
print(ariel.altura)  # Accede a la altura de la persona
print(ariel[2])  # Accede al peso de la persona usando el índice


print('\n')
from collections import deque
# deque es una lista doblemente enlazada que permite agregar y eliminar elementos de ambos extremos
# Lista inicial de ciudades
ciudades = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]

# Crear la deque con los elementos iniciales
lista_ciudades = deque(ciudades)

# Agregar un elemento por la izquierda
lista_ciudades.appendleft("Ámsterdam")

# Agregar un elemento por la derecha
lista_ciudades.append("Lisboa")

print(lista_ciudades)



lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])