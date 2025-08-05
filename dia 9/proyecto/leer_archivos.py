from pathlib import Path

ruta = Path('C:\\Users\\PC_WIN10\\Desktop\\UDEMY\\Curso Phyton\\Clase 9\\Proyecto\\desc_proy')

def leer_archivo(ruta_archivo):
    if ruta_archivo.exists() and ruta_archivo.is_dir(): # Verifica si la ruta existe y es un directorio
        archivos = list(ruta_archivo.iterdir())
        for i in archivos:
            if i.is_file():# Verifica si es un archivo
                print(f'\n📄 Archivo:{i.name}')
                try:
                    contenido = i.read_text(encoding='utf-8')
                    print(f'Contenido del archivo:\n{contenido}')
                except Exception as e:
                    print(f'Error al leer el archivo {i.name}: {e}')
            else:
                print(f'{i.name} es una carpeta.')
    else:
        print(f'La ruta {ruta_archivo} no existe o no es un directorio válido.')

if __name__ == "__main__":
    leer_archivo(ruta)