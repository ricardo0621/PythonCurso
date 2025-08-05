menor = min(58,59,35,65,45)
mayor = max(98,59,63,4)
print(menor)
############

lista = [58,59,35,65,45]
print(max(lista))
print(f'el menor es {min(lista)} y el mayor es {max(lista)}')
##########

nom = ['juan','alicia','carlos']
print(min(nom))
#######################

nombre = 'Carlos'
print(min(nombre.lower()))
############

dic = {'c1':45,'c2':42}
print(min(dic.values()))

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)
print(edad_minima,ultimo_nombre)