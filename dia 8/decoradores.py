def mayuscula(texto):
    print(texto.upper())

def  minuscula(texto):
    print(texto.lower())

def una_funcion(algo):
    return algo

una_funcion(minuscula('ProBando'))

mi_funcion =  mayuscula  # x = minuscula
mi_funcion('hola mundo, ricardo')  # Llama a la función mayuscula

######-------------- ejemplo 2
print('*'*50)
def cambiar_letras(tipo):

    def palabra_mayus(texto):
        print(texto.upper())

    def palabra_minus(texto):
        print(texto.lower())

    if tipo == 'may':
        return palabra_mayus
    elif tipo == 'min':
        return palabra_minus

try:
    operacion = cambiar_letras('may')
    operacion('esta es una prueba de mayusculas\n')  # Llama a la función palabra_mayus
except TypeError:
    print('Error: No se pudo llamar a la función. Asegúrate de que el tipo sea correcto.')

######------------- ejemplo  3
print('*'*50)
def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion


def mayus(texto):
    print(texto.upper())


def minus(texto):
    print(texto.lower())

mayuscula_decorada = decorar_saludo(mayus)
mayuscula_decorada('ricardo')



