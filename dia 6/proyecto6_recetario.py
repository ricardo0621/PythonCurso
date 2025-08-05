from pathlib import Path
from os import system

nombre_usuario = input('cual es tu nombre: ')
system('cls')
# ruta
ruta_recetas = Path('C:/Users/PC_WIN10/Desktop/UDEMY/Curso Phyton/Clase 6/proyecto_recetario/Recetas')
if not ruta_recetas.exists():
    print(f'❌ la ruta que esta consultando no existe.')
# variables
categorias_ruta = []
nombre_categoria = []
archivos_recetas = []
nombre_archivos = []

#### bucles para capturar el numero y nombre de las carpetas y archivos---------------------------
for carpeta in ruta_recetas.iterdir():# este for recorre las cantidad de elementos
    if carpeta.is_dir():#este valida si es una carpeta
        categorias_ruta.append(carpeta)
        for archivo in carpeta.iterdir():# Obtener el contenido de esa subcarpeta
            if archivo.is_file():#este valida si es un archivo
                archivos_recetas.append(archivo)

for i in categorias_ruta:# este for es para guardar los nombre de las carpetas
    nombre_categoria.append(i.name)
for i in archivos_recetas:# este for es para guardar los nombre de los archivos
    nombre_archivos.append(i.name)

print(f'HOLA BIENVENIDO {nombre_usuario}\nlas Recetas de CASA-CASTILLO estan en la siguiente direccion:\n{ruta_recetas}')
print(f'Hay {len(categorias_ruta)} categorias y {len(archivos_recetas)} Recetas en total')

#### funciones-------------------------------------------
def mostrar_categorias_recetas(categoria):
    print('\nCategorías disponibles:')
    for poscion,valor in enumerate(categoria, start=1):
        print(f'{poscion}.{valor.name}')
    while True:
        seleccion = input('\nSelecciona una categoría por número: ')
        if seleccion.isdigit():
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(categoria):
                carpeta_seleccion = categoria[seleccion - 1]
                print(f'\n✅ Seleccionaste la categoría: {carpeta_seleccion.name}')

                # Buscar recetas en la carpeta seleccionada----------------
                receta = []
                for i in carpeta_seleccion.iterdir():
                    if i.is_file():
                        receta.append(i)
                if len(receta) == 0:
                    print('⚠️ Esta categoría no tiene recetas.\n')
                    return None
                print('\n📃 Recetas disponibles:')
                for indice, nombre in enumerate(receta, start=1):
                    print(f'{indice}.{nombre.name}')
                ##########
                while True:
                    sel_receta = input('\nSelecciona una receta por número: ')
                    if sel_receta.isdigit():
                        sel_receta = int(sel_receta)
                        if 1 <= sel_receta <= len(receta):
                            receta_elegida = receta[sel_receta - 1]
                            return receta_elegida
                        else:
                            print("❌ Número fuera del rango de recetas.\n")
                    else:
                        print("❌ Entrada inválida. Debes ingresar un número para la receta.\n")

            else:
                print("❌ Número fuera del rango de categorías.\n")
        else:
            print('❌ Entrada inválida. Debes ingresar un número.\n')


def leer_receta(receta):## para leer una receta
    if receta is None:
        print("⚠️ No se seleccionó ninguna receta.")
        return
    with open(receta,encoding='utf-8')as archivo:# con with no necesitas cerrar, se cierra solo
        print(archivo.read())

