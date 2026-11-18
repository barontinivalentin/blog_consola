# blog/validaciones.py
# Reglas lógicas del sistema: validación de la estructura de los posts.

# Se importan los estados válidos desde datos.py (datos.py no importa nada de acá,
# así se evitan los imports circulares)
from blog.datos import estados_post

# Claves que todo post debe tener
CLAVES_OBLIGATORIAS = ("id", "titulo", "contenido", "autor", "tags", "estado")


def validar_post(post):
    """Verifica la estructura de un post. Retorna (True, "válido") o (False, mensaje de error)."""
    # El post tiene que ser un diccionario
    if not isinstance(post, dict):
        return False, "el post no es un diccionario"

    # Todas las claves obligatorias tienen que existir (se usa in)
    for clave in CLAVES_OBLIGATORIAS:
        if clave not in post:
            return False, f'falta la clave "{clave}"'

    # Título y contenido tienen que ser texto y no estar vacíos
    if not isinstance(post["titulo"], str) or post["titulo"].strip() == "":
        return False, "el título está vacío"
    if not isinstance(post["contenido"], str) or post["contenido"].strip() == "":
        return False, "el contenido está vacío"

    # El autor tiene que ser un diccionario con la clave "nombre"
    if not isinstance(post["autor"], dict):
        return False, "el autor no es un diccionario"
    if "nombre" not in post["autor"]:
        return False, 'el autor no tiene la clave "nombre"'

    # Los tags tienen que estar en una lista
    if not isinstance(post["tags"], list):
        return False, "tags no es una lista"

    # El estado tiene que ser uno de los definidos en estados_post
    if post["estado"] not in estados_post:
        return False, f'el estado "{post["estado"]}" no es válido'

    return True, "válido"
