#{} []
""""
mi_set = set([1,2,3,4,5])#debe tener encerrado en algun simbolo
#otro_set = {1,2,3} # de esta manera tambn se pede declara un set
##en los set no se repiten los valores porque los elimina
#no se pueden poner listas adentro del set
#si acepta tables mi_set = set([1,2,3,(2,3,4),4,5])
print(len(mi_set))
print(2 in mi_set)
print(mi_set)
print(type(mi_set))
#####################

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)
###############################
"""
s1 = {1,2,3}
s1.add('hola')
s1.remove(3)
s1.discard(6)

print(s1)
sorteo = s1.pop()#eliminia aleatoreamente es util como para un sorteo
print(sorteo)

s1.clear()##para limpiar el set
print(s1)





