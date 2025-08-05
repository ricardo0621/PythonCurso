""""
lista = ['a','b','c']
for i,x in enumerate(lista):
    print(i,x)
####################


for indice,item in enumerate(range(50,55)):
    print(indice,item)
#################################


mis_taples = list(enumerate(lista))
print(mis_taples)
print(mis_taples[2][1])
#############################


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')
###########################


lista_indices = list(enumerate("Python"))
print(lista_indices)

lista_indices = list("Python")
for indice,elemento in enumerate(lista_indices):
    print(indice,elemento)
############################



lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for i, nombre in enumerate(lista_nombres):
    if nombre[0] == "M":
        print(i)
"""

l = 'juan'
for i, x in enumerate(l):
    if x[0] == "n":
        print(i)
