def crear_receta(categoria):
    print('\nCategorías disponibles:')
    for poscion, valor in enumerate(categoria, start=1):
        print(f'{poscion}.{valor.name}')
    while True:
        seleccion = input('\n🔢 Selecciona una categoría por número: ')

        if seleccion.isdigit():
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(categoria):
                carpeta_seleccion = categoria[seleccion - 1]
                print(f'\n✅ Seleccionaste la categoría: {carpeta_seleccion.name}')

                # crear un archivo----------------
                while True:
                    nombre_receta_sin_extension = input('📝 Ingresa el nombre de la receta (sin extensión): ')
                    if not nombre_receta_sin_extension.strip():
                        print('⚠️ No ingresaste un nombre.')
                    else:
                        break
                nombre_receta = nombre_receta_sin_extension + '.txt'
                ruta_nueva_receta = carpeta_seleccion / nombre_receta
                # validar si ya existe
                if ruta_nueva_receta.exists():
                    sobreescribir = input("⚠️ El archivo ya existe. ¿Deseas sobrescribirlo? (s/n): ")
                    if sobreescribir.lower() == 's':
                        contenido = input("📃 Escribe el contenido de la receta:\n")
                        if not contenido:
                            print('⚠️ No ingresaste un nombre.')
                            return
                        with open(ruta_nueva_receta, 'w', encoding='utf-8') as nuevo:
                            nuevo.write(contenido)
                        print(f'✅ Receta guardada en la carpeta {carpeta_seleccion.name}')
                        break
                    else:
                        print("🚫 Operación cancelada.")
                else:
                    contenido = input("📃 Escribe el contenido de la receta:\n")
                    with open(ruta_nueva_receta, 'w', encoding='utf-8') as nuevo:
                        nuevo.write(contenido)
                    print(f'✅ Receta guardada en la carpeta {carpeta_seleccion.name}')
                    break

            else:
                print("❌ Número fuera de rango.")
        else:
            print("❌ Entrada inválida. Debes ingresar un número.....")

def crear_categoria(ruta_recetas):
    print('\nCategorías disponibles:')
    for i in ruta_recetas.iterdir():
        if i.is_dir():
            print(f'{i.name}')

    while True:
        nueva_categoria = input('📁 Ingresa el nombre de la nueva categoria: ')
        if not nueva_categoria:
            print("⚠️ No ingresaste un nombre.")
            continue # vuelve a pedir
        else:
            nueva_carpeta = ruta_recetas/nueva_categoria

        if nueva_carpeta.exists():
            print(f"❌ La categoría '{nueva_categoria}' ya existe.")
            continue# pide otro nombre
        else:
            nueva_carpeta.mkdir()
            print(f"✅ categoria '{nueva_categoria}' creada en {ruta_recetas.name}")
            break # salimos tras crearla

def quitar_receta(receta_ruta):
    if receta_ruta:
        receta_ruta.unlink()# Elimina el archivo
        print(f"✅ SE HA ELIMINADO LA RECETA: {receta_ruta.name} ☹️\n")

    else:
        print("⚠️ No se pudo eliminar ninguna receta, ya que no se encontraron archivos en la categoria.\n")

def elimina_carpeta(ruta_categoria):
    if not ruta_categoria.exists():
        print(f'❌ no hay carpetas de categorias para eliminar.')
        return
### aca creo una lista la cual captura las capetas dentro del directorio
    lista_categoria = []
    for i in ruta_categoria.iterdir():
        if i.is_dir():
            lista_categoria.append(i)
    if not lista_categoria:
        print("⚠️ No se encontraron categorias para eliminar.")
        return

    print('\n📂 Categorías disponibles:')

    for numerador,valor in enumerate(lista_categoria,start=1):
        print(f'{numerador}.{valor.name}')

    while True:
        categoria_seleccionada = input('📂 elige el numero de la categoria a eliminar: ').strip()
        if not categoria_seleccionada:
            print("⚠️ No ingresaste ningún valor.")
            continue
        if not categoria_seleccionada.isdigit():
            print("❌ Solo se permiten números.")
            continue


        if categoria_seleccionada.isdigit():
            categoria_seleccionada = int(categoria_seleccionada)
            if categoria_seleccionada>len(lista_categoria):
                print(f'❌ Solo se permiten números dentor del rango 1 al {len(lista_categoria)}.')

            if 1 <= categoria_seleccionada <= len(lista_categoria):
                categoria_eliminar = lista_categoria[categoria_seleccionada - 1]
                print(f'SE HA ELIMINADO LA CARPETA O CATEGORIA "{categoria_eliminar.name}"')
                categoria_eliminar.rmdir()
                break

