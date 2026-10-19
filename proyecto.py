# AVANCE 1: Selección de proyecto
# Proyecto Libre: RECOMENDADOR MUSICAL

print("RECOMENDADOR MUSICAL")

# AVANCE 3: Incorpora a tu proyecto libre uso de funciones
# Función encargada de calcular la compatibilidad de una canción 
def calcular_compatibilidad(
    genero_cancion,
    artista_cancion,
    mood_cancion,
    genero_usuario,
    segundo_genero,
    artista_usuario,
    mood_usuario):
    puntuacion = 0

# AVANCE 2: Incorpora a tu proyecto libre operaciones con operadores
# (Operadores aritméticos y lógicos para el cálculo de compatibilidad)

# Suma puntos si el género principal coincide
    if genero_cancion == genero_usuario:
        puntuacion = puntuacion + 4

# Suma puntos si el segundo género coincide
    if genero_cancion == segundo_genero:
        puntuacion = puntuacion + 2

# Suma puntos si el artista favorito coincide
    if artista_cancion == artista_usuario:
        puntuacion = puntuacion + 3

# Suma puntos si el estado de ánimo (mood) coincide
    if mood_cancion == mood_usuario:
        puntuacion = puntuacion + 3

# Extra si coincide el género principal y el mood al mismo tiempo
    if genero_cancion == genero_usuario and mood_cancion == mood_usuario:
        puntuacion = puntuacion + 2

# Extra si coincide algún género y el artista favorito
    if (genero_cancion == genero_usuario or
        genero_cancion == segundo_genero) and artista_cancion == artista_usuario:
        puntuacion = puntuacion + 2

    return puntuacion

# Función para mostrar en pantalla la canción recomendada y su puntaje final
def mostrar_recomendacion(
    nombre_cancion,
    artista_cancion,
    puntuacion):

    print("\n----------------------------------------")
    print("¡Canción recomendada para ti!")
    print(nombre_cancion, "-", artista_cancion)
    print("Compatibilidad:", puntuacion, "puntos")
    print("----------------------------------------\n")

# Interacción inicial con el usuario
nombre = input("¿Cuál es tu nombre?: ")
print("Hola,", nombre + "!")

# AVANCE 6: Incorpora a tu proyecto libre listas (arreglos)
# (Creación de la lista 'historial_recomendaciones')
historial_recomendaciones = []

# AVANCE 5: Incorpora a tu proyecto libre estructuras de repetición (ciclos)
# (Ciclo while para permitir repetir el recomendador)
continuar = "si"
while continuar.lower() == "si" or continuar.lower() == "sí":
    print("\n Vamos a encontrar música que podría gustarte.")

# Selección del género musical principal con validación básica
    print("\nSelecciona tu género musical favorito:")
    print("1. Pop")
    print("2. K-Pop")
    print("3. R&B")
    print("4. Afrobeats")

# AVANCE 4: Incorpora a tu proyecto libre estructuras de decisión
# (Uso de condicionales if-elif-else para procesar las elecciones del usuario)
    opcion = int(input("Selecciona una opción (1-4): "))
    if opcion == 1:
        genero_usuario = "Pop"
    elif opcion == 2:
        genero_usuario = "K-Pop"
    elif opcion == 3:
        genero_usuario = "R&B"
    elif opcion == 4:
        genero_usuario = "Afrobeats"
    else:
        genero_usuario = "Pop"
        print("Opción no válida. Se utilizará Pop por defecto.")

# Selección del segundo género musical de preferencia
    print("\nSelecciona otro género que también te guste:")
    print("1. Pop")
    print("2. K-Pop")
    print("3. R&B")
    print("4. Afrobeats")

    opcion = int(input("Selecciona una opción (1-4): "))
    if opcion == 1:
        segundo_genero = "Pop"
    elif opcion == 2:
        segundo_genero = "K-Pop"
    elif opcion == 3:
        segundo_genero = "R&B"
    elif opcion == 4:
        segundo_genero = "Afrobeats"
    else:
        segundo_genero = "Pop"
        print("Opción no válida. Se utilizará Pop por defecto.")

