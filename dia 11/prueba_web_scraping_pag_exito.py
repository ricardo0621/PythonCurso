from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Configurar opciones de Chrome (modo sin ventana)
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

# Iniciar navegador con WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Abrir la página
url = "https://www.exito.com/mercado/home"
driver.get(url)

# Esperar a que cargue el contenido dinámico
time.sleep(5)

# Obtener el HTML
html = driver.page_source
driver.quit()

# Parsear con BeautifulSoup
sopa = BeautifulSoup(html, "lxml")

# Buscar los elementos de categoría por clase
categorias = sopa.select('.categorie-buble_fs-categorie-buble__d83AA')

# Imprimir el texto de cada categoría encontrada
print("Categorías encontradas:")
for cat in categorias:
    print("-", cat.get_text(strip=True))