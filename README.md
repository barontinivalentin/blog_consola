# Blog por consola

Sistema de blog que se usa desde la terminal. Permite ver los posts, buscarlos por título, filtrarlos por tag y validar que tengan la estructura correcta. Los datos se guardan en memoria, sin archivos ni base de datos.

## Requisitos

- Python 3.8 o superior. No usa librerías externas.

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

El archivo que hay que ejecutar es siempre `main.py`, desde la carpeta raíz. Si lo ejecutás desde otra carpeta, Python no va a encontrar el paquete `blog` y vas a ver un error de importación.

## Estructura del proyecto

```
blog_consola/
│
├── main.py
├── README.md
│
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py
```

## Qué hace cada archivo

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Archivo principal. Importa las funciones del paquete `blog` y coordina el menú. La ejecución está protegida con `if __name__ == "__main__":`. |
| `blog/__init__.py` | Hace que Python reconozca la carpeta `blog` como un paquete. Solo tiene un comentario. |
| `blog/datos.py` | Datos base: `perfil_autor`, `estados_post`, `etiquetas_blog` y la lista `posts`. |
| `blog/menu.py` | Muestra el menú y maneja la entrada del usuario con `input()`. Usa `try-except` para que el programa no se cierre si se escribe texto en lugar de un número. |
| `blog/operaciones.py` | Listar posts, buscar por título y filtrar por tag. Las búsquedas usan `.lower()` para ignorar mayúsculas y minúsculas. |
| `blog/validaciones.py` | Revisa que cada post tenga las claves obligatorias, título y contenido no vacíos, autor como diccionario con nombre, tags como lista y un estado válido. |

## Opciones del menú

1. **Ver todos los posts:** muestra título, autor y estado de cada post.
2. **Buscar por titulo:** muestra los posts cuyo título contiene el texto ingresado.
3. **Filtrar por tag:** muestra los posts que tienen el tag ingresado.
4. **Validar posts:** indica qué posts son válidos y qué error tiene cada uno de los demás.
5. **Salir:** cierra el programa.

Los posts 4 y 5 de `blog/datos.py` tienen errores cargados a propósito para probar la opción de validación.
