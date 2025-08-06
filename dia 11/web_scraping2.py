import requests
from bs4 import BeautifulSoup

# URL objetivo
url = "https://quotes.toscrape.com"

# Enviar solicitud HTTP
respuesta = requests.get(url)

# Verificar que todo esté bien
if respuesta.status_code == 200:
    # Parsear el contenido HTML
    soup = BeautifulSoup(respuesta.text, 'html.parser')

    # Buscar todas las citas
    citas = soup.find_all('span', class_='text') # Cambia 'text' por la clase que contiene las citas

    print("Citas encontradas:\n")
    for i, cita in enumerate(citas, 1): # Enumerar las citas
        print(f"{i}. {cita.get_text()}")
else:
    print("Error al acceder a la página:", respuesta.status_code)