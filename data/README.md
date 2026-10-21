# Datos

## Fuente

- **Nombre:** Most watched movies of 2026
- **Autor:** Adarsh Maurya (usuario de Kaggle: da1adarshmaurya)
- **URL:** https://www.kaggle.com/datasets/da1adarshmaurya/most-watched-movies-of-2026
- **Licencia:** Creative Commons Atribución 4.0 Internacional (CC BY 4.0)
- **Fecha de consulta:** 21 de octubre de 2026
- **Archivo original:** `trending_movies.csv`

Según Kaggle, el conjunto original tiene frecuencia de actualización
semanal; al momento de la consulta figuraba como actualizado hace dos
meses. La copia usada en este trabajo corresponde a la fecha de consulta
indicada.

## Modificaciones respecto del original

En este repositorio se conserva únicamente una muestra reducida del
archivo, junto con su versión equivalente en JSON. Los datos no fueron
alterados a mano; la limpieza se realiza mediante el programa y los
registros rechazados se guardan aparte con su motivo.

## Unidad de análisis

Cada fila representa una película en tendencia.

## Variables utilizadas

| Variable | Descripción |
|---|---|
| `id` | Identificador numérico de la película |
| `title` | Título de la película |
| `original_language` | Código de idioma original (dos letras, por ejemplo `en`, `es`) |
| `vote_average` | Valoración media |
| `vote_count` | Cantidad de votos recibidos |
| `popularity` | Índice de popularidad |

Las columnas `original_title`, `overview` y `adult` existen en el original,
pero no se utilizan en esta versión.

## Tamaño

El archivo original tiene 9.993 filas y 9 columnas.
Aquí se incluye una muestra pequeña (ver `data/`).

## Limitaciones conocidas

- Hay filas completamente duplicadas (alrededor del 26 %) y algunos
  identificadores repetidos con datos distintos.
- Hay películas con `vote_count = 0` y `vote_average = 0`: no significan
  "mal valoradas", sino "sin datos".
- Algunas películas no tienen descripción (`overview`).
- El conjunto no incluye géneros ni fecha de estreno.
- La documentación del autor no detalla las unidades de `popularity`.