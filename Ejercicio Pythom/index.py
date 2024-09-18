mensaje = input("Escribe algo (escribe 'adios' para salir): ")

while mensaje.lower() != "adios":
    if mensaje.lower() == "hola":
        print("Hola, ¿cómo estás?")
    elif mensaje.lower() == "bien":
        print("¡Qué bueno! Me alegra saber que estás bien.")
    elif mensaje.lower() == "mal":
        print("Lo siento mucho. Si quieres hablar de ello, aquí estoy.")
    elif mensaje.lower() == "¿cómo te va?":
        print("Estoy aquí para ayudarte. ¿En qué puedo asistirte hoy?")
    elif mensaje.lower() == "gracias":
        print("¡De nada! Siempre estoy aquí para ayudarte.")
    elif mensaje.lower() == "cuéntame un chiste":
        print("¿Por qué los pájaros no usan Facebook? ¡Porque ya tienen Twitter!")
    elif mensaje.lower() == "¿qué te gusta hacer?":
        print("Me gusta ayudar a las personas y aprender cosas nuevas. ¿Y a ti?")
    elif mensaje.lower() == "hablame de tus intereses":
        print("Me interesan muchos temas: ciencia, tecnología, arte... ¡Soy curioso por naturaleza!")
    elif mensaje.lower() == "¿tienes hobbies?":
        print("No tengo hobbies como los humanos, pero disfruto conversando contigo.")
    elif mensaje.lower() == "¿qué sabes hacer?":
        print("Puedo ayudarte con información, responder preguntas y tener conversaciones. ¿Algo específico que necesites?")
    elif mensaje.lower() == "cuéntame algo interesante":
        print("¿Sabías que los pulpos tienen tres corazones? ¡Es fascinante!")
    elif mensaje.lower() == "¿qué tiempo hace hoy?":
        print("No tengo acceso a datos en tiempo real, pero siempre es buen momento para una charla.")
    elif mensaje.lower() == "¿me recomiendas un libro?":
        print("Claro, 'Cien años de soledad' de Gabriel García Márquez es un clásico. ¡Te lo recomiendo!")
    else:
        print("No entiendo, ¿puedes repetir?")

    mensaje = input("Escribe algo (escribe 'adios' para salir): ")

print("Hasta luego")