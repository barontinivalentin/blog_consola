# Blog por consola

Sistema de blog que se usa desde la terminal. Permite ver los posts, buscarlos por título, filtrarlos por tag, crear posts nuevos, validar que tengan datos correctos y guardarlos en un archivo `posts.json` para que no se pierdan al cerrar el programa.

El sistema está hecho con Programación Orientada a Objetos: los autores, los posts y el blog son clases.

## Requisitos

- Python 3.8 o superior. No usa librerías externas (solo el módulo `json`, que viene con Python).

## Cómo ejecutarlo

1. Abrí una terminal y entrá a la carpeta raíz del proyecto, donde está `main.py`:

   ```
   cd blog_consola
   ```

2. Ejecutá el archivo principal:

   ```
   python main.py
   ```

   En macOS o Linux puede ser necesario usar `python3 main.py`.

El archivo que hay que ejecutar es siempre `main.py`.

## Opciones del menú

1. **Ver todos los posts:** muestra id, título, autor y estado de cada post.
2. **Buscar por titulo:** muestra los posts cuyo título contiene el texto ingresado, sin importar mayúsculas o minúsculas.
3. **Filtrar por tag:** muestra los posts que tienen el tag ingresado, sin importar mayúsculas o minúsculas.
4. **Crear nuevo post:** pide título, contenido, tags y estado, y agrega el post al blog.
5. **Validar posts:** indica qué posts son válidos y qué error tiene cada uno de los demás.
6. **Guardar posts en JSON:** guarda todos los posts en `posts.json`.
7. **Salir:** cierra el programa. Si hay cambios sin guardar, pregunta si querés guardarlos antes.

## Estructura del proyecto

```
blog_consola/
│
├── main.py
├── README.md
├── posts.json
│
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── modelos.py
    ├── operaciones.py
    └── validaciones.py
```

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Punto de entrada. Carga los posts, crea el objeto `Blog` y llama a la acción de cada opción del menú. Usa `if __name__ == "__main__":`. |
| `posts.json` | Archivo donde se guardan los posts entre una ejecución y otra. |
| `blog/__init__.py` | Hace que Python reconozca la carpeta `blog` como un paquete. |
| `blog/modelos.py` | Las clases `Autor`, `Post` y `Blog`. |
| `blog/datos.py` | Persistencia: carga y guarda `posts.json`. También tiene los datos iniciales del blog. |
| `blog/menu.py` | Todo lo que se muestra y se pide por consola: el menú, los `input()` y la forma de mostrar resultados. |
| `blog/operaciones.py` | Una función por cada opción del menú. Conecta lo que pide el usuario con los métodos de `Blog`. |
| `blog/validaciones.py` | Los estados válidos y las reglas para validar un post. |

## Clases principales

Están en `blog/modelos.py`.

- **`Autor`:** representa a la persona que escribe. Atributos: `nombre`, `bio`, `especialidad` y `redes_sociales`.
- **`Post`:** representa una publicación. Atributos: `id`, `titulo`, `contenido`, `autor`, `tags` y `estado`. El atributo `autor` tiene que ser un objeto `Autor`; si se le pasa un texto, la clase lanza un error.
- **`Blog`:** centraliza la lógica del sistema. Tiene una lista de objetos `Post` en el atributo `posts` y los métodos `listar_posts()`, `obtener_posts()`, `buscar_por_titulo()`, `filtrar_por_tag()`, `crear_post()` y `validar_posts()`.

## Cómo se guarda y se carga la información

JSON no puede guardar objetos de Python directamente, así que los objetos se convierten a diccionarios y viceversa:

- **Para guardar** (opción 6): `Blog.to_list()` llama a `Post.to_dict()` en cada post, que a su vez llama a `Autor.to_dict()`. El resultado es una lista de diccionarios, y `guardar_posts()` de `datos.py` la escribe en `posts.json` con el módulo `json`.
- **Para cargar** (al iniciar): `cargar_posts()` de `datos.py` lee `posts.json` y convierte cada diccionario en un objeto con `Post.from_dict()`, que también crea el `Autor` con `Autor.from_dict()`. Con esa lista de objetos, `main.py` crea el `Blog`.

Si algo sale mal, el programa avisa y sigue funcionando:

- Si `posts.json` no existe, está vacío o tiene contenido inválido, se cargan los posts iniciales de `datos.py`.
- Si un post del archivo está incompleto (por ejemplo, le falta el contenido o el autor no es un diccionario), se avisa cuál es y se saltea.
- Si al guardar hay datos que no se pueden convertir a JSON, se muestra un error y no se modifica el archivo.

## Qué cambió respecto al módulo anterior

- Se agregó `blog/modelos.py` con las clases `Autor`, `Post` y `Blog`. Antes los posts y el autor eran diccionarios.
- La búsqueda, el filtrado y la validación ahora son métodos de `Blog`.
- `blog/datos.py` ahora se encarga de cargar y guardar los posts en `posts.json`. Antes los datos solo existían mientras el programa estaba abierto.
- Se agregaron al menú las opciones **Crear nuevo post** y **Guardar posts en JSON**.
- `blog/operaciones.py` ahora tiene una función por cada opción del menú, que recibe el objeto `Blog`.
- `estados_post` pasó a `blog/validaciones.py`, junto con las reglas que lo usan.

El post 4 de los datos iniciales tiene el título vacío y un estado que no existe, a propósito, para probar la opción de validación.
