# blog/datos.py
# Estructuras de datos base del blog (continuidad de los módulos anteriores)

# Diccionario con el perfil del autor
perfil_autor = {
    "nombre": "Ana López",
    "bio": "Desarrolladora web y creadora de contenido sobre programación.",
    "especialidad": "Python y Django",
    "redes_sociales": ["@ana_dev", "@ana_python"]
}

# Tupla con los estados posibles de un post
estados_post = ("borrador", "publicado", "archivado")

# Set de etiquetas del blog (los duplicados se eliminan solos)
etiquetas_blog = {"Python", "Django", "Web", "Backend", "Python"}

# Lista de posts: los 3 primeros son correctos y los 2 últimos tienen errores
# a propósito para probar las validaciones. El autor es el diccionario perfil_autor.
posts = [
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
        # Post incompleto: falta la clave "contenido"
        "id": 4,
        "titulo": "Introducción a funciones",
        "autor": perfil_autor,
        "tags": ["Python", "Funciones"],
        "estado": "publicado"
    },
    {
        # Post incorrecto: título vacío, tags como texto y estado inexistente
        "id": 5,
        "titulo": "",
        "contenido": "Este post tiene varios datos mal cargados.",
        "autor": perfil_autor,
        "tags": "Python",
        "estado": "eliminado"
    }
]
