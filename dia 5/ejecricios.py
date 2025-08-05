'''
##### ejercicio 1 enviar tres numeros enteros y devuelve un numero deacurdo a las condiciones
def devolver_distintos(a,b,c):
    suma = a + b + c
    lista = [a,b,c]
    if suma > 15:
        return max(a,b,c)
    elif suma < 10:
        return min(a,b,c)
    elif suma >=10 and suma <=15:
        lista.sort()
        return lista[1]
print(devolver_distintos(3,5,2))

##### ejercicio 2 enviar una palabra y la devuelva una lista sin repetidos
def ejer_2(a):
    lista = list(set(a))##convierte a tipo lista y el set elimina repetidos
    lista.sort()## ordena en orden alfabetico
    return lista
a = ejer_2('cascarrabias')
print(a)


##### ejercicio 3 valida si tiene el cero repetido consecutivo
def cantidad_repetido(*numeros):
    for i in range(1, len(numeros)):  # Empezamos desde el segundo elemento
        if numeros[i] == 0 and numeros[i-1] == 0:
            return True
    return False

x = cantidad_repetido(0,2, 0, 2, 3, 1,0)
print(x)  # False (no hay ceros consecutivos)
'''
#### ejercicio 4 Queremos encontrar todos los números primos desde 2 hasta ese número.
##opcion 1 de chat gpt
def contar_primos(numeros):
    lista_primos = []##creamos una lista vacia
    for i in range(2, numeros + 1):## ciclo que recorre desde el numero dos hasta el numero enviado mas 1 para incluirlo
        es_primo = True #Suponemos que i es primo, y luego intentaremos demostrar lo contrario.
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                es_primo = False
                break
        if es_primo:
            lista_primos.append(i)
    return lista_primos

# Usar la función
x = contar_primos(50)
print(f'{x}, hay: {len(x)}')

###############
####opcion 2 mi opcion
def contar_primos(numeros):
    lista_primos = []
    if numeros < 2:
        return 0
    for i in range(2, numeros + 1):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            lista_primos.append(i)
    return lista_primos

x = contar_primos(10)
print(f'{x}, hay: ',len(x))




