#{} []
mi_tuple = (1,2,3,4)
t = (5,6.7,'ff')

print(mi_tuple[1])
print(type(mi_tuple))

taple2= (2,3,4,(3,7))#se puede crear taple dentro e taple
#taple2 = list(taple2)#convertirlo tipo lista
print(taple2[3][1])#para mostrar el taple dentro del table y mostrar el de la pos

t = 1,2,3
x,y,z = t
print(x,y,z)

dd = (1,2,3,4,2)
print(dd.count(2))#cuenta cuantas veces aparece el valor consultado
print(dd.index(3))#buscar cual es la pos del valor consultado