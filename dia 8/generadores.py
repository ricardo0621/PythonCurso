def mi_generador():
    yield 4

g = mi_generador()
print(next(g))

#####--------------------------
print('*'*50)
def generador_numeros():
    for i in range(1,4):
        yield i * 10

x = generador_numeros()
print(next(x))
print(next(x))
print(next(x))

#####--------------------------
print('*'*50)
def generador_otro():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

h = generador_otro()
print(next(h))
print(next(h))
print(next(h))

#####--------------------------
print('*'*50)
def gen():
    x = 1
    while True:
        yield x
        x+= 1


generador = gen()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

#####--------------------------
print('*'*50)
def multiplos_de_7():
    n = 7
    while True:
        yield n
        n += 7
generador = multiplos_de_7()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

#####--------------------------
print('*'*50)
def vidas():
    vida = 3
    while vida > 0:
        if vida == 1:
            yield "Te queda 1 vida"
        else:
            yield f"Te quedan {vida} vidas"
        vida -= 1
    yield "Game Over"

perder_vida = vidas()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))



