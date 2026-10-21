# TP2_PROGRAMACION_RAY
Trabajo Practico 2
# Catálogo de películas con mínimo de votos

**Autora:** Maria Alfonsina Ray
**Materia:** Programación Orientada a Datos – UCA – 2026  
**Trabajo:** TP2 individual  

## Problema

Cuando queremos buscar una película para ver o recomendar, es muy común ordenarlas por puntaje. El problema es que una película con solo 1 o 2 votos puede tener un 10 de nota y quedar primera en el ranking sin que casi nadie la haya visto. 

Además, los archivos con los datos suelen venir con errores: filas repetidas, películas sin votos o datos incompletos que arruinan la lista si no los limpiamos antes.

## Usuario

Cualquier persona que quiera elegir qué película ver (o armar una lista para recomendar) y busque recomendaciones confiables, pudiendo decidir cuántos votos mínimos debe tener una película para aparecer en el ranking.

## Solución propuesta

Un programa sencillo por consola que lee el catálogo desde un archivo CSV o JSON, filtra los datos con errores y muestra las películas ordenadas, dejando que el usuario elija cuántos votos mínimos exigirles.

## Funcionalidades previstas

Desde un menú en la pantalla, el usuario podrá:

1. Cargar el catálogo desde un archivo CSV o JSON.
2. Buscar películas escribiendo parte de su título.
3. Definir el número mínimo de votos requeridos.
4. Armar la lista ordenada y guardarla en un archivo nuevo.

## Resultado

- Una lista de películas ordenada de mejor a peor nota, mostrando solo las que juntan los votos necesarios. Si dos películas empatan en nota, se desempatan por cantidad de votos y luego por popularidad.
- Un archivo aparte que guarda las filas eliminadas y el motivo por el cual se descartaron.

Esta lista funciona como un ranking de películas **bien calificadas y con respaldo de público**, no como una verdad absoluta de si la película es buena o mala.

## Alcance de la primera versión

**Qué incluye:** lectura de archivos CSV y JSON, revisión y limpieza de errores (guardando los descartes), búsqueda por título, ajuste de votos mínimos y guardado de resultados.

**Qué queda afuera:** filtro por idioma original, filtros por género o año (este conjunto de datos no trae esos campos), aplicaciones web o interfaces gráficas, y recomendaciones con inteligencia artificial.

## Datos

Fuente, licencia, unidad de análisis y variables: ver [`data/README.md`](data/README.md).

## Instalación y ejecución

*(Se completará cuando la aplicación esté terminada.)*

## Organización del código

*(Se completará cuando la aplicación esté terminada.)*

## Decisiones de limpieza

*(Se completará cuando la aplicación esté terminada.)*

## Interpretación y limitaciones

*(Se completará cuando la aplicación esté terminada.)*