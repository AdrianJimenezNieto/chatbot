import speech_recognition as sr
import pyttsx3
from chatbot import chatbot

def sintetizar_voz(texto):
  # Inicializar el motor de síntesis de voz
  motor_voz = pyttsx3.init()
  motor_voz.setProperty('rate', 150)
  # Configurar el motor para utilizar voces en español
  voices = motor_voz.getProperty('voices')
  motor_voz.setProperty('voice', voices[0].id)  # Puedes cambiar el índice para seleccionar otra voz si está disponible

  # Sintetizar el texto a voz
  motor_voz.say(texto)
  motor_voz.runAndWait()

def reconocimiento_voz():
  # Crear un reconocedor de voz
  reconocedor = sr.Recognizer()

  # Configurar el micrófono como fuente de audio
  mic = sr.Microphone()

  try:
      print("Escuchando... Di algo.")

      with mic as source:
          reconocedor.adjust_for_ambient_noise(source)
          audio = reconocedor.listen(source, timeout=5, phrase_time_limit=5)

      print("Procesando audio...")

      # Utilizar la API de reconocimiento de voz de Google
      texto = reconocedor.recognize_google(audio, language='es-ES')

      return texto

  except sr.UnknownValueError:
      return "No se pudo entender el audio."

  except sr.RequestError as e:
      return f"Error en la solicitud al servicio de reconocimiento de voz: {str(e)}"

while True:
  message = reconocimiento_voz()
  res = chatbot(message)
  sintetizar_voz(res)

