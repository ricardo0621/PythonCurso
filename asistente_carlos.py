import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import pyjokes
import pywhatkit
import yfinance as yf
import random

# =====================
# CONFIGURACIÓN DE VOZ
# =====================
VOICE_ID = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'

# =====================
# FUNCIONES BÁSICAS
# =====================
def hablar(mensaje: str):
    """Convierte texto a voz"""
    engine = pyttsx3.init()
    engine.setProperty('voice', VOICE_ID)
    engine.say(mensaje)
    engine.runAndWait()

def escuchar() -> str:
    """Escucha el micrófono y devuelve el texto"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Escuchando...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        pedido = r.recognize_google(audio, language="es-CO")
        print(f"👉 Dijiste: {pedido}")
        return pedido.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        hablar("⚠ No hay servicio de reconocimiento en este momento")
        return ""
    except:
        return ""

# =====================
# FUNCIONES DEL ASISTENTE
# =====================
def pedir_dia():
    dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
    hoy = datetime.date.today()
    hablar(f"Hoy es {dias[hoy.weekday()]}")

def pedir_hora():
    hora = datetime.datetime.now().strftime("Son las %H horas con %M minutos")
    hablar(hora)

def saludo_inicial():
    hora = datetime.datetime.now().hour
    if hora < 6 or hora >= 18:
        momento = "buenas noches"
    elif hora < 12:
        momento = "buen día"
    else:
        momento = "buenas tardes"

    hablar(f"{momento}, soy eli, tu asistente personal. ¿En qué te puedo ayudar?")

# =====================
# FUNCIONES EXTRAS
# =====================
def abrir_youtube():
    hablar("Con gusto, estoy abriendo YouTube")
    webbrowser.open("https://www.youtube.com/")

def abrir_google():
    hablar("Claro, estoy abriendo Google")
    webbrowser.open("https://www.google.com/")

def buscar_wikipedia(pedido):
    try:
        tema = pedido.replace("busca en wikipedia", "").strip()
        resumen = wikipedia.summary(tema, sentences=2, auto_suggest=True)
        hablar("Según Wikipedia: " + resumen)
    except:
        hablar("Lo siento, no encontré resultados en Wikipedia")

def contar_chiste():
    hablar(pyjokes.get_joke("es"))

def reproducir_youtube(pedido):
    cancion = pedido.replace("reproduce", "").strip()
    hablar(f"Reproduciendo {cancion} en YouTube")
    pywhatkit.playonyt(cancion)

def precio_accion(pedido):
    accion = pedido.replace("precio de", "").strip()
    try:
        ticker = yf.Ticker(accion)
        precio = ticker.history(period="1d")["Close"][0]
        hablar(f"El precio actual de {accion} es {precio:.2f} dólares")
    except:
        hablar("No pude obtener el precio de la acción")

# =====================
# FUNCIÓN DE REDACCIÓN ORIGINAL
# =====================
def redactar_texto(pedido):
    tema = pedido.replace("redacta un texto sobre", "").replace("redacta un texto de", "").strip()

    if not tema:
        hablar("Por favor dime el tema del texto que quieres redactar")
        return

    introducciones = [
        f"Reflexionar sobre {tema} es esencial, ya que influye de manera directa en nuestra vida cotidiana.",
        f"{tema.capitalize()} se ha convertido en un asunto de gran interés en los últimos tiempos.",
        f"Cuando se habla de {tema}, resulta evidente su impacto en la sociedad actual."
    ]

    desarrollos = [
        f"Desde una perspectiva amplia, {tema} abre nuevas posibilidades y plantea también ciertos desafíos.",
        f"Este tema no solo se relaciona con aspectos individuales, sino que también repercute en lo social y lo colectivo.",
        f"Es innegable que {tema} transforma la manera en que las personas aprenden, trabajan y se relacionan."
    ]

    transiciones = [
        "Además, conviene resaltar que ",
        "Por otra parte, no podemos ignorar que ",
        "Igualmente, resulta clave comprender que "
    ]

    argumentos = [
        f"{tema} impulsa cambios significativos en distintos ámbitos de la vida.",
        f"El análisis de {tema} permite comprender mejor los retos del presente y del futuro.",
        f"La presencia de {tema} plantea la necesidad de adaptarse a nuevas realidades."
    ]

    conclusiones = [
        f"En definitiva, {tema} constituye un pilar fundamental para la evolución social y cultural.",
        f"A manera de conclusión, puede afirmarse que {tema} seguirá marcando tendencias en el porvenir.",
        f"Finalmente, reconocer la importancia de {tema} es dar un paso hacia un futuro más consciente."
    ]

    texto = (
        random.choice(introducciones) + " " +
        random.choice(desarrollos) + " " +
        random.choice(transiciones) + random.choice(argumentos) + " " +
        random.choice(conclusiones)
    )

    print("\n📝 Texto generado (original y no rastreable):\n", texto, "\n")
    hablar("He redactado un texto sobre " + tema)
    hablar(texto)

# =====================
# PROCESAR COMANDOS
# =====================
def procesar_pedido(pedido: str):
    if "youtube" in pedido:
        abrir_youtube()
    elif "google" in pedido or "navegador" in pedido:
        abrir_google()
    elif "qué día es" in pedido:
        pedir_dia()
    elif "qué hora es" in pedido:
        pedir_hora()
    elif "busca en wikipedia" in pedido:
        buscar_wikipedia(pedido)
    elif "chiste" in pedido:
        contar_chiste()
    elif "reproduce" in pedido:
        reproducir_youtube(pedido)
    elif "precio de" in pedido:
        precio_accion(pedido)
    elif "redacta un texto" in pedido:
        redactar_texto(pedido)
    elif "salir" in pedido or "termina" in pedido:
        hablar("Hasta luego, fue un gusto ayudarte")
        return False
    else:
        hablar("Lo siento, no entendí el comando")
    return True

# =====================
# LOOP PRINCIPAL
# =====================
def iniciar_asistente():
    saludo_inicial()
    activo = True
    while activo:
        pedido = escuchar()
        if pedido:
            activo = procesar_pedido(pedido)

# =====================
# EJECUCIÓN
# =====================
if __name__ == "__main__":
    iniciar_asistente()