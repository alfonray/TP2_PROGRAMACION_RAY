import sys
import os

# Puente para que este archivo pueda leer los códigos de la carpeta "src"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from dominio import convertir_fila
from fuentes import FuenteCSV, FuenteJSON

print("--- INICIANDO PRUEBAS ---")

# 1. Caso normal: Le pasamos datos correctos y vemos si los lee bien
fila_correcta = {"id": "123", "title": "Peli OK", "vote_average": "8.5", "vote_count": "100", "popularity": "50.0"}
pelicula = convertir_fila(fila_correcta)

if pelicula.titulo == "Peli OK":
    print("Prueba 1 (Caso normal): PASÓ")
else:
    print("Prueba 1 (Caso normal): FALLÓ")


# 2. Caso inválido: Le pasamos un ID con letras para ver si el programa lo rechaza
fila_invalida = {"id": "ABC", "title": "Peli Rota", "vote_average": "8.5", "vote_count": "100", "popularity": "50.0"}

try:
    # Intentamos convertir la fila mala. Si el programa está bien hecho, esto va a fallar.
    convertir_fila(fila_invalida)
    print("Prueba 2 (Caso límite): FALLÓ (Debería haber saltado un error por el ID con letras)")
except ValueError:
    # Si salta el ValueError (que es lo que programaste para IDs malos), la prueba es un éxito.
    print("Prueba 2 (Caso límite): PASÓ (El error saltó correctamente para proteger el sistema)")


# 3. Equivalencia: Verificamos que CSV y JSON lean la misma cantidad de filas
fuente_csv = FuenteCSV()
fuente_json = FuenteJSON()

datos_csv = fuente_csv.cargar("data/trending_movies_muestra.csv")
datos_json = fuente_json.cargar("data/trending_movies_muestra.json")

if len(datos_csv) == len(datos_json):
    print("Prueba 3 (Equivalencia CSV/JSON): PASÓ")
else:
    print("Prueba 3 (Equivalencia CSV/JSON): FALLÓ")

print("--- PRUEBAS TERMINADAS ---")