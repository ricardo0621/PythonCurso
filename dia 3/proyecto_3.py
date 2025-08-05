texto = input("por favor ingresar un texto: ")
letras = input("por favor ingrese tres letras: ")
texto_min =texto.lower()
separador_texto = texto_min.split()
lista_letra= list(letras.lower())

cantidad_letras1 = texto_min.count(lista_letra[0])
cantidad_letras2 = texto_min.count(lista_letra[1])
cantidad_letras3 = texto_min.count(lista_letra[2])


#inicio_letra = texto_min[0]
#fin_letra = texto_min[-1]
######### punto 1
print("\n")
print(f"la primera letra hay {cantidad_letras1} cantidades \nla segunda letra hay {cantidad_letras2} cantidades \nla tercera letra hay {cantidad_letras3} cantidades")

########## punto 2
print("\n")
print(f"en el texto hay {len(separador_texto)} palabras")

########## punto 3
print("\n")
print(f"la letra inicial es: {texto_min[0]} y la letra final del texto es {texto_min[-1]}")

######### punto 4
print("\n")
print("texto invertido")
separador_texto.reverse()
texto_reverso = ' '.join(separador_texto)
print(texto_reverso)

########## punto 5
buscador = 'python' in texto_min
dic = {True:'si',False:'no'}
print("\n")
print(f"la palabra que busca esta en el texto ? {dic[buscador]}")




