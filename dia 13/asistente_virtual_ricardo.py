import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance
import pyjokes
import webbrowser
import datetime
import wikipedia


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



transformar_audio_en_texto()
