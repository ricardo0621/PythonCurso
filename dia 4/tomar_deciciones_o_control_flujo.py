######!=  >  <
if 10 > 9:
    print("es correcto")


#################
x = 5==2
if x:
    print("es correcto")
else:
    print("es mentira")

##################
mascota = 'perro'
if mascota == 'gato':
    print('tienes un gato')
else:
    print('no se que animal tienes')

#################
mascota2 = 'perro'

if mascota2 == 'gato':
    print('tienes un gato')
elif mascota2 =='perro':
    print('es un perro lo que tienes')
else:
    print('no se que animal tienes')



##############
edad = 16
calificacion = 9

if edad <= 18:
    print('eres menor de edad')
    if calificacion > 10:
        print('paso la materia')
    else:
        print('no paso')

elif edad >= 50:
    print('eres mayor de edad y estas en la tercera edad')
    if calificacion > 10:
        print('paso la materia')
    else:
        print('no paso')

elif (edad >= 18) and (edad < 50):
    print('eres mayor de edad')
    if calificacion > 10:
        print('paso la materia')
    else:
        print('no paso')
else:
    print("la edad que ingresa no es valida")



########################
calificacion = float(input('ingresa la calificacion: '))

if calificacion < 10.5:
    print('malo')
elif calificacion < 13:
    print('regular')
elif calificacion < 16:
    print('bueno')
elif (calificacion >= 16) and (calificacion <=20):
    print('excelente')
else:
    print('digite una calificacion valida')

###################
num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1>num2:
    print(f'{num1} es mayor que {num2}')
elif num2>num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")




