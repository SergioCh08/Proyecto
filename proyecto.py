print("RECOMENDADOR MUSICAL")

def calcular_compatibilidad(
    genero_cancion,
    artista_cancion,
    mood_cancion,
    genero_usuario,
    segundo_genero,
    artista_usuario,
    mood_usuario):
    puntuacion = 0

    if genero_cancion == genero_usuario:
        puntuacion = puntuacion + 4

    if genero_cancion == segundo_genero:
        puntuacion = puntuacion + 2

    if artista_cancion == artista_usuario:
        puntuacion = puntuacion + 3

    if mood_cancion == mood_usuario:
        puntuacion = puntuacion + 3

    if genero_cancion == genero_usuario and mood_cancion == mood_usuario:
        puntuacion = puntuacion + 2

    if (genero_cancion == genero_usuario or
        genero_cancion == segundo_genero) and artista_cancion == artista_usuario:
        puntuacion = puntuacion + 2

    return puntuacion


def mostrar_recomendacion(
    nombre_cancion,
    artista_cancion,
    puntuacion):
    print("\nCanción recomendada:")
    print(nombre_cancion, "-", artista_cancion)
    print("Compatibilidad:", puntuacion, "puntos")

nombre = input("\n¿Cuál es tu nombre?: ")

print("\n¡Hola,", nombre + "!")
print("Vamos a encontrar música que podría gustarte.")


print("\nSelecciona tu género musical favorito:")
print("1. Pop")
print("2. K-Pop")
print("3. R&B")
print("4. Afrobeats")

opcion = int(input("Selecciona una opción: "))

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
    print("Opción no válida. Se utilizará Pop.")


print("\nSelecciona otro género que también te guste:")
print("1. Pop")
print("2. K-Pop")
print("3. R&B")
print("4. Afrobeats")

opcion = int(input("Selecciona una opción: "))

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
    print("Opción no válida. Se utilizará Pop.")


print("\nSelecciona un artista que te guste:")
print("1. Sabrina Carpenter")
print("2. Dua Lipa")
print("3. The Weeknd")
print("4. Jennie")
print("5. Billie Eilish")
print("6. Ninguno en especial")

opcion = int(input("Selecciona una opción: "))

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


print("\n¿Qué tipo de música quieres escuchar?")
print("1. Energética")
print("2. Para fiesta")
print("3. Relajada")
print("4. Romántica")

opcion = int(input("Selecciona una opción: "))

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
    print("Opción no válida. Se utilizará música energética.")


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

if cancion1 >= cancion2 and cancion1 >= cancion3:

    mostrar_recomendacion(
        "Espresso",
        "Sabrina Carpenter",
        cancion1)

elif cancion2 >= cancion1 and cancion2 >= cancion3:

    mostrar_recomendacion(
        "Mantra",
        "Jennie",
        cancion2)

else:

    mostrar_recomendacion(
        "One Of The Girls",
        "The Weeknd",
        cancion3 )

print("FIN DEL RECOMENDADOR")
