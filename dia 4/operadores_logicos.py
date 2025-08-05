#######hacer mas de una comparacion
####operadores logicos and , or,  not
###!=  >  <

### and
mi_bool = (4<5) and (5==2+3)
print(mi_bool)

mi_bool = (55 == 55) and ('perro' == 'perro')
print(mi_bool)

##### or
mi_bool = (2 == 55) or ('nada' == 'perro')
print(mi_bool)

texto = 'esto es una prueba'
bool1= ('estos' in texto) or ('ya' in texto)
bool1= ('estos' in texto) and ('ya' in texto)
print(bool1)

######### not

bolea = not ('a' == 'a') ## esto es para negar la opercion
print(bolea)

