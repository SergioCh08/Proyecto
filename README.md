# Recomendador musical

# Contexto
Actualmente existen muchas canciones y artistas diferentes, por lo que algunas veces puede ser difícil encontrar música nueva que sea de nuestro gusto, las plataformas de música suelen mostrar recomendaciones, pero para este proyecto se busca crear un programa sencillo que pueda recomendar canciones según los gustos del usuario.

# Problema
El programa busca ayudar a las personas a encontrar canciones que puedan ser de su agrado sin tener que buscar entre muchas opciones, y para poder hacerlo, el usuario debe de indicar qué géneros musicales le gustan y el programa comparará esa información con una lista de canciones; la idea es que después, el programa mostrará algunas canciones que coincidan con sus gustos.

# ¿Por qué es importante?
Es importante porque permite aplicar la programación a una situación de la vida cotidiana y además, los sistemas de recomendaciones son utilizados en muchas plataformas para ayudar a las personas a encontrar contenido de acuerdo con sus intereses.

# Objetivo
Crear un programa que recomiende canciones al usuario tomando en cuenta sus géneros musicales favoritos, la idea (hasta ahora) es que el usuario indique del 1 al 10 qué tanto le gusta un género musical y también proporciona una puntuación para una canción. El programa multiplica ambos valores para obtener un puntaje de compatibilidad.

# Idea del algoritmo
INICIO

print("RECOMENDADOR MUSICAL")

genero = input("¿Qué género musical te gusta? ")
gusto_genero = int(input("Del 1 al 10, ¿qué tanto te gusta este género? "))

puntuacion_cancion = int()
input("Del 1 al 10, ¿qué tanto te gusta esta canción? ")


Calcular el puntaje de compatibilidad
puntaje = gusto_genero * puntuacion_cancion

Calcular el puntaje máximo posible
puntaje_maximo = 10 * 10

Calcular el porcentaje de compatibilidad
porcentaje = (puntaje / puntaje_maximo) * 100

print("Género seleccionado:", genero)
print("Puntaje de compatibilidad:", puntaje)
print("Porcentaje de compatibilidad:", porcentaje, "%")


# Resultado esperado
El programa deberá mostrar una lista de canciones que coincidan con los gustos musicales que el usuario haya seleccionado.

