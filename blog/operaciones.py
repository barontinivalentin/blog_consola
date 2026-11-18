# blog/operaciones.py
# Operaciones principales del blog: listar, buscar y filtrar posts.
# Todas las funciones reciben los datos por parámetro.


def obtener_nombre_autor(post):
    """Retorna el nombre del autor de forma segura, aunque el dato esté mal cargado."""
    autor = post.get("autor")
    if isinstance(autor, dict):
        return autor.get("nombre", "Autor desconocido")
    return "Autor desconocido"


def formatear_post(post):
    """Retorna una línea de texto con título, autor y estado del post."""
    # .get() evita un KeyError si falta alguna clave
    titulo = post.get("titulo") or "(sin título)"
    estado = post.get("estado", "sin estado")
    return f"- {titulo} | Autor: {obtener_nombre_autor(post)} | Estado: {estado}"


def listar_posts(lista):
    """Muestra todos los posts de la lista con título, autor y estado."""
    if len(lista) == 0:
        print("No hay posts para mostrar.")
        return

    print("\nPosts disponibles:")
    for post in lista:
        print(formatear_post(post))


def buscar_por_titulo(lista, termino):
    """Retorna los posts cuyo título contiene el término (sin importar mayúsculas)."""
    resultados = []
    for post in lista:
        titulo = post.get("titulo", "")
        # Se usa .lower() en ambos lados para ignorar mayúsculas/minúsculas
        if isinstance(titulo, str) and termino.lower() in titulo.lower():
            resultados.append(post)
    return resultados


def filtrar_por_tag(lista, tag):
    """Retorna los posts que tienen el tag indicado (sin importar mayúsculas)."""
    resultados = []
    for post in lista:
        tags = post.get("tags", [])
        # Si tags no es una lista, el post se saltea para no generar errores
        if not isinstance(tags, list):
            continue
        for t in tags:
            if isinstance(t, str) and t.lower() == tag.lower():
                resultados.append(post)
                break  # ya coincidió, pasar al siguiente post
    return resultados


def mostrar_resultados(resultados, mensaje_vacio):
    """Muestra los posts encontrados o un mensaje si no hay resultados."""
    if len(resultados) == 0:
        print(mensaje_vacio)
    else:
        print(f"\nSe encontraron {len(resultados)} post(s):")
        for post in resultados:
            print(formatear_post(post))
