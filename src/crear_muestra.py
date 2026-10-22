"""Crea la muestra reducida del dataset en formatos CSV y JSON equivalentes."""

import csv
import json
import random

SEMILLA = 42
N_MUESTRA = 140

RUTA_CSV_SALIDA = "data/trending_movies_muestra.csv"
RUTA_JSON_SALIDA = "data/trending_movies_muestra.json"


def obtener_nota(pelicula):
    """Devuelve la calificación de la película convertida a número.
    Si falta la nota o viene vacía, devuelve 0.
    """
    return float(pelicula.get("vote_average", 0))


def main():
    ruta_original = input("Ruta del archivo trending_movies.csv original: ").strip('"\' ')

    # 1. Leer el archivo CSV original
    with open(ruta_original, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        columnas = lector.fieldnames
        filas = list(lector)

    # 2. Fijar semilla y tomar una muestra aleatoria reproducible
    random.seed(SEMILLA)
    muestra = random.sample(filas, N_MUESTRA)

    # 3. Agregar 10 filas duplicadas a propósito para probar la etapa de limpieza
    muestra += muestra[:10]

    # 4. Ordenar la lista de películas de mayor a menor según su calificación
    muestra.sort(key=obtener_nota, reverse=True)

    # 5. Guardar la muestra en archivo CSV
    with open(RUTA_CSV_SALIDA, mode="w", encoding="utf-8", newline="") as f_csv:
        escritor = csv.DictWriter(f_csv, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(muestra)

    # 6. Guardar la muestra en archivo JSON
    with open(RUTA_JSON_SALIDA, mode="w", encoding="utf-8") as f_json:
        json.dump(muestra, f_json, ensure_ascii=False, indent=2)

    print(f"Muestra creada con éxito: {len(muestra)} filas guardadas en la carpeta data/")


if __name__ == "__main__":
    main()