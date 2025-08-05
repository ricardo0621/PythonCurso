def suma():
    n1 = int(input('ingrese un numero: '))
    n2 = int(input('ingrese otro numero: '))
    print(n1 + n2)
    print('gracias por usar la funcion suma'+ n1)

try:
    # codigo que queremos ejecutar
    suma()

except TypeError:
    # codigo que se ejecuta si hay un error
    print('el error es de tipo TypeError, estas intentando sumar un numero con un texto o algo que no es un numero')
except ValueError:
    # codigo que se ejecuta si hay un error
    print('el error es de tipo ValueError, ese no es un numero, por favor ingrese un numero valido')

else:
    # codigo que se ejecuta si no hay error
    print('la funcion se ejecuto correctamente')

finally:
    #codigo que se ejecuta siempre, haya error o no
    print('esto se ejecuta siempre')



#########--------------------------------------------
print('*'*40)
def pedir_numero():
    while True:
        try:
            numero = int(input('ingrese un numero: '))

        else:
            print(f'Numero ingresado correctamente. {numero}')
            break
    print('Gracias por usar la funcion pedir_numero')
pedir_numero()