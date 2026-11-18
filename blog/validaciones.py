# blog/validaciones.py
# Reglas lógicas del sistema: estados válidos y validación de los posts.
# Este módulo no importa nada del paquete, así se evitan los imports circulares.

# Tupla con los estados posibles de un post
estados_post = ("borrador", "publicado", "archivado")

# Claves que un post debe tener en el archivo JSON para poder reconstruirse
CLAVES_OBLIGATORIAS = ("id", "titulo", "contenido", "autor", "tags", "estado")


def validar_post(post):
    """Verifica los datos de un objeto Post. Retorna (True, "válido") o (False, mensaje de error)."""
    # Título y contenido tienen que ser texto y no estar vacíos
    if not isinstance(post.titulo, str) or post.titulo.strip() == "":
        return False, "el título está vacío"
    if not isinstance(post.contenido, str) or post.contenido.strip() == "":
        return False, "el contenido está vacío"

    # El autor tiene que ser un objeto con nombre (una instancia de Autor)
    nombre_autor = getattr(post.autor, "nombre", None)
    if not isinstance(nombre_autor, str) or nombre_autor.strip() == "":
        return False, "el autor no tiene nombre"

    # Los tags tienen que estar en una lista
    if not isinstance(post.tags, list):
        return False, "tags no es una lista"

    # El estado tiene que ser uno de los definidos en estados_post
    if post.estado not in estados_post:
        return False, f'el estado "{post.estado}" no es válido'

    return True, "válido"


def claves_faltantes(diccionario, claves):
    """Retorna la lista de claves que no están en el diccionario (se usa in)."""
    return [clave for clave in claves if clave not in diccionario]
