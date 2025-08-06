import subprocess
import sys


# Paquetes requeridos
paquetes = ['pyinstaller']

# Función para instalar un paquete si no está presente
def instalar_paquetes(paquetes):
    for paquete in paquetes:
        try:
            __import__(paquete)
            print(f'✅ {paquete} ya está instalado.')
        except ImportError:
            print(f'📦 Instalando {paquete}...')
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', paquete])
            print(f'✅ {paquete} instalado correctamente.')

if __name__ == '__main__':
    print("🔧 Verificando dependencias...\n")
    instalar_paquetes(paquetes)
    print("\n🎯 Todos los paquetes están listos para usar.")

    pyinstaller - -onefile - -windowed - -add - data "ovni.png;." - -add - data "disparo.mp3;." - -add - data "cohete.png;." - -add - data "bala.png;." - -add - data "enemigo.png;." - -add - data "Fondo.jpg.mp3;." - -add - data "Golpe.mp3;." - -add - data "MusicaFondo.mp3;." juego_invasion_espacial.py
