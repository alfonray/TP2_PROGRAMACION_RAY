from fuentes import FuenteCSV, FuenteJSON
from pipeline import validar_y_limpiar_datos, filtrar_catalogo, guardar_resultado, guardar_rechazos


def ejecutar_aplicacion(ruta, formato, min_votos, min_calificacion):
    # 1. Cargar los datos
    if formato == "csv":
        fuente = FuenteCSV()
    elif formato == "json":
        fuente = FuenteJSON()
    else:
        raise ValueError("Formato no soportado. Debe ser 'csv' o 'json'.")

    datos = fuente.cargar(ruta)
    print("Registros leídos:", len(datos))

    # 2. Validar y limpiar
    validas, rechazados = validar_y_limpiar_datos(datos)
    print("Películas válidas:", len(validas), "| Rechazadas:", len(rechazados))

    # 3. Filtrar y ordenar
    resultados = filtrar_catalogo(validas, min_votos, min_calificacion)

    # 4. Guardar los archivos de salida
    guardar_resultado(resultados, "outputs/resultado.csv")
    guardar_rechazos(rechazados, "outputs/rechazados.csv")
    print("Archivos guardados en la carpeta outputs")

    # 5. Mostrar las 10 primeras
    print("Películas que cumplen el filtro:", len(resultados))
    for p in resultados[:10]:
        print(p.id_pelicula, "|", p.titulo, "|", p.calificacion, "|", p.votos)


if __name__ == "__main__":
    ejecutar_aplicacion("data/trending_movies_muestra.csv", "csv", 50, 6.0)