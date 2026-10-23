"""Validación, limpieza y filtrado del catálogo de películas."""

import csv
import re

# El id es un número entero escrito solo con dígitos (por ejemplo: 1338799).
PATRON_ID = re.compile(r"^\d+$")
# El idioma original es un código de dos letras minúsculas (por ejemplo: en, es, ja).
PATRON_IDIOMA = re.compile(r"^[a-z]{2}$")


class Pelicula:
    """Una película del catálogo, con sus datos ya validados."""

    def __init__(self, id_pelicula, titulo, idioma, calificacion, votos, popularidad):
        self.id_pelicula = id_pelicula
        self.titulo = titulo
        self.idioma = idioma
        self.calificacion = calificacion
        self.votos = votos
        self.popularidad = popularidad

    def tiene_respaldo(self, min_votos):
        """Devuelve True si la película tiene al menos min_votos votos."""
        return self.votos >= min_votos


def convertir_fila(fila):
    """Convierte una fila (diccionario con textos) en una Pelicula.

    Si algún dato no es válido, lanza ValueError explicando el motivo.
    """
    id_pelicula = str(fila.get("id", "")).strip()
    if not PATRON_ID.match(id_pelicula):
        raise ValueError("id con formato inválido")

    titulo = str(fila.get("title", "")).strip()
    if titulo == "":
        raise ValueError("título vacío")

    idioma = str(fila.get("original_language", "")).strip()
    if not PATRON_IDIOMA.match(idioma):
        raise ValueError("idioma con formato inválido")

    try:
        calificacion = float(fila.get("vote_average", ""))
        votos = int(fila.get("vote_count", ""))
        popularidad = float(fila.get("popularity", ""))
    except (ValueError, TypeError):
        raise ValueError("calificación, votos o popularidad no son números")

    if not 0 <= calificacion <= 10:
        raise ValueError("calificación fuera de rango (debe estar entre 0 y 10)")
    if votos < 0:
        raise ValueError("cantidad de votos negativa")
    if popularidad < 0:
        raise ValueError("popularidad negativa")

    return Pelicula(id_pelicula, titulo, idioma, calificacion, votos, popularidad)


def validar_y_limpiar_datos(datos):
    """Separa las filas válidas de las rechazadas.

    Devuelve dos listas:
    - validas: objetos Pelicula (sin ids repetidos)
    - rechazados: diccionarios con la fila original y el motivo del rechazo
    """
    validas = []
    rechazados = []
    ids_vistos = set()

    for fila in datos:
        try:
            pelicula = convertir_fila(fila)
        except ValueError as error:
            rechazados.append({"fila": fila, "motivo": str(error)})
            continue

        if pelicula.id_pelicula in ids_vistos:
            rechazados.append({"fila": fila, "motivo": "id repetido (se conserva la primera aparición)"})
            continue

        ids_vistos.add(pelicula.id_pelicula)
        validas.append(pelicula)

    return validas, rechazados


def clave_orden(pelicula):
    """Criterio de orden: calificación, luego votos, luego popularidad."""
    return (pelicula.calificacion, pelicula.votos, pelicula.popularidad)


def filtrar_catalogo(peliculas, min_votos=50, min_calificacion=0):
    """Filtra las películas y las ordena de mejor a peor.

    - Se quedan solo las que tienen al menos min_votos votos y una
      calificación mayor o igual a min_calificacion.
    - Se ordenan por calificación (de mayor a menor). Si empatan, desempata
      la cantidad de votos y luego la popularidad.
    """
    if min_votos < 0:
        raise ValueError("El mínimo de votos no puede ser negativo.")
    if not 0 <= min_calificacion <= 10:
        raise ValueError("La calificación mínima debe estar entre 0 y 10.")

    seleccionadas = []
    for pelicula in peliculas:
        if pelicula.tiene_respaldo(min_votos) and pelicula.calificacion >= min_calificacion:
            seleccionadas.append(pelicula)

    seleccionadas.sort(key=clave_orden, reverse=True)
    return seleccionadas
def guardar_resultado(peliculas, ruta):
    """Guarda la lista final de películas en un archivo CSV."""
    columnas = ["id", "titulo", "idioma", "calificacion", "votos", "popularidad"]

    filas = []
    for p in peliculas:
        fila = {
            "id": p.id_pelicula,
            "titulo": p.titulo,
            "idioma": p.idioma,
            "calificacion": p.calificacion,
            "votos": p.votos,
            "popularidad": p.popularidad,
        }
        filas.append(fila)

    try:
        with open(ruta, mode="w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(filas)
    except FileNotFoundError:
        raise FileNotFoundError(f"No se pudo guardar en {ruta}: la carpeta no existe.")


def guardar_rechazos(rechazados, ruta):
    """Guarda las filas rechazadas, con el motivo, en un archivo CSV."""
    columnas = ["id", "titulo", "motivo"]

    filas = []
    for rechazo in rechazados:
        original = rechazo["fila"]
        fila = {
            "id": original.get("id", ""),
            "titulo": original.get("title", ""),
            "motivo": rechazo["motivo"],
        }
        filas.append(fila)

    try:
        with open(ruta, mode="w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(filas)
    except FileNotFoundError:
        raise FileNotFoundError(f"No se pudo guardar en {ruta}: la carpeta no existe.")