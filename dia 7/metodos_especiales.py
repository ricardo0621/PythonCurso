class CD:

    def __init__(self,autor,titulo,canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f'albun: {self.titulo} de {self.autor}'

    def __len__(self):
        return self.canciones

    def __del__(self):
        print('se ha eliminado el cd')

mi_cd = CD('pink floyd','the wol',24)
print(mi_cd)
print(len(mi_cd))# este solo va a imprimir las cantidad de lo que este en la funcion __len
print(mi_cd.titulo)

#del mi_cd #es para eliminar una instancia
print('********************\n')
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"{self.nombre} ha sido creada.")

    def __del__(self):
        print(f"{self.nombre} ha sido destruida.")

p = Persona("Carlos")
del p  # Llama al destructor __del__

#########-------------------------------
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}",de {self.autor},{self.cantidad_paginas} paginas'

mi_libro = Libro('callate','mario',300)
print(mi_libro)  # Imprime el resultado de __str__

