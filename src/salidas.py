"""Guardado de los resultados y de las filas rechazadas en archivos de texto.

Las columnas se separan con punto y coma (;).
"""


def guardar_resultado(peliculas, ruta):
    """Guarda la lista final de películas en un archivo."""
    try:
        with open(ruta, mode="w", encoding="utf-8") as archivo:
            archivo.write("id;titulo;calificacion;votos;popularidad\n")
            for p in peliculas:
                titulo = p.titulo.replace(";", ",")  # para que no se confunda con el separador
                archivo.write(f"{p.id_pelicula};{titulo};{p.calificacion};{p.votos};{p.popularidad}\n")
    except FileNotFoundError:
        raise FileNotFoundError(f"No se pudo guardar en {ruta}: la carpeta no existe.")


def guardar_rechazos(rechazados, ruta):
    """Guarda las filas rechazadas, con el motivo, en un archivo."""
    try:
        with open(ruta, mode="w", encoding="utf-8") as archivo:
            archivo.write("id;titulo;motivo\n")
            for rechazo in rechazados:
                fila = rechazo["fila"]
                titulo = str(fila.get("title", "")).replace(";", ",")
                archivo.write(f"{fila.get('id', '')};{titulo};{rechazo['motivo']}\n")
    except FileNotFoundError:
        raise FileNotFoundError(f"No se pudo guardar en {ruta}: la carpeta no existe.")