#esta fue una funcion mas larga pero no se esta usando no la voy a usar
def elimina_receta(categorias):
    print('\nCategorías disponibles:')
    for i,carpeta in enumerate(categorias,start=1):
        print(f'{i}.{carpeta.name}')

    while True:
        cate = input('📂 elige el numero de una categoria: ').strip()  ## elimina espacios al inicio y final
        if not cate:
            print("⚠️ No ingresaste ningún valor.")
            continue
        if not cate.isdigit():
            print("❌ Solo se permiten números.")
            continue
        cate = int(cate)
        if 1 <= cate <= len(categorias):
            cat_elegida = categorias[cate - 1]
            print(f"✅ Elegiste la categoría: {cat_elegida.name}")

            ###elegir receta-------
            receta = []
            for i in cat_elegida.iterdir():
                if i.is_file():
                    receta.append(i)
            if len(receta)==0:
                print('⚠️ Esta categoría no tiene recetas.\n')
                return None
            print('📃  Recetas disponibles: ')
            for indice,valor in enumerate(receta,start=1):
                print(f'{indice}.{valor.name}')

            while True:
                rece = input('\n📃 elige el numero de la receta que va a eliminar:').strip()
                if not rece:
                    print("⚠️ No ingresaste ningún valor.")
                    continue
                if not rece.isdigit():
                    print("❌ Solo se permiten números.")
                    continue
                if len(rece)>1:
                    print(f"❌ ingresa un numero del 1 al {len(receta)}")
                    continue
                rece = int(rece)
                if rece > len(receta):
                    print(f"❌ ingresa un numero del 1 al {len(receta)}")
                    continue

                if 1<= rece <= len(receta):
                    rece_elegida = receta[rece -1]
                    print(f"✅ SE HA ELIMINADO LA RECETA: {rece_elegida.name} ☹️")
                    rece_elegida.unlink()  # 🔥 Elimina el archivos mas nunca carpetas
                    break
            break

        else:
            print(f"❌ Número fuera de rango. Ingresa un valor entre 1 y {len(categorias)}.")

#### logica del recetario------------------------------------------
while True:
    print('¿que quieres hacer, elige una OPCION?\n')
    print('1. LEER RECETA')
    print('2. CREAR RECETA')
    print('3. CREAR CATEGORIA')
    print('4. ELIMINAR RECETA')
    print('5. ELIMINAR CATEGORIA')
    print('6. FINALIZAR PROGRAMA')
    opcion_menu = input('ingrese una opcion del menu: ')

    if opcion_menu.isdigit() and len(opcion_menu)==1:
        opcion_menu = int(opcion_menu) # convertir a entero la opcion ingresada

        if 1<= opcion_menu <= 6:
            if opcion_menu == 1:##-------------
                system('cls')
                receta=mostrar_categorias_recetas(categorias_ruta)
                if receta:
                    leer_receta(receta)
                    print('\n')
                else:
                    print("⚠️ No se pudo leer ninguna receta, ya que no se encontraron archivos en la categoria.\n")

            elif opcion_menu == 2:##-----------------
                system('cls')
                crear_receta(categorias_ruta)
                print('\n')

            elif opcion_menu == 3:##-----------------
                system('cls')
                crear_categoria(ruta_recetas)

                # 🔄 ACTUALIZAR categorias_ruta y nombre_categoria DESPUÉS DE CREAR CATEGORÍA
                categorias_ruta = []
                nombre_categoria = []
                for carpeta in ruta_recetas.iterdir():
                    if carpeta.is_dir():
                        categorias_ruta.append(carpeta)
                print('\n')

            elif opcion_menu == 4:
                system('cls')
                x = mostrar_categorias_recetas(categorias_ruta)
                quitar_receta(x)
                print('\n')

            elif opcion_menu == 5:
                system('cls')
                elimina_carpeta(ruta_recetas)

                # 🔄 ACTUALIZAR categorias_ruta DESPUÉS DE eliminar CATEGORÍA
                categorias_ruta = []
                for carpeta in ruta_recetas.iterdir():
                    if carpeta.is_dir():
                        categorias_ruta.append(carpeta)
                print('\n')


            elif opcion_menu == 6:
                system('cls')
                print('Chao, Bye, adios')
                break

                # Preguntar si quiere volver al menú después de ejecutar la acción
            if opcion_menu != 6:
                volver = input("¿Quieres volver al menú principal? (s/n): ").strip().lower()
                if volver != 's':
                    print("Saliendo del programa...")
                    break
                else:
                    system('cls')

        else:
            system('cls')
            print('Número fuera de rango. Elige una opción entre 1 y 6.\n')
    else:
        system('cls')
        print('Entrada inválida. Debes ingresar un numero de opcion valido.\n')














