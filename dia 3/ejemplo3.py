"""
mi_texto = "esta es una prueba"
#resultado = mi_texto[5]
#resultado = mi_texto.index("a",5)#este es para buscar la a a partir de la quinta poscicion
resultado = mi_texto.rindex("a")#este devuelve el vlor de derecha a izq
print(resultado)
#########################

texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5]#extraer desde pos 2 hasta pos 5
fragmento = texto[2:]#extraer desde pos 2 hasta final
fragmento = texto[:5]#extraer hasta pos 5
fragmento = texto[2:10:2]#extraer desde pos 2 hasta pos 10 y coger de dos en dos
fragmento = texto[::3]#busca todos pero saltanto de tres en tres
fragmento = texto[::-1]#este es para ver las frases desde atras a adelante
print(fragmento)
#################################

texto = "Este es el Texto de ricardo"
res = texto.upper()#para convertir a mayuscula
res = texto[2].upper()#para convertir a mayuscula la poscicion
res = texto.lower()#para convertir a minuscula
res = texto.split()#para separa por lista por comillas simples el texto
res = texto.split("e")#para separar deacuerdo al caracter
print(res)
############################

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])#este es para unir deacuerdo a lo que tenga la variable
print(e)
#######################

texto = "Este es el texto de Ricardo"
res = texto.find("es")##para buscar
res = texto.replace("Ricardo","el mejor")##este es para reemplazar por lo que quieras
print(res)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
print(frase.replace("difícil", "fácil").replace("mala", "buena"))##para reemplazar varias cosas en una frase
#######################

##n= """mil pequeños peces blancos
como si hirviera
el color del agua"""
print(n)
print("agua" in n)
print("agua" not in n)
print(len(n))
#########################
"""

























