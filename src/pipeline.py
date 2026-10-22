"""Validación, limpieza y filtrado del catálogo de películas."""

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