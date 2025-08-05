import zipfile

mi_zip = zipfile.ZipFile('archivo_comprimido.zip','w') # 'w' para escribir, 'r' para leer, 'a' para agregar

mi_zip.write(('mi_texto_A.txt')) #archivo que se va a comprimir
mi_zip.write(('mi_texto_B.txt'))

mi_zip.close()

#---------------------------------------------------------
#otra manera de comprimir archivos es con shutil
import shutil

carpeta_origen = 'C:\\Users\\PC_WIN10\\Desktop\\UDEMY\\Curso Phyton\\Clase 9\\ejercicio_9'

archivo_destino = 'C:\\Users\\PC_WIN10\\Desktop\\UDEMY\\Curso Phyton\\Clase 9\\archivo_comprimido_con_shutil.zip'
#archivo_destino = 'archivo_comprimido_con_shutil.zip' # si se quiere guardar en la misma carpeta, no es necesario poner la ruta completa

shutil.make_archive(archivo_destino, 'zip', carpeta_origen)






