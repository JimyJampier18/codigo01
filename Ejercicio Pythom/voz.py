import pyttsx3

engine = pyttsx3.init()

mensaje = input("Escribe algo (escribe 'adios' para salir): ")

while mensaje.lower() != "adios":
    if mensaje.lower() == "hola":
        engine.say("Hola, ¿cómo estás?")
    else:
        engine.say("No entiendo, ¿puedes repetir?")

    engine.runAndWait()

    mensaje = input("Escribe algo (escribe 'adios' para salir): ")

engine.say("Hasta luego")
engine.runAndWait()