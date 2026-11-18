# blog/operaciones.py
# Acciones del menú: conectan lo que pide el usuario (menu.py) con los métodos de Blog.
# Cada función recibe el objeto Blog por parámetro.

from blog.menu import pedir_texto, pedir_datos_post, mostrar_posts, mostrar_validacion
from blog.modelos import Autor
from blog.datos import perfil_autor


def accion_listar(blog):
    """Opción 1: muestra todos los posts del blog."""
    mostrar_posts(blog.listar_posts(), "El blog todavía no tiene posts.")


def accion_buscar(blog):
    """Opción 2: pide un término y muestra los posts cuyo título lo contiene."""
    termino = pedir_texto("Buscar por titulo: ")
    if termino == "":
        print("La búsqueda no puede estar vacía.")
        return
    mostrar_posts(blog.buscar_por_titulo(termino), f"No se encontraron posts con '{termino}' en el título.")


def accion_filtrar(blog):
    """Opción 3: pide un tag y muestra los posts que lo tienen."""
    tag = pedir_texto("Ingresá un tag: ")
    if tag == "":
        print("El tag no puede estar vacío.")
        return
    mostrar_posts(blog.filtrar_por_tag(tag), f"No hay posts con el tag '{tag}'.")


def accion_crear(blog):
    """Opción 4: pide los datos, crea un objeto Post y lo agrega al blog."""
    datos = pedir_datos_post()
    # El autor de los posts nuevos es un objeto Autor creado desde el perfil del blog
    autor = Autor.from_dict(perfil_autor)
    nuevo = blog.crear_post(datos["titulo"], datos["contenido"], autor, datos["tags"], datos["estado"])
    print(f"Post creado con id {nuevo.id}. Elegí la opción 6 para guardarlo en posts.json.")


def accion_validar(blog):
    """Opción 5: valida todos los posts y muestra el resultado."""
    mostrar_validacion(blog.validar_posts())
