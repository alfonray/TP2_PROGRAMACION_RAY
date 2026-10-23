"""La clase Pelicula y la conversión de una fila de datos en Pelicula."""

import re

# El id es un número entero escrito solo con dígitos (por ejemplo: 1338799).
PATRON_ID = re.compile(r"^\d+$")


class Pelicula:
    """Una película del catálogo, con sus datos ya validados."""

    def __init__(self, id_pelicula, titulo, calificacion, votos, popularidad):
        self.id_pelicula = id_pelicula
        self.titulo = titulo
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

    return Pelicula(id_pelicula, titulo, calificacion, votos, popularidad)