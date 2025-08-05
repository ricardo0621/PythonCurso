from pathlib import Path

# path es como la ruta de un archivo
'''
base = Path.home()#  home para obtener la ruta absoluta
gia = Path(base,'europa','españa',Path('barcelona','sagrada_familia.txt'))
guia2 = gia.with_name('la_pedrera.txt')
#print(base)
print(gia)
print(guia2)

base = Path.home()
gia = Path(base,'europa','españa',Path('barcelona','sagrada_familia.txt'))
print(gia.parent)## trae el antes del archivo
print(gia.parent.parent)
'''
#### ejemplo
guia = Path(Path.home(),'europa')
for i in Path(guia).glob('*.txt'):# con este ve todos los archivos de la carpeta
    print(i)
#------------------
print('\n')
for x,y in enumerate(Path(guia).glob('**/*.txt')):# este va a mostrar todos los archivos txt de las carpetas

    print(x,y.name)

print('\n')

#------------
guia3 = Path('europa','españa','barcelona','sagrada_familia.txt')
en_europa = guia3.relative_to(Path('europa'))# relative_to devuelve un Path
espania = guia3.relative_to(Path('europa','españa'))
print(en_europa)
print(espania)


