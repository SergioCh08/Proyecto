# Recomendador musical

# Contexto
Actualmente existen muchas canciones y artistas diferentes, por lo que algunas veces puede ser difícil encontrar música nueva que sea de nuestro gusto, las plataformas de música suelen mostrar recomendaciones, pero para este proyecto se busca crear un programa sencillo que pueda recomendar canciones según los gustos del usuario.

# Problema
El programa busca ayudar a las personas a encontrar canciones que puedan ser de su agrado sin tener que buscar entre muchas opciones, y para poder hacerlo, el usuario debe de indicar qué géneros musicales le gustan y el programa comparará esa información con una lista de canciones; la idea es que después, el programa mostrará algunas canciones que coincidan con sus gustos.

# ¿Por qué es importante?
Es importante porque permite aplicar la programación a una situación de la vida cotidiana y además, los sistemas de recomendaciones son utilizados en muchas plataformas para ayudar a las personas a encontrar contenido de acuerdo con sus intereses.

# Objetivo
Crear un programa que recomiende canciones al usuario tomando en cuenta sus géneros musicales favoritos, la idea (hasta ahora) es que el usuario indique del 1 al 10 qué tanto le gusta un género musical y también proporciona una puntuación para una canción. El programa multiplica ambos valores para obtener un puntaje de compatibilidad.

# Avance 1 (Corregido)
Entradas:

Calificación de cada una de las canciones — número entero.
Información previamente almacenada de cada canción: nombre, artista, género y canciones similares.

Salidas:

Canción o canciones que obtuvieron las mayores calificaciones.
Lista de canciones recomendadas de acuerdo con las preferencias del usuario.

Pseudocódigo:

INICIO.
1. Mostrar el nombre del programa: "RECOMENDADOR MUSICAL".
2. Solicitar el nombre del usuario.
3. Mostrar al usuario una lista de 7 canciones previamente seleccionadas.
4. Solicitar al usuario una calificación del 1 al 10 para cada una de las 7 canciones.
5. Guardar las calificaciones proporcionadas por el usuario.
6. Comparar las calificaciones obtenidas por las 7 canciones.
7. Identificar las canciones que obtuvieron las mayores calificaciones.
8. Consultar la información de las canciones con mayor calificación para identificar su género, artista y estilo musical.
9. Consultar las listas de canciones asociadas a las canciones mejor calificadas.
10. Seleccionar canciones de esas listas que no hayan sido calificadas previamente por el usuario.
11. Organizar las canciones seleccionadas de acuerdo con la preferencia obtenida por el usuario.
12. Mostrar al usuario las canciones recomendadas.
13. Mostrar un mensaje indicando que las recomendaciones fueron seleccionadas de acuerdo con sus preferencias musicales.
    
FIN.

# Avance 2

puntaje_total = p1 + p2 + p3 + p4 + p5 + p6 + p7

promedio = puntaje_total / 7

puntaje_final = promedio * 10

puntaje_maximo = 10 * 10

porcentaje = (puntaje / puntaje_maximo) * 100

# Avance 3

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



# Resultado esperado
El programa deberá mostrar una lista de canciones que coincidan con los gustos musicales que el usuario haya seleccionado.

