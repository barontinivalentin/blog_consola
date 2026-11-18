# blog/modelos.py
# Clases principales del sistema: Autor, Post y Blog.

from blog.validaciones import validar_post, claves_faltantes, CLAVES_OBLIGATORIAS


class Autor:
    """Representa a una persona autora del blog."""

    def __init__(self, nombre, bio="", especialidad="", redes_sociales=None):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        # Se crea una lista nueva para que cada autor tenga la suya
        self.redes_sociales = list(redes_sociales) if redes_sociales else []

    def to_dict(self):
        """Convierte el autor a diccionario para poder guardarlo en JSON."""
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales
        }

    @classmethod
    def from_dict(cls, datos):
        """Crea un Autor a partir de un diccionario cargado desde JSON."""
        if not isinstance(datos, dict):
            raise ValueError("el autor no es un diccionario")
        if "nombre" not in datos:
            raise ValueError('el autor no tiene la clave "nombre"')
        # .get() da un valor por defecto para los datos opcionales
        return cls(
            nombre=datos["nombre"],
            bio=datos.get("bio", ""),
            especialidad=datos.get("especialidad", ""),
            redes_sociales=datos.get("redes_sociales", [])
        )

    def __str__(self):
        return self.nombre


class Post:
    """Representa una publicación del blog. Su autor es un objeto Autor."""

    def __init__(self, id, titulo, contenido, autor, tags, estado="borrador"):
        # Composición: el post solo acepta una instancia de Autor
        if not isinstance(autor, Autor):
            raise TypeError("el autor de un post tiene que ser un objeto Autor")
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

    def to_dict(self):
        """Convierte el post (y su autor) a diccionario para poder guardarlo en JSON."""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dict(),
            "tags": self.tags,
            "estado": self.estado
        }

    @classmethod
    def from_dict(cls, datos):
        """Crea un Post a partir de un diccionario. Lanza ValueError si está incompleto."""
        if not isinstance(datos, dict):
            raise ValueError("el post no es un diccionario")
        faltan = claves_faltantes(datos, CLAVES_OBLIGATORIAS)
        if faltan:
            raise ValueError(f"faltan las claves: {', '.join(faltan)}")
        return cls(
            id=datos["id"],
            titulo=datos["titulo"],
            contenido=datos["contenido"],
            autor=Autor.from_dict(datos["autor"]),
            tags=datos["tags"],
            estado=datos["estado"]
        )

    def tiene_tag(self, tag):
        """Retorna True si el post tiene el tag indicado (sin importar mayúsculas)."""
        if not isinstance(self.tags, list):
            return False
        return any(isinstance(t, str) and t.lower() == tag.lower() for t in self.tags)

    def __str__(self):
        titulo = self.titulo or "(sin título)"
        return f"- [{self.id}] {titulo} | Autor: {self.autor.nombre} | Estado: {self.estado}"


class Blog:
    """Centraliza la lógica del sistema y guarda la lista de objetos Post."""

    def __init__(self, nombre, posts=None):
        self.nombre = nombre
        self.posts = list(posts) if posts else []
        # Indica si hubo cambios que todavía no se guardaron en el JSON
        self.cambios_sin_guardar = False

    def obtener_posts(self):
        """Retorna todos los posts cargados."""
        return self.posts

    def listar_posts(self):
        """Retorna la lista de posts para mostrarla (igual que obtener_posts)."""
        return self.obtener_posts()

    def buscar_por_titulo(self, termino):
        """Retorna los posts cuyo título contiene el término (sin importar mayúsculas)."""
        return [
            post for post in self.posts
            if isinstance(post.titulo, str) and termino.lower() in post.titulo.lower()
        ]

    def filtrar_por_tag(self, tag):
        """Retorna los posts que tienen el tag indicado (sin importar mayúsculas)."""
        return [post for post in self.posts if post.tiene_tag(tag)]

    def siguiente_id(self):
        """Calcula el id del próximo post (el mayor id actual + 1)."""
        ids = [post.id for post in self.posts if isinstance(post.id, int)]
        return max(ids) + 1 if ids else 1

    def crear_post(self, titulo, contenido, autor, tags, estado="borrador"):
        """Crea un objeto Post, lo agrega al blog y lo retorna."""
        nuevo = Post(self.siguiente_id(), titulo, contenido, autor, tags, estado)
        self.posts.append(nuevo)
        self.cambios_sin_guardar = True
        return nuevo

    def validar_posts(self):
        """Valida cada post con validar_post(). Retorna una lista de (post, es_valido, mensaje)."""
        resultados = []
        for post in self.posts:
            es_valido, mensaje = validar_post(post)
            resultados.append((post, es_valido, mensaje))
        return resultados

    def to_list(self):
        """Convierte todos los posts a una lista de diccionarios (formato para JSON)."""
        return [post.to_dict() for post in self.posts]
