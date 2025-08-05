nombres = ['ana','juan','hugo']
edades = [65,29,42]
ciudades = ['mexico','colombia','venezu']

combinado = list(zip(nombres,edades,ciudades))
print(combinado)
for nombres,edades,ciudades in combinado:
    print(f'{nombres} tiene {edades} años y vive en {ciudades}')
####################################

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

comb = zip(capitales,paises)

for capitales,paises in comb:
    print(f'la capital de {paises} es {capitales}')
#######################################

espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

numeros = list(zip(espaniol, portugues, ingles))
print(numeros)