# Selección del artista favorito
    print("\nSelecciona un artista que te guste:")
    print("1. Sabrina Carpenter")
    print("2. Dua Lipa")
    print("3. The Weeknd")
    print("4. Jennie")
    print("5. Billie Eilish")
    print("6. Ninguno en especial")

    opcion = int(input("Selecciona una opción (1-6): "))
    if opcion == 1:
        artista_usuario = "Sabrina Carpenter"
    elif opcion == 2:
        artista_usuario = "Dua Lipa"
    elif opcion == 3:
        artista_usuario = "The Weeknd"
    elif opcion == 4:
        artista_usuario = "Jennie"
    elif opcion == 5:
        artista_usuario = "Billie Eilish"
    else:
        artista_usuario = "Ninguno"

# Selección del estado de ánimo (mood) deseado
    print("\n¿Qué tipo de música quieres escuchar?")
    print("1. Energética")
    print("2. Para fiesta")
    print("3. Relajada")
    print("4. Romántica")

    opcion = int(input("Selecciona una opción (1-4): "))
    if opcion == 1:
        mood_usuario = "Energico"
    elif opcion == 2:
        mood_usuario = "Fiesta"
    elif opcion == 3:
        mood_usuario = "Relajado"
    elif opcion == 4:
        mood_usuario = "Romantico"
    else:
        mood_usuario = "Energico"
        print("Opción no válida. Se utilizará música energética por defecto.")

# Cálculo de compatibilidad enviando parámetros a la función
    cancion1 = calcular_compatibilidad(
        "Pop",
        "Sabrina Carpenter",
        "Fiesta",
        genero_usuario,
        segundo_genero,
        artista_usuario,
        mood_usuario)

    cancion2 = calcular_compatibilidad(
        "K-Pop",
        "Jennie",
        "Energico",
        genero_usuario,
        segundo_genero,
        artista_usuario,
        mood_usuario)

    cancion3 = calcular_compatibilidad(
        "R&B",
        "The Weeknd",
        "Relajado",
        genero_usuario,
        segundo_genero,
        artista_usuario,
        mood_usuario)

# Nivel de compatibilidad encontrado usando condicionales
    if cancion1 >= 9 or cancion2 >= 9 or cancion3 >= 9:
        print("\n¡Encontramos una canción con alta compatibilidad!")
    elif cancion1 >= 6 or cancion2 >= 6 or cancion3 >= 6:
        print("\nEncontramos una canción con compatibilidad moderada.")
    else:
        print("\nLa compatibilidad con las canciones disponibles es baja.")

# Estructura condicional para determinar cuál canción obtuvo la mayor puntuación
    if cancion1 >= cancion2 and cancion1 >= cancion3:
        nombre_cancion_rec = "Espresso"
        artista_cancion_rec = "Sabrina Carpenter"
        puntaje_rec = cancion1
        mostrar_recomendacion(nombre_cancion_rec, artista_cancion_rec, puntaje_rec)

    elif cancion2 >= cancion1 and cancion2 >= cancion3:
        nombre_cancion_rec = "Mantra"
        artista_cancion_rec = "Jennie"
        puntaje_rec = cancion2
        mostrar_recomendacion(nombre_cancion_rec, artista_cancion_rec, puntaje_rec)

    else:
        nombre_cancion_rec = "One Of The Girls"
        artista_cancion_rec = "The Weeknd"
        puntaje_rec = cancion3
        mostrar_recomendacion(nombre_cancion_rec, artista_cancion_rec, puntaje_rec)

# AVANCE 6: Uso del método .append() en la lista para agregar elementos
    historial_recomendaciones.append(nombre_cancion_rec + " - " + artista_cancion_rec + " (" + str(puntaje_rec) + " puntos)")

# Preguntar al usuario si desea realizar otra consulta para el control del ciclo while
    continuar = input("¿Te gustaría buscar otra recomendación musical? (sí/no): ")

# AVANCE 6: Recorrer la lista (arreglo) con un ciclo 'for'
if len(historial_recomendaciones) > 0:
    print("\n========================================")
    print("HISTORIAL DE RECOMENDACIONES DE LA SESIÓN:")
    print("========================================")
    for cancion_guardada in historial_recomendaciones:
        print("•", cancion_guardada)
    print("========================================")

# Mensaje final al salir del programa
print("FIN DEL RECOMENDADOR")
