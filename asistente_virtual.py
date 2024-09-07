import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
from gtts import gTTS
from playsound import playsound



# escuchar nuestro micrófono y devolver el audio como texto
def transformar_audio_en_texto():
    """Esta función usa la librería speech_recognizion para convertir
    voz en texto.
    """

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el micrófono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzó la grabación
        print('Ya puedes hablar')

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language='es-col')

            # prueba de que pudo ingresar 
            print('Dijiste: ' + pedido)

            # devolver pedido
            return pedido
        
        except sr.UnknownValueError:

            # prueba de que no comprendió el audio
            print('Ups, no entendí')

            # devolver error
            return 'sigo esperando'
        
        except sr.RequestError:

            # prueba de que no comprendió el audio
            print('Ups, no hay servicio')

            # devolver error
            return 'sigo esperando'
        
        # error inesperado
        except:
        
            # prueba de que no comprendió el audio
            print('Ups, algo ha salido mal')

            # devolver error
            return 'sigo esperando'
        
# función para que el asistente pueda ser escuchado
def hablar(mensaje):
    tts = gTTS(text=mensaje, lang='es')
    tts.save("mensaje.mp3")
    playsound('mensaje.mp3')

# informar el día de la semana
def pedir_dia():
    # crear variable con datos de hoy
    dia = datetime.date.today()

    # crear variable para el día de la semana (índice)
    dia_semana = dia.weekday()

    # diccionario con nombres de días
    calendario = {0: 'lunes', 1: 'martes', 2: 'miercoles', 3:'jueves', 4: 'viernes', 5: 'sábado', 6:' domingo'}

    # decir el día de la semana
    hablar(f"Hoy es {calendario[dia_semana]}")

# informar que hora es
def pedir_hora():
    # crear una variable con los datos de la hora
    hora = datetime.datetime.now()
    hora = f"En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos"

    # decir hora
    hablar(hora)

# funcion saludo inicial
def saludo_inicial():

    # crear variable con datos de hora
    hora = datetime.datetime.now()

    if 19 <= hora.hour < 24 or 0 < hora.hour < 5:
        momento = 'Buenas noches'
    elif 5 <= hora.hour < 12:
        momento = 'Buenos días'
    elif 12 <= hora.hour < 19:
        momento = 'Buenas tardes'

    # decir saludo
    hablar(f'{momento}, soy Helena, tu asistente personal. Por favor, dime en qué te puedo ayudar.')

# funcion central del asistente
def pedir_cosas():
    # activar saludo inicial
    saludo_inicial()

    # variable de corte 
    comenzar = True

    # loop central
    while comenzar:
        # activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy habriendo YouTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue

        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue

        elif 'qué hora es' in pedido:
            pedir_hora()
            continue

        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar(resultado)
            continue

        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue

        elif 'reproducir' in pedido:
            hablar('Buena idea ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue

        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue

        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'Apple': 'APPL', 
                       'Amazon': 'AMZN',
                       'Google': 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdón pero no la he encontrado')
                continue

        elif 'adiós' in pedido:
            hablar('Me voy a descansar, cualquier cosa me avisas')
            break

pedir_cosas()
    