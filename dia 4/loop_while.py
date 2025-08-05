"""
moneda = 5
while moneda > 0:
    print(f'tengo {moneda} moneda')
    moneda = moneda - 1
else:
    print('no tengo mas dinero')

###############

respuesta = 's'

while respuesta == 's':
    respuesta = input('quieres seguir?(s/n) ')
else:
    print('gracias')
#####################

res = 's'
while res == 's':
    pass

print("hola")

################
n = input("tu nombre")

for xi in n:
    if xi == 'r':
        break
    print(xi)
########################
f = input("tu nombre")

for g in f:
    if g == 'r':
        continue
    print(g)
"""
numero = 50
while numero >= 0:
    if numero % 5 == 0:
        print(numero)
        numero -= 1
    else:
        numero -= 1
####################

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for i in lista_numeros:
    if i > 0:
        print(i)
    else:
        break


