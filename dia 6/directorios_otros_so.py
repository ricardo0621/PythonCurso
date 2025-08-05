### para leer desde mac o linux
from pathlib import Path
# con la barra / es para que los mac y linus lo interprete
carpeta = Path('/Users/PC_WIN10/Desktop/UDEMY/Curso Phyton/archivos_clase6')
archivo = carpeta / 'alter_2.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())



#os.path.basename(archivo) esto seria para obtener el nombre del archivo