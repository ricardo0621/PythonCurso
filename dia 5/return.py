'''return es para devolver un resultado
y poderlo almacenar ya que si solo
se imprime no se puede almacenar
##lo ideal es que una fucnion no imprima y solo devuelva un valor
'''
def multiplicar(num1,num2):
        return num1*num2 ##opcion 1 colocando directamente la operacion e el return

resultado = multiplicar(5,10)
print(resultado)
#########################

##opcion 2
def multiplicar_numeros(num1, num2):
    total = num1*num2
    return total  ##colocando directamente la variable que contiene la operacion

resul= multiplicar_numeros(2, 10)
print(resul)
##########################

def usd_a_eur(x):
    return x*0.90

dolares = usd_a_eur(5)###estoy creando una var que me guarda el valor que retorna la funcion usd_a_eur
print(dolares)
####################

def invertir_palabra(a):
    res = a[::-1].upper()##esto guarda el string al inverso
    return res##si no se pone el return no retorna nada solo ejecuta la accion de la funcion

palabra = invertir_palabra('Python')
print(palabra)
#################