import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance
import pyjokes
import webbrowser
import datetime
import wikipedia

# opciones de voz / idioma
id1 = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id2 = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'


# escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():

    #almacenar recognizer en variable
    r = sr.Recognizer()

    #configurar el microfono
    with sr.Microphone() as origen:

        #tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print('YA PUEDES HABLAR')

        #GUARDAR LO QUE ESCUCHE COMO AUDIO
        audio = r.listen(origen)

        try:
            #buscar en google
            pedido = r.recognize_google(audio,language="es-CO")

            #prueba de que pudo ingresar
            print('disjiste: '+ pedido)

            #devolver pedido
            return pedido

        except sr.UnknownValueError:
            #prueba que no comprendio el audio
            print('ups, no entendi')

            #devolver error
            return 'sigo esperando'

        #en caso de no resolver el pedido
        except sr.RequestError:
            # prueba que no comprendio el audio
            print('ups, no hay servicio')

            # devolver error
            return 'sigo esperando'

        except:
            # prueba que no comprendio el audio
            print('ups, algo salio mal')

            # devolver error
            return 'sigo esperando'


# funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    #encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice',id1)

    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

# esto es para ver cuales son las voces
####engine = pyttsx3.init()
####for voz in engine.getProperty('voices'):
    ####print(voz)


#informar el dia de la semana
def pedir_dia():

    #crear variable de datos de hoy
    dia = datetime.date.today()
    print(dia)

    #crear variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    #diccionario con nombre de los dias
    semana = {0:'Lunes',1:'Martes',2:'Miercoles',3:'Jueves',4:'Viernes',5:'Sabado',6:'Domingo'}

    #decir el dia de la semana
    hablar(f'Hoy es {semana[dia_semana]}')


#informar que hora es
def pedir_hora():

    #crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'en este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    #decir la hora
    hablar(hora)


#funcion saludo inicial
def saludo_inicial():

    #crear variable con datos de hora
    hora=datetime.datetime.now()
    if hora.hour < 6 or hora.hour >= 18:
        momento = 'buenas noches mi Amo'
    elif 6 <= hora.hour < 12:
        momento = 'buen dia mi Amo'
    else:
        momento = 'buenas tardes mi Amo'


    hablar(f'{momento}. soy Reina paola,  tu asistente personal. por favor, dime en que te puedo ayudar')


#funcion central del asistente
def pedir_cosas():

    #activar el saludo inicial
    saludo_inicial()

    #variable de corte
    comenzar = True

    while comenzar:

        #activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'youtube' in pedido:
            hablar('con gusto, estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com/')
            continue
        elif 'abrir el navegador' in pedido:
            hablar('claro, estoy en eso')
            webbrowser.open('https://www.google.com/?hl=es')
            continue
        elif 'qué dia es ' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'buscar en wikipedia' in pedido:
            hablar('Buscando en wikipedia')
            pedido = pedido.replace('busca en wikipedia','')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences = 1)
            hablar('wikipedia dice lo siguiente')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet','')
            pywhatkit.search(pedido)
            hablar('esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('buena idea, ya mismo lo reproduzco')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL','amazon':'AMZN','google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'la encontre, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('perdon pero no la he encontrado')
                continue
        elif 'adiós' in pedido:
            hablar('esta bien mi amo ricardo. estare atento para ti')
            comenzar = False

if __name__ == "__main__":
    pedir_cosas()




#hablar('hola ricardo, esto es una prueba')
#y = transformar_audio_en_texto()
#hablar(y)
