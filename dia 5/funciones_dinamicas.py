
def chequear_numero(numero):
    return numero in range(100,1000)

suma = 586 + 63
res = chequear_numero(suma)
print(res)
##############################

def chek_3_cifras(lista):
    lista_3_cifras = []
    for i in lista:
        if i in range(100,1000):
            lista_3_cifras.append(i)## llenar la lista
        else:
            pass## esto significa que no pase nada que siga
    return lista_3_cifras

resultado = chek_3_cifras([555,99,600])
print(resultado)
################################

####opcion 1 este me dice si todos son positivos los elementos de una lista, llenando la lista para mas adelante
def todos_positivos(numeros):
    lista_numeros = []
    for i in numeros:
        if i >= 0:
            lista_numeros.append(i)#llenar la lista
        else:
            return False

    return True


envio = todos_positivos([1, 2, 3, 4])
print(envio)
#############################
###opcion 2 para los numeros positivos de una lista
def todos_positivos(numeros):
    for i in numeros:
        if i >= 0:
            pass
        else:
            return False

    return True
lif = todos_positivos([1, 2, 3, -4])
print(lif)




###########################

####este me dice si todos son positivos los elementos de una lista
lista_numeros = [1, -50, 502, -5000, 755, 600, 33, 61]
def todos_positivos(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return False

    return True
###########################################

####este suma los valores del rango de numeros establecidos en la lista
lista_numeros = [1, 50, 500, 5000, 750, 600]

def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero in range(1, 1000):
            suma += numero
        else:
            pass
    return suma
###############################

####este suma los valores del rango de numeros establecidos en la lista
lista_numeros = [1,2,3,-5]
def suma_menores(lista_numeros):
    suma = 0
    for i in lista_numeros:
        if i > 0 and i<1000:
            suma += i
    return  suma

l = suma_menores(lista_numeros)
print(l)


####este es un contador de pares que tiene una lista
lista_numeros = [1,2,3,4,6]
def cantidad_pares(lista_numeros):
    contador = 0
    for i in lista_numeros:
        if i%2 == 0:
            contador += 1
    return contador

x = cantidad_pares(lista_numeros)
print(x)
#######################################

##este codigo toma un tuple y valida el valor mas caro en este caso es de varios cafes
precios_cafe = [('americano',3000),('late',4000),('milo',5500)]

def cafe_mas_caro(precios):
    p = 0
    nom_bebida = ''
    for cafe,valor in precios:
        if valor > p:
            p = valor
            nom_bebida = cafe
    return (nom_bebida,p)

resultado = cafe_mas_caro(precios_cafe)
print(resultado)

a,b = cafe_mas_caro(precios_cafe)
print(f'el cafe mas caro es {a.upper()} cuyo valor es {b}')
###################



























