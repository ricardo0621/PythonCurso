##################esta es la manera mas larga
palabra = 'python'
lista = []
for i in palabra:
    lista.append(i)####append es para agregar a la lista
print(lista)

###########esta e la mas eficiente

p = 'ricardo'
lis = [i for i in p]
print(lista)


l = [i for i in 'carlos']
print(l)
######################


lis2 = [num for num in range(1,50,3)]
print(lis2)

lis3 = [x/3 for x in range(1,50,3)]
print(lis2)

lis5 = [f for f in range(1,50) if f*2 > 40]
print(lis5)


lis7 = [f if f*2 > 10 else 'no' for f in range(1,10) ]
print(lis7)

###############
pies = [10,20,30,40,50]
metros = []
for i in pies:
    m = i*3.281
    metros.append(m)
print(metros)
###################esta es la version resumida

foot = [10,20,30,40,50]
mt = [x * 3.281 for x in foot]
print(mt)
##################

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [i for i in valores if i%2==0]
print(valores_pares)

