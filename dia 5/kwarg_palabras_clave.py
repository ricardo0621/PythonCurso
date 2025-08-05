'''
def suma(**kwarg):
    total = 0
    for clave,valor in kwarg.items():
        print(f'{clave} = {valor}')
        total += valor
    return total

print(suma(x=3,y=5,z=9))
#############################
### este codigo es para mezclar argumentos

def prueba(num1,num2,*arg,**kwar):
    print(f'el primer valor es {num1}')
    print(f'el primer valor es {num2}')

    for i in arg:
        print(f'arg {i}')

    for clave,valor in kwar.items():
        print(f'{clave} = {valor}')
### prueba(2,15,100,200,300,x='ricar',y='carlos')

#### esta es una opcion para imprimir directamente de las variables
args = [100,200,300]
kwarg = {'x':'uno','y':'dos'}
prueba(2,3,*args,**kwarg)
################################
'''


def cantidad_atributos(**atributos):
    return len(atributos)

print(cantidad_atributos(x=8,r=9,t=6))
###################


def lista_atributos(**palabra):
    lista = []
    for b in palabra.values():
        lista.append(b)
    return lista

x = lista_atributos(a='keywords')
print(x)
print(type(x))
##############################

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')
describir_persona('tomás',color_ojos='azules',color_pelo='rubio')




