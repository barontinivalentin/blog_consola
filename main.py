# main.py
# Punto de entrada: carga los posts desde posts.json, crea el objeto Blog
# y llama a la acción que corresponde a cada opción del menú.

from blog.modelos import Blog
from blog.datos import cargar_posts, guardar_posts
from blog.menu import mostrar_menu, pedir_si_no
from blog.operaciones import accion_listar, accion_buscar, accion_filtrar, accion_crear, accion_validar


def ejecutar():
    """Crea el blog con los posts cargados y mantiene el menú activo hasta salir."""
    blog = Blog("Blog de Ana", cargar_posts())

    while True:
        opcion = mostrar_menu()

        # Si la entrada no era un número, se vuelve a mostrar el menú
        if opcion is None:
            continue

        if opcion == 1:
            accion_listar(blog)
        elif opcion == 2:
            accion_buscar(blog)
        elif opcion == 3:
            accion_filtrar(blog)
        elif opcion == 4:
            accion_crear(blog)
        elif opcion == 5:
            accion_validar(blog)
        elif opcion == 6:
            guardar_posts(blog)
        elif opcion == 7:
            # Si hay cambios sin guardar, se ofrece guardarlos antes de salir
            if blog.cambios_sin_guardar and pedir_si_no("Hay cambios sin guardar. ¿Guardarlos antes de salir? (s/n): "):
                guardar_posts(blog)
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta de nuevo")


# La ejecución solo arranca si se corre este archivo directamente
if __name__ == "__main__":
    ejecutar()
