import subprocess
import sys


# Paquetes requeridos
paquetes = ['flask']

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
