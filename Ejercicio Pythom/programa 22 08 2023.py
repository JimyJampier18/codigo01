import pyttsx3

texto = "buenos dias profe"

# Inicializa el motor de síntesis de voz
engine = pyttsx3.init()

# Configura propiedades si es necesario
# engine.setProperty('rate', 150)  # Velocidad de habla (palabras por minuto)
# engine.setProperty('volume', 0.9) # Volumen (0.0 a 1.0)

# Convierte el texto en voz y reproduce
engine.say(texto)
engine.runAndWait()