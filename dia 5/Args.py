################
'''
# opcio 1 para enviar argumentos
def suma(*args):

    total = 0
    for i in args:
        total += i
    return total
print(suma(5,6,5,5,5))
'''

# opcio 2 para enviar argumentos reducido
def suma(*numeros):
    return sum(numeros)

print(suma(5,6,5,5,5,))
##########################
def suma_cuadrados(*numeros):
    elev = 0
    for i in numeros:
        elev += i**2
    return elev
print(suma_cuadrados(1,2,3))

#############################
#este pasa a positivos y suma todos los numeros
def suma_absolutos(*numeros):
    suma = 0
    for i in numeros:
        suma += abs(i)
    return suma
print(suma_absolutos(2, -2, -1))

############################
# este codigo toma un string y varios numeros lo cual devuelve un mensaje
def numeros_persona(nombre, *numeros):
    sumatoria = sum(numeros)
    return (f"{nombre}, la suma de tus números es {sumatoria}")

print(numeros_persona('ricardo', 2, 2, 2))
