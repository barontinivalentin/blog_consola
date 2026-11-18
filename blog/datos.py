# blog/datos.py
# Persistencia del sistema: carga y guardado de los posts en posts.json.
# También guarda los datos iniciales que se usan si todavía no existe el archivo.

import json
import os

from blog.modelos import Post

# Ruta de posts.json: siempre en la carpeta raíz del proyecto (al lado de main.py)
RUTA_JSON = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "posts.json")

# ---------------------------------------------
# DATOS INICIALES (continuidad de los módulos anteriores)
# ---------------------------------------------

# Diccionario con el perfil del autor
perfil_autor = {
    "nombre": "Ana López",
    "bio": "Desarrolladora web y creadora de contenido sobre programación.",
    "especialidad": "Python y Django",
    "redes_sociales": ["@ana_dev", "@ana_python"]
}

# Set de etiquetas del blog (los duplicados se eliminan solos)
etiquetas_blog = {"Python", "Django", "Web", "Backend", "Python"}

# Posts iniciales en formato diccionario. Se usan solo si posts.json no existe
# o no se puede leer. El último tiene errores a propósito para probar la validación.
posts_iniciales = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "En este post veremos cómo empezar a programar con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Qué es Django",
        "contenido": "Django es un framework web creado con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Django", "Web"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con listas",
        "contenido": "Las listas permiten guardar varios elementos en una sola variable.",
        "autor": perfil_autor,
        "tags": ["Python", "Listas"],
        "estado": "archivado"
    },
    {
        "id": 4,
        "titulo": "",
        "contenido": "Este post tiene el título vacío y un estado que no existe.",
        "autor": perfil_autor,
        "tags": ["Python"],
        "estado": "eliminado"
    }
]


# ---------------------------------------------
# FUNCIONES DE CARGA Y GUARDADO
# ---------------------------------------------

def dicts_a_posts(lista_dicts):
    """Convierte una lista de diccionarios en objetos Post. Saltea los que estén incompletos."""
    posts = []
    for posicion, datos in enumerate(lista_dicts, start=1):
        try:
            posts.append(Post.from_dict(datos))
        except (ValueError, TypeError) as error:
            print(f"Aviso: el post en la posición {posicion} no se pudo cargar ({error}).")
    return posts


def cargar_posts(ruta=RUTA_JSON):
    """Lee posts.json y retorna una lista de objetos Post.
    Si el archivo no existe, está vacío o es inválido, usa los datos iniciales."""
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print("No se encontró posts.json: se cargan los posts iniciales.")
        return dicts_a_posts(posts_iniciales)
    except OSError as error:
        print(f"No se pudo leer posts.json ({error}): se cargan los posts iniciales.")
        return dicts_a_posts(posts_iniciales)

    if contenido.strip() == "":
        print("posts.json está vacío: se cargan los posts iniciales.")
        return dicts_a_posts(posts_iniciales)

    try:
        datos = json.loads(contenido)
    except json.JSONDecodeError as error:
        print(f"posts.json tiene contenido inválido (línea {error.lineno}): se cargan los posts iniciales.")
        print("El archivo no se modifica hasta que elijas guardar.")
        return dicts_a_posts(posts_iniciales)

    if not isinstance(datos, list):
        print("posts.json no contiene una lista de posts: se cargan los posts iniciales.")
        return dicts_a_posts(posts_iniciales)

    posts = dicts_a_posts(datos)
    print(f"Se cargaron {len(posts)} post(s) desde posts.json.")
    return posts


def guardar_posts(blog, ruta=RUTA_JSON):
    """Convierte los posts del blog a diccionarios y los guarda en posts.json.
    Retorna True si se guardó bien y False si hubo un error."""
    try:
        # Los objetos se convierten a diccionarios antes de pasarlos a json
        datos = blog.to_list()
        texto = json.dumps(datos, ensure_ascii=False, indent=4)
    except (TypeError, AttributeError) as error:
        # Pasa si algún dato no es compatible con JSON (por ejemplo, un objeto sin convertir)
        print(f"Error: hay datos que no se pueden convertir a JSON ({error}). No se guardó nada.")
        return False

    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(texto)
    except OSError as error:
        print(f"Error: no se pudo escribir posts.json ({error}).")
        return False

    blog.cambios_sin_guardar = False
    print(f"Se guardaron {len(datos)} post(s) en posts.json.")
    return True
