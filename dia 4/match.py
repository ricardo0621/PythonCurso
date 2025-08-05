#####match es para mirar las coincidencias
serie = 'n-03'
match serie:
    case 'n-01':
        print('samsung')
    case 'n-02':
        print('nokia')
    case 'n-03':
        print('LG')
    case _:
        print('no existe este producto')
##############

cliente =  {'nombre':'federico',
            'edad':45,
            'ocupacion':'instructor'}
pelicula = {'titulo':'matrix',
            'ficha_tecnica':{'protagonista':'keanu reev',
                             'director':'lana y wachoski'}}

elementos = [cliente,pelicula,'libro']

for e in elementos:
    match e:
        case {'nombre':a,
            'edad':b,
            'ocupacion':c}:
            print('esto es un cliente')
            print(a,b,c)
        case {'titulo':a,
            'ficha_tecnica':{'protagonista':b,
                             'director':c}}:
            print('esto es una peli')
            print(a,b,c)
        case _:
            print('no se que es eso')