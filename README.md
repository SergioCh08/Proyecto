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


# Resultado esperado
El programa deberá mostrar una lista de canciones que coincidan con los gustos musicales que el usuario haya seleccionado.

