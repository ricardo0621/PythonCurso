import zipfile

zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')  # Abre el archivo zip en modo lectura

zip_abierto.extractall()



###-------------------

#descomprimir un archivo zip con shutil

import shutil

shutil.unpack_archive('archivo_comprimido.zip', 'prueba','zip')  # Descomprime el archivo zip en la carpeta destino