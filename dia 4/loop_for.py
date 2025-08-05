nombre = ['a','b','c']

for l in nombre:
    num_l = nombre.index(l)+1
    print(f"letra {num_l}: {l}")
    #print("letra: " + l)
######################

lista = ['laura','ricardo','juan','carlos','luis']

for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print(f'nombre que no comienza con l: {nombre}')
############################

numeros = [1,2,3,4,5]
mi_valor = 0
for n in numeros:
    mi_valor = mi_valor + n
    print(mi_valor)###si el print esta dentro del for imprime cada ciclo
print(mi_valor)### si el print esta fiera del for imprime el acumulado de la variable
#######################

palabra = 'python'

for i in palabra:
    print(i)
#########################

for x in [[1,2],[3,10],5]:
    print(x)
##########################

dic = {'c1':'a','c2':'b','c3':'c'}

for a,b in dic.items():
    print(a,b)
###############################

lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_pares = 0
suma_impares = 0

for i in lista_numeros:
    if (i % 2) == 0:
        suma_pares = suma_pares + i

    elif i % 2 == 1:
        suma_impares = suma_impares + i

print(suma_pares)
print(suma_impares)

""""
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
 
suma_pares = 0
 
suma_impares = 0
 
for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero
"""



