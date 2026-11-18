# blog/menu.py
# Menú e interacción con el usuario: todo el manejo de input() y print() de resultados.

from blog.validaciones import estados_post


def mostrar_menu():
    """Muestra el menú y retorna la opción elegida como número (o None si no es un número)."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Crear nuevo post")
    print("5. Validar posts")
    print("6. Guardar posts en JSON")
    print("7. Salir")

    # try-except: si el usuario escribe texto, int() falla y el programa no se cierra
    try:
        return int(input("Elegí una opción: "))
    except ValueError:
        print("Error: tenés que ingresar un número del 1 al 7.")
        return None


def pedir_texto(mensaje):
    """Pide un texto por consola y lo retorna sin espacios al principio ni al final."""
    return input(mensaje).strip()


def pedir_texto_obligatorio(mensaje):
    """Pide un texto hasta que el usuario escriba algo que no esté vacío."""
    while True:
        texto = pedir_texto(mensaje)
        if texto != "":
            return texto
        print("Este campo no puede quedar vacío.")


def pedir_si_no(mensaje):
    """Pregunta por sí o no. Retorna True si la respuesta empieza con 's'."""
    return pedir_texto(mensaje).lower().startswith("s")


def pedir_datos_post():
    """Pide los datos de un post nuevo y los retorna en un diccionario."""
    print("\n--- NUEVO POST ---")
    titulo = pedir_texto_obligatorio("Título: ")
    contenido = pedir_texto_obligatorio("Contenido: ")

    # Tags separados por coma; se descartan los vacíos
    texto_tags = pedir_texto("Tags separados por coma (ej: Python, Web): ")
    tags = [tag.strip() for tag in texto_tags.split(",") if tag.strip() != ""]

    # Estado: se elige por número; Enter deja "borrador"
    print("Estados posibles:")
    for numero, estado in enumerate(estados_post, start=1):
        print(f"  {numero}. {estado}")
    estado = "borrador"
    eleccion = pedir_texto("Elegí un estado (Enter = borrador): ")
    if eleccion != "":
        try:
            estado = estados_post[int(eleccion) - 1]
        except (ValueError, IndexError):
            print("Estado inválido: se usa 'borrador'.")

    return {"titulo": titulo, "contenido": contenido, "tags": tags, "estado": estado}


def mostrar_posts(posts, mensaje_vacio="No hay posts para mostrar."):
    """Muestra una lista de objetos Post o un mensaje si está vacía."""
    if len(posts) == 0:
        print(mensaje_vacio)
        return
    print(f"\n{len(posts)} post(s):")
    for post in posts:
        print(post)


def mostrar_validacion(resultados):
    """Muestra el resultado de Blog.validar_posts()."""
    if len(resultados) == 0:
        print("No hay posts para validar.")
        return
    print("\nResultado de la validación:")
    for post, es_valido, mensaje in resultados:
        if es_valido:
            print(f"Post {post.id}: válido")
        else:
            print(f"Post {post.id}: error - {mensaje}")
