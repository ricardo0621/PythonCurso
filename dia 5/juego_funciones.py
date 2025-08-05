
from random import *

def lanzar_dados():
    num1 = randint(1,6)## guardo en la var un aleatorio
    num2 = randint(1,6)

    return (num1,num2)

def evaluar_jugada(dado1,dado2):

    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        print (f'La suma de tus dados es {suma_dados}. Lamentable')
    elif suma_dados > 6 and suma_dados < 10:
        print (f'La suma de tus dados es {suma_dados}. Tienes buenas chances')
    elif suma_dados >= 10:
        print (f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")
    print(f'el primer numero es {dado1} y el segundo es {dado2}')

t,g = lanzar_dados()####asigno a dos variables lo que retorna lanzar dados()
evaluar_jugada(t,g)
#######################################
lista_numeros = [1, 2, 15, 7, 2, 8]

def reducir_lista(lista):
    lista = set(lista) ### aca quito los duplicados
    maximo = max(lista)##### capturo el maximo de la lista
    lista.remove(maximo) #### remuevo el maximo
    return lista


def promedio(lista):
    suma = sum(lista)
    cantidad = len(lista)
    promedio = suma / cantidad
    return promedio


x = reducir_lista(lista_numeros)
print(promedio(x))
####################################


from random import *

lista_numeros = [1, 2, 3]

def lanzar_moneda():
    moneda = ['Cara', 'Cruz']
    eleccion = choice(moneda)###es un aleatorio para str
    return eleccion

def probar_suerte(a, b):
    if a == 'Cara':
        print('La lista se autodestruirá')
        b.clear()##borra la lista o el argumento que recibe
        return b
    else:
        print('La lista fue salvada')
        return b


moneda_final = lanzar_moneda()
print(moneda_final)
probar_suerte(moneda_final, lista_numeros)
print(lista_numeros)


