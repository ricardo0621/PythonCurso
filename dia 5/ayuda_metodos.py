caracteres = ',:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#'
res = caracteres.lstrip(",:#_")####para quitar los caracters a la izquierda
print(res)
######################

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,"naranja")##para insertar en una pos especifica
print(frutas)
####################

##la funcion isdisjoint() solo funciona con sets y es para mirar si dos conjuntos no tienen elementos en comun
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)
