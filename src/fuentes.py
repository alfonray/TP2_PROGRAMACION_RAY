"""Fuentes de datos: lectura de archivos CSV y JSON.

Las dos fuentes devuelven lo mismo: una lista de diccionarios, donde cada
diccionario es una película con sus campos (id, title, vote_average, ...).
"""

import csv
import json


class FuenteDatos:
    """Clase base: define qué tiene que saber hacer cualquier fuente de datos."""

    def cargar(self, ruta):
        """Lee el archivo y devuelve una lista de diccionarios."""
        raise NotImplementedError("Cada fuente debe implementar cargar()")


class FuenteCSV(FuenteDatos):
    """Lee películas desde un archivo CSV."""

    def cargar(self, ruta):
        try:
            with open(ruta, mode="r", encoding="utf-8", newline="") as archivo:
                lector = csv.DictReader(archivo)
                return list(lector)
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo CSV: {ruta}")


class FuenteJSON(FuenteDatos):
    """Lee películas desde un archivo JSON (una lista de objetos)."""

    def cargar(self, ruta):
        try:
            with open(ruta, mode="r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo JSON: {ruta}")
        except json.JSONDecodeError:
            raise ValueError(f"El archivo no es un JSON válido: {ruta}")

        if not isinstance(datos, list):
            raise ValueError("El JSON debe ser una lista de objetos (una por película).")
        return datos