import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


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
        
transformar_audio_en_texto()
