from fuentes import FuenteCSV, FuenteJSON
from pipeline import validar_y_limpiar_datos, filtrar_catalogo


def ejecutar_aplicacion(ruta_archivo: str, formato: str, min_votos: int = 50, min_calificacion: float = 6.0):
    print("==================================================")
    print("   CATÁLOGO Y BUSCADOR DE PELÍCULAS TRENDING      ")
    print("==================================================")

    # 1. Cargar datos según el formato seleccionado
    if formato.lower() == "csv":
        fuente = FuenteCSV()
    elif formato.lower() == "json":
        fuente = FuenteJSON()
    else:
        raise ValueError("Formato no soportado. Debe ser 'csv' o 'json'.")

    datos_brutos = fuente.cargar(ruta_archivo)
    print(f"-> Archivo cargado ({formato.upper()}): {len(datos_brutos)} registros leídos.")

    # 2. Validar y limpiar
    validas, rechazados = validar_y_limpiar_datos(datos_brutos)
    print(f"-> Películas válidas: {len(validas)} | Registros rechazados: {len(rechazados)}")

    # 3. Aplicar filtro y ordenamiento
    resultados = filtrar_catalogo(validas, min_votos=min_votos, min_calificacion=min_calificacion)

    # 4. Mostrar resultados por consola
    print(f"\nResultados (Mínimo {min_votos} votos y nota >= {min_calificacion}):")
    print("-" * 75)
    print(f"{'ID':<10} | {'TÍTULO':<35} | {'NOTA':<6} | {'VOTOS':<8} | {'POPULARIDAD'}")
    print("-" * 75)
    
    for p in resultados[:10]:  # Muestra las primeras 10 recomendaciones
        print(f"{p.id_pelicula:<10} | {p.titulo[:33]:<35} | {p.calificacion:<6.2f} | {p.votos:<8} | {p.popularidad:.2f}")
    
    print("-" * 75)


if __name__ == "__main__":
    # Prueba de ejecución utilizando la muestra generada
    ejecutar_aplicacion("data/trending_movies_muestra.csv", formato="csv", min_votos=50, min_calificacion=6.